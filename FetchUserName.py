import pymongo

URL = "mongodb+srv://abhishek:abhishek123@filamentai.dgbcetm.mongodb.net/Intelligent_Travelling"
DATABASE_NAME = "Intelligent_Travelling"
COLLECTION_NAME = "User"


def fetch_user_name(email):
    try:
        client = pymongo.MongoClient(URL)
        db = client.get_database(DATABASE_NAME)
        collection = db.get_collection(COLLECTION_NAME)
        found_user = collection.find_one({"email": email})

        if found_user:
            full_name = found_user.get("name")
            first_name = full_name.split()
            return first_name[0]
        else:
            return None

    except Exception as e:
        print("Error:", str(e))
        return None
