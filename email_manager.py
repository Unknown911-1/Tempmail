import requests

def get_current_email():
    try:
        with open('Tempmail/email.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def check_inbox():
    email = get_current_email()
    if not email:
        raise ValueError("No email address found.")
    username, domain = email.split('@')
    response = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}")
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def read_email(username, domain, message_id):
    response = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={message_id}")
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def generate_email():
    response = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
    if response.status_code == 200:
        email = response.json()[0]
        with open('Tempmail/email.txt', 'w') as file:
            file.write(email)
        return email
    else:
        response.raise_for_status()

def reset_email():
    open('Tempmail/email.txt', 'w').close()

def delete_email():
    email = get_current_email()
    if email:
        username, domain = email.split('@')
        response = requests.get(f"https://www.1secmail.com/api/v1/?action=deleteMailbox&login={username}&domain={domain}")
        if response.status_code == 200:
            open('Tempmail/email.txt', 'w').close()
        else:
            response.raise_for_status()
    else:
        raise ValueError("No email address found.")
