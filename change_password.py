import pymongo

client = pymongo.MongoClient("mongodb+srv://abhishek:abhishek123@filamentai.dgbcetm.mongodb.net/")
db = client["Intelligent_Travelling"]
users_collection = db["User"]


def change_password(email, newpassword):
    try:
        # user = users_collection.find_one({"email": email})
        user = users_collection.find_one({"email": {"$regex": f"^{email}$", "$options": "i"}})

        print(user)
        if user:
            users_collection.update_one({"email": email}, {"$set": {"password": newpassword}})
            return {'message': 'Password changed successfully!'}
        else:
            return {'message': 'User not found.'}
            
    except Exception as e:
        return {'message': f'An error occurred: {str(e)}'}
