from config import API_URL
from storage_manager import save_email, get_current_email, delete_email
from utils import request_with_retry, validate_choice

# Update the API_URL for the new API
API_URL = "https://www.1secmail.com/api/v1/"

def generate_email():
    if get_current_email():
        print("[+] An email already exists.")
        return get_current_email()

    response = request_with_retry(f"{API_URL}?action=genRandomMailbox&count=1")
    email = response.json()[0]
    save_email(email)
    print(f"[+] Temporary email generated: {email}")
    return email

def check_inbox():
    email = get_current_email()
    if not email:
        print("[!] No email generated yet.")
        return []

    username, domain = email.split('@')
    response = request_with_retry(f"{API_URL}?action=getMessages&login={username}&domain={domain}")
    messages = response.json()

    if messages:
        print("Inbox:")
        for i, msg in enumerate(messages, start=1):
            print(f"\n{i}. From: {msg['from']} | Subject: {msg['subject']} | Date: {msg['date']}\n")
            print('-' * 50)

        if validate_choice("\n[1] Read Email\n[2] Return to Menu\n\nEnter choice: ", ['1', '2']) == '1':
            choice = int(validate_choice("\nChoose Email (number): ", [str(i) for i in range(1, len(messages) + 1)])) - 1
            read_email(username, domain, messages[choice]['id'])
    else:
        print("[!] Inbox is empty.")

    return messages

def read_email(username, domain, email_id):
    response = request_with_retry(f"{API_URL}?action=readMessage&login={username}&domain={domain}&id={email_id}")
    message = response.json()
    print(f"\nFrom: {message['from']}\nSubject: {message['subject']}\nDate: {message['date']}\n\n{message['textBody']}\n")
    print('-' * 50)

def reset_email():
    delete_email()
    print("[+] Temporary email has been reset.")
    return generate_email()
