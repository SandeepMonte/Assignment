
# Flask Avatar Generator and User Search

This Flask application provides two endpoints: one for generating circular avatars based on user data and another for searching users by name, email, and location.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies using pip:
   ```
   pip install flask pillow
   ```

## Usage

1. Run the Flask app:
   ```
   python main.py
   ```
2. Access the following endpoints:

   - **Generate Avatar** (POST): `/generate_avatar`
     - Input: User name and gender (male, female, or unspecified)
     - Output: Base64-encoded circular avatar image

   - **Search Users** (GET): `/search_users?q=<search_query>`
     - Input: Query parameter (`q`) for searching users
     - Output: List of matching user data

## Example Requests

1. Generate Avatar:
   - POST request to `http://localhost:5000/generate_avatar`
   - Form data: `name=John Doe` and `gender=male`

2. Search Users:
   - GET request to `http://localhost:5000/search_users?q=John`
   - Returns users matching the query (by name, email, or location)

## Notes

- Customize the avatar generation logic and user data as needed.
- Ensure proper error handling and validation in a production environment.

---

Feel free to enhance this README with additional details, deployment instructions, or any other relevant information. Good luck with your project! 😊  

---
**Note**: The provided README is a starting point. You can expand it further by adding sections like "Deployment," "Contributing," "License," and any other relevant information specific to your project.
