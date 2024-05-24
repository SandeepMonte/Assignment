import io

from flask import Flask, request, jsonify
from PIL import Image, ImageDraw, ImageFont
import db
import base64
import sqlite3

app = Flask(__name__)
users = [
    {'name': 'John Doe', 'email': 'john@example.com', 'location': 'New York', 'gender': 'male'},
    {'name': 'Jane Smith', 'email': 'jane@example.com', 'location': 'Los Angeles', 'gender': 'female'}
]

groups = []
events = []
#conn = db.connect_to_database()
conn = sqlite3.connect('example.db')

# Task 1: Generate user profile image
@app.route('/generate_avatar', methods=['POST'])
def generate_avatar():
    user_name = request.form.get('name')
    user_gender = request.form.get('gender')

    # Validate inputs
    if not user_name or not user_gender:
        return jsonify({'error': 'Name and gender are required'}), 400

    # Get user's name
    initials = user_name[:2].upper()  # Take the first two letters as initials
    if user_gender.lower() == 'male':
        background_color = '#1976D2'  # Blue for male
    elif user_gender.lower() == 'female':
        background_color = '#E91E63'  # Pink for female
    else:
        background_color = '#9E9E9E'  # Grey for unspecified gender

    # Create an avatar image
    img = Image.new('RGB', (150, 150), color=background_color)
    img_draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    text_width, text_height = img_draw.textsize(initials, font=font)
    position = ((150 - text_width) / 2, (150 - text_height) / 2)
    img_draw.text(position, initials, fill='white', font=font)

    # Convert image to base64
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    img_base64 = base64.b64encode(buffer.getvalue()).decode()

    # Store the generated avatar in the user profile (simulate update)
    for user in users:
        if user['name'] == user_name:
            user['avatar'] = img_base64
            break

    return jsonify({'avatar': img_base64})

# Task 2: Search for users
@app.route('/search_users', methods=['GET'])
def search_users():
    query = request.args.get('q')  # Get search query from request URL parameter

    # Validate input
    if not query:
        return jsonify({'error': 'Search query is required'}), 400

    # Search for users by name, email, and location
    results = [user for user in users if query.lower() in user['name'].lower()
               or query.lower() in user['email'].lower()
               or query.lower() in user['location'].lower()]
    return jsonify({'results': results})

# Additional functionality for creating groups and scheduling events
@app.route('/create_group', methods=['POST'])
def create_group():
    group_name = request.form.get('group_name')
    members = request.form.getlist('members')  # List of member names

    if not group_name or not members:
        return jsonify({'error': 'Group name and members are required'}), 400

    group = {
        'group_name': group_name,
        'members': members
    }
    groups.append(group)
    return jsonify({'message': 'Group created successfully', 'group': group})

@app.route('/schedule_event', methods=['POST'])
def schedule_event():
    event_name = request.form.get('event_name')
    event_date = request.form.get('event_date')
    event_time = request.form.get('event_time')
    group_name = request.form.get('group_name')  # Group hosting the event

    if not event_name or not event_date or not event_time or not group_name:
        return jsonify({'error': 'Event name, date, time, and group name are required'}), 400

    # Check if the group exists
    group = next((g for g in groups if g['group_name'] == group_name), None)
    if not group:
        return jsonify({'error': 'Group not found'}), 404

    event = {
        'event_name': event_name,
        'event_date': event_date,
        'event_time': event_time,
        'group_name': group_name
    }
    events.append(event)
    return jsonify({'message': 'Event scheduled successfully', 'event': event})

if __name__ == '__main__':
    app.run(debug=True)




