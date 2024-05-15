from flask import Flask, request, jsonify
from PIL import Image, ImageDraw, ImageFont


import base64
app = Flask(__name__)
# Pass the data
users = [
    {'name': ' ', 'email': ' ', 'gender': ' '}
]

@app.route('/generate_avatar', methods=['POST'])
def generate_avatar():
    user_name = request.form.get('name')
    user_gender = request.form.get('gender')
    # Get user's name
    initials = user_name[:2].upper()  # Take the first two letters as initials
    if user_gender.lower() == 'male':
        background_color = '#1976D2'  # Blue for male
    elif user_gender.lower() == 'female':
        background_color = '#E91E63'  # Pink for female
    else:
        background_color = '#9E9E9E'  # Grey for unspecified gender
    # Create a circular avatar image
    img = Image.new('RGB', (150, 150), color=background_color)
    img_draw = ImageDraw.Draw(img)
    img_draw.text((20, 60), initials, fill='white', font=ImageFont.load_default())
    # Convert image to base64
    img_bytes = img.tobytes()
    img_base64 = base64.b64encode(img_bytes).decode()
    return jsonify({'avatar': img_base64})
@app.route('/search_users', methods=['GET'])
def search_users():
    query = request.args.get('q')  # Get search query from request URL parameter
    # Search for users by name, email, and location
    results = [user for user in users if query.lower() in user['name'].lower()
               or query.lower() in user['email'].lower()
               or query.lower() in user['location'].lower()]
    return jsonify({'results': results})
if __name__ == '__main__':
    app.run(debug=True)
