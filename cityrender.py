# from flask import Flask, jsonify
# import os

# app = Flask(__name__)


# folder = "./assets/"
# with open(json)
# folder+ image_name
# @app.route('/images', methods=['GET'])
# def get_images():
#     image_paths = [
#         'image1.jpg',
#         'image2.jpg',
#         'image3.jpg',
#         'image4.jpg',
#         'image5.jpg',
#         'image6.jpg',
#         'image7.jpg',
#         'image8.jpg',
#         'image9.jpg',
#         'image10.jpg',
#     ]

#     image_data = []

#     for image_path in image_paths:
#         image_path = os.path.join('path/to/your/image/directory', image_path)  # Update the path
#         if os.path.exists(image_path):
#             with open(image_path, 'rb') as f:
#                 image_bytes = f.read()
#                 image_data.append({
#                     'image_name': image_path.split('/')[-1],
#                     'image_data': image_bytes.decode('latin-1')
#                 })

#     return jsonify(images=image_data)

# if __name__ == '__main__':
#     app.run(debug=True)
