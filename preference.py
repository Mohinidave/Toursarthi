import pymongo
  
client = pymongo.MongoClient("mongodb+srv://abhishek:abhishek123@filamentai.dgbcetm.mongodb.net/")
db = client["Intelligent_Travelling"]

users_collection = db["preference"]


def preference_info(data):
   
    name=data.get('name')
    email = data.get('email')
    catagories=data.get('catagories')
    
    preference_data = {
        
        'name':name,
        'email': email,
        'categories':catagories
        
        
    }
    users_collection.insert_one(preference_data)

    return {'message': 'Preferences Added Sucessfully'}, 200
def retrieve_preference_info(email):
    # Find documents in the collection where the email field matches the specified email
    cursor = users_collection.find({"email": email})
    
    # Initialize an empty list to store the results
    preference_data = []
    
    # Iterate over the cursor to extract data from documents
    for document in cursor:
        preference_data.append(document)
    
    return preference_data[0]['categories']
# data=retrieve_preference_info('mira@gmail.com')
