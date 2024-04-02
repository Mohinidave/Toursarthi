from flask_bcrypt import Bcrypt
from flask import Flask, request, jsonify, session
from register import *
from login import *
from reset_password import *
from OTP_validation import *
from change_password import *
from preference import *
from feedback import *
from flask import Flask, session, request
from flask_session import Session
from pymongo import MongoClient
from Dashboard import (
    CITY_IMAGE_10,
    SPOT_IMAGE_10,
    STATE_IMAGE_10,
    UT_IMAGE_10,
    BEST_SELLER_10,
)
from FetchUserName import fetch_user_name
from detailedScreeninfo import (
    extract_tourist_spots_by_ut_name,
    extract_random_tourist_spots_in_city,
    extract_random_tourist_spot_names_in_state,
    extract_city_info,
    extract_cities_in_state,
    extract_state_info,
    extract_tourist_spot_info,
    extract_tourist_spots_in_city,
    extract_cities_in_state_list,
    extract_unionterritory_info,
    extract_cities_in_state,
)
import json
from feedback import get_feedback_info, calculate_feedback_statistics
from flask import jsonify
from wheatherapi import weatherapi, get_city_coordinates, temperature_city
from bson import json_util
from error_log import *
from bson import ObjectId

with open("IndianJson.json", "r") as file:
    json_data = json.load(file)


emaillist = []

app = Flask(__name__)


app.config["PERMANENT_SESSION_LIFETIME"] = 3600
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
all_the_tourist_spot = None
days = 0


@app.route("/register", methods=["GET", "POST"])
def register_route():
    data = request.get_json()
    email = data.get("email")

    # Initialize emaillist from session
    emaillist = session.get("emaillist", [])

    # Append the new email to the emaillist
    emaillist.append(email)

    # Store the updated emaillist in the session
    session["emaillist"] = emaillist
    print(emaillist)
    print(session)

    response_data, status = register_user(data)
    return jsonify(response_data), status


@app.route("/login", methods=["POST"])
def login_route():
    data = request.get_json()
    email = data.get("email")
    TrueEmail = email_exists_in_database(email)
    print(TrueEmail)

    if TrueEmail:
        sessionemaillist = session.get("emaillist", [])
        print("sessionemaillist", sessionemaillist)

        # Update sessionemaillist if necessary
        if email not in sessionemaillist:
            sessionemaillist.append(email)
            session["emaillist"] = sessionemaillist

        response_data, status = login_user(data)
        return response_data
    else:
        error_message = "Invalid email address"
        return jsonify({"error": error_message}), 400


@app.route("/profile", methods=["POST", "GET"])
def get_profile():
    email_final = request.args.get("info")
    print(email_final)

    session_email_list = session.get("emaillist", [])
    if email_final:
        user_data = retrieve_data_from_database(email_final)
        user_preference = retrieve_preference_info(email_final)
        data = {"user_data": user_data, "user_preference": user_preference}
        return jsonify(data)
    else:
        error_message = "Data not found for the user"
        return jsonify({"error": error_message}), 404


