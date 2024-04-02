import pymongo
import bcrypt
import datetime
client = pymongo.MongoClient("mongodb+srv://abhishek:abhishek123@filamentai.dgbcetm.mongodb.net/")
db = client["Intelligent_Travelling"]

users_collection = db["User"]


def register_user(data):
   
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    city = data.get('city')
    signupdate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    highest_user = users_collection.find_one(sort=[("user_id", -1)])

    user_data = {
        'name': name,
        'email': email,
        'password': hashed_password,
        'city': city,  
        'signupdate':signupdate
    }
    

    users_collection.insert_one(user_data)
    
    return {'message': 'User registered successfully!'}, 200
def email_exists_in_database(email):
           user =users_collection.find_one({"email": email})
           if user:
               return True
           else:
               return False
def extract_name_from_email(email):
    user_document = users_collection.find_one({"email": email})
    
    # If user document exists and has a name field, extract the name
    if user_document and "name" in user_document:
        name = user_document["name"]
        return name
    else:
        return None

def retrieve_data_from_database(email):
    # Check if the email exists in the database
    user = users_collection.find_one({"email": email})
    if user:
        # Create a new dictionary with the required fields
        user_data = {
            "name": user.get("name"),
            "city": user.get("city"),
            "email": user.get("email")
        }
        return user_data
    else:
        # Return None if the email does not exist
        return None
# input=retrieve_data_from_database('mira@gmail.com')
# print(input)
def logout_user(email):
    # Check if the email exists in the database
    user = users_collection.find_one({"email": email})
    if user:
        # If the user exists, delete the user's data from the database
        users_collection.delete_one({"email": email})
        return {'message': 'User logged out successfully!'}, 200
    else:
        # Return an error message if the email does not exist
        return {'error': 'User not found'}, 404
    
def extract_city_names_from_collection():
    # Fetch all documents from the collection
    all_data = list(users_collection.find({}))  # Retrieve all documents
    city_names = []
    
    for entry in all_data:
        city = entry['city']
        city_names.append(city)

    return city_names

city_names = extract_city_names_from_collection()
# print(city_names)

# print(email_exists_in_database(''))
def check_password(email, password):
    # Retrieve the user document from the database based on the provided email
    user = users_collection.find_one({"email": email})
    if user:
        # Retrieve the hashed password stored in the database for the user
        hashed_password = user.get('password')
        # Check if the provided password matches the hashed password in the database
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            return True  # Passwords match
        else:
            return False  # Passwords don't match
    else:
        return False  # User with the provided email doesn't exist
    
# print(retrieve_data_from_database('jiya@gmail.com'))