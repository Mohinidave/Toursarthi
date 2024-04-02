import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb+srv://abhishek:abhishek123@filamentai.dgbcetm.mongodb.net/")
db = client["Intelligent_Travelling"]
errors_collection = db["errors"]


def error_to_database(error_detail):
    current_datetime = datetime.now()

    error_document = {

        "date": current_datetime.date().strftime("%Y-%m-%d"),
        "time": current_datetime.time().strftime("%H:%M:%S"),
        "error_detail": error_detail
    }

    result = errors_collection.insert_one(error_document)
    if result.inserted_id:
        print(f"Crash details stored in the database with ID: {result.inserted_id}")
    else:
        print("Error storing details in the database.")