import pymongo
from flask import jsonify
  
client = pymongo.MongoClient("mongodb+srv://abhishek:abhishek123@filamentai.dgbcetm.mongodb.net/")
db = client["Intelligent_Travelling"]

users_collection = db["Feedback"]


def feedback_info(data):
   
    
    email = data.get('email')
    comment=data.get('comment')
    rating=data.get('rating')
    
    feedback_data = {
        
        'email': email,
        'comment':comment,
        'rating':rating
        
    }
    users_collection.insert_one(feedback_data)

    return {'message': 'Feedback inserted Successfully'}, 200
def get_feedback_info():
    # Fetch feedback data from MongoDB collection
    feedback_data = list(users_collection.find({}, {"_id": 0}))  
    print(feedback_data)        # Exclude _id field from the result
    return feedback_data

data=get_feedback_info()
print(data)
def calculate_feedback_statistics(feedback_data):
    # Create a dictionary to store rating counts
    rating_counts = {}

    # Calculate total number of ratings
    total_ratings = len(feedback_data)

    # Count the number of occurrences for each rating
    for feedback in feedback_data:
        rating = feedback['rating']
        if rating in rating_counts:
            rating_counts[rating] += 1
        else:
            rating_counts[rating] = 1

    # Calculate percentage for each rating
    feedback_statistics = []
    for rating, count in rating_counts.items():
        percentage = (count / total_ratings) * 100
        rating_info = {
            "rating": rating,
            "count": count,
            "percentage": round(percentage, 2)
        }
        feedback_statistics.append(rating_info)

    return feedback_statistics

# Example usage:


feedback_statistics = calculate_feedback_statistics(data)
# print(feedback_statistics)