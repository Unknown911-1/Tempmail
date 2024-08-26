import json
import os

EMAIL_FILE = "Tempmail/temp_email.json"

def save_email(email):
    with open(EMAIL_FILE, 'w') as file:
        json.dump({"email": email}, file)

def get_current_email():
    if os.path.exists(EMAIL_FILE):
        with open(EMAIL_FILE, 'r') as file:
            data = json.load(file)
            return data.get("email")
    return None

def delete_email():
    if os.path.exists(EMAIL_FILE):
        os.remove(EMAIL_FILE)