@app.route("/send_otp", methods=["POST"])
def send_otp_route():
    try:
        data = request.get_json()
        email = data.get("email")
        if not email:
            return jsonify({"error": "Email address is required"}), 400
        if send_otp_email(email):
            return jsonify({"message": "OTP sent successfully"})
        else:
            return jsonify({"error": "Failed to send OTP"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/emailverification", methods=["POST"])
def emailverification_route():
    try:
        data = request.get_json()
        email = data.get("email")

        if email_exists_in_database(email):
            if send_otp_email(email):
                return jsonify({"message": "OTP sent successfully"}), 200
        else:
            return jsonify({"message": "Email does not exist"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/validate_otp", methods=["POST"])
def validate_otp_route():
    try:
        data = request.get_json()
        email = data.get("email")
        entered_otp = data.get("otp")

        if not entered_otp:
            return jsonify({"error": "OTP are required"}), 400
        print(f"Received email: {email}, OTP: {entered_otp}")
        if validate_otp(email, entered_otp):
            return jsonify({"message": "OTP is valid"})

        else:
            return jsonify({"error": "Invalid OTP"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/reset_password", methods=["POST"])
def change_password_route():
    try:
        data = request.get_json()
        print(data)
        email = data["fdata"]["email"]

        print(email)
        newpassword = data["fdata"]["newpassword"]

        result = change_password(email, newpassword)
        return jsonify(result)
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500


@app.route("/prefernce", methods=["POST"])
def preference_route():
    # Assuming you're using Flask's session to store the user's email
    data = request.get_json()
    email = data.get("email")
    # sessionemail=session.get('email')
    sessionemaillist = session.get("emaillist", [])
    print(sessionemaillist)

    if email in sessionemaillist:
        response_data, status = preference_info(data)
        return jsonify(response_data), status


@app.route("/image_to_dashboard", methods=["GET"])
def image_to_dashboard():
    try:
        if session["email"]:
            user_email = session["email"]
            username = fetch_user_name(user_email)
    except Exception as e:
        username = "Traveller"
    return jsonify(
        {
            "USERNAME": username,
            "BEST_SELLER_10": BEST_SELLER_10,
            "SPOT_IMAGE_10": SPOT_IMAGE_10,
            "CITY_IMAGE_10": CITY_IMAGE_10,
            "STATE_IMAGE_10": STATE_IMAGE_10,
            "UT_IMAGE_3": UT_IMAGE_10,
        }
    )


@app.route("/temperature_city", methods=["GET"])
def temperature_city():
    Info = request.args.get("info")
    temp_info = weatherapi(Info)
    #  print(temp_info)
    return jsonify(temp_info)


@app.route("/map_city", methods=["GET"])
def map_city():
    Info = extract_city_names_from_collection()
    print("Info", Info)
    city_data = get_city_coordinates(Info)
    #  print("city_data",city_data)
    return jsonify(city_data)


@app.route("/city_information", methods=["GET"])
def city_information():
    try:
        city = request.args.get("city")
        print("city", city)
        city_info = extract_city_info(json_data, city)
        # print(city_info)
        return jsonify(city_info)
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/city_touristspot_information", methods=["GET"])
def city_touristspot_information():
    try:
        city = request.args.get("city")
        tourist_info = extract_tourist_spots_in_city(json_data, city)
        return jsonify(tourist_info)
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/state_information", methods=["GET"])
def state_information():
    try:
        state = request.args.get("state")
        print("state", state)
        state_info = extract_state_info(json_data, state)
        city_in_state = extract_cities_in_state_list(json_data, state)
        # print(state_info)
        return jsonify(state_info)
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/state_information_cities", methods=["GET"])
def state_information_cities():
    try:
        state = request.args.get("state")
        print("state", state)
        city_in_state = extract_cities_in_state_list(json_data, state)
        return jsonify(city_in_state)
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/state_information_touristspot", methods=["GET"])
def state_information_touristspot():
    try:
        state = request.args.get("state")
        print("state", state)
        tourist_in_state = extract_random_tourist_spot_names_in_state(json_data, state)
        return jsonify(tourist_in_state)
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/city_information_touristspot", methods=["GET"])
def city_information_touristspot():
    try:
        city = request.args.get("city")
        print("City", city)
        tourist_in_city = extract_random_tourist_spots_in_city(json_data, city)
        return jsonify(tourist_in_city)
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/touristspot_information", methods=["GET"])
def touristspot_information():
    try:
        touristspot = request.args.get("touristspot")
        print("state", touristspot)
        touristspot_info = extract_tourist_spot_info(json_data, touristspot)
        # print(touristspot_info)
        return jsonify(touristspot_info)
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/ut_information", methods=["GET"])
def ut_information():
    try:
        ut = request.args.get("utname")
        print("unionterritory", ut)
        ut_info = extract_unionterritory_info(json_data, ut)
        print(ut_info)
        return jsonify(ut_info)
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/ut_information_touristspot", methods=["GET"])
def ut_information_touristspot():
    try:
        ut = request.args.get("utname")
        print("unionterritory", ut)
        ut_touristspot = extract_tourist_spots_by_ut_name(json_data, ut)
        print(ut_touristspot)
        return jsonify(ut_touristspot)
    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": "Internal Server Error"}), 500


@app.route("/feedback", methods=["GET", "POST"])
def feedback_route():
    data = request.args.get("error")
    response_data, status = feedback_info(data)
    return jsonify(response_data), status


@app.route("/error", methods=["GET", "POST"])
def error_route():
    data = request.get_json()
    response_data, status = error_to_database(data)
    return jsonify(response_data), status


@app.route("/feedbackanalysis", methods=["GET"])
def feedback_analysis_route():
    data = get_feedback_info()
    finaldata = calculate_feedback_statistics(data)
    return finaldata


@app.route("/logout", methods=["GET", "POST"])
def logout_route():
    # data = request.get_json()
    email = request.args.get("email")
    print(email)
    # Remove email from sessionemaillist
    sessionemaillist = session.get("emaillist", [])
    print(sessionemaillist)
    if email in sessionemaillist:
        sessionemaillist.remove(email)
        logout_user(email)
        session["emaillist"] = sessionemaillist

    session.clear()

    return jsonify({"message": "Logged out successfully"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
