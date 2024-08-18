import requests
import os
import time

email_file = 'email.txt'

def options():
    clear_screen()

    current_email = get_current_email() or "No email generated yet"

    print(f'''
      Current Email: {current_email}

      [1] Generate Temporary Email 
      [2] Check Inbox
      [3] Reset Email
      [4] Delete Email
      [5] Exit
    ''')

    choice = int(input('[~] Enter your choice: '))
    if choice == 1:
        generate()
    elif choice == 2:
        check_inbox()
    elif choice == 3:
        reset_email()
    elif choice == 4:
        delete_email()
    elif choice == 5:
        exiting()
    else:
        print("[!] Invalid choice. Please select a valid option.")
        time.sleep(10)
        options()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate():
    if os.path.exists(email_file) and os.path.getsize(email_file) > 0:
        print("[+] An email already exists.")
        options()
        return

    response = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
    email = response.json()[0]

    with open(email_file, "w") as file:
        file.write(email)

    print(f"[+] Temporary email generated: {email}")
    time.sleep(6)
    options()

def read_email(username, domain, email_id):
    response = requests.get(f"https://www.1secmail.com/api/v1/?action=readMessage&login={username}&domain={domain}&id={email_id}")
    message = response.json()
    print(f"\nFrom: {message['from']}\nSubject: {message['subject']}\nDate: {message['date']}\n\n{message['textBody']}\n")
    print('-' * 50)
    print("[~] Go Back....")
    choice = input("[~] Go Back....Y/n: ")
    if choice.lower() == 'y':
        check_inbox()
    else:
        exiting()

def check_inbox():
    email = get_current_email()
    if not email:
        options()
        return

    username, domain = email.split('@')
    response = requests.get(f"https://www.1secmail.com/api/v1/?action=getMessages&login={username}&domain={domain}")
    messages = response.json()

    if messages:
        print("Inbox:")
        for i, msg in enumerate(messages, start=1):
            print(f"\n{i}. From: {msg['from']} | Subject: {msg['subject']} | Date: {msg['date']}\n")
            print('-' * 50)

        read = input("\n1. Read Inbox\n2. Return to Menu\n\n[~] Enter choice: ")
        if read == "1":
            choice = input("\n[~] Choose Inbox: ")
            if choice.isdigit():
                choice = int(choice) - 1
                if 0 <= choice < len(messages):
                    read_email(username, domain, messages[choice]['id'])
                else:
                    print("[!] Invalid choice.")
                    options()
            else:
                print("[!] Invalid input. Please enter a number.")
                options()
        else:
            options()
    else:
        print("[!] Inbox is empty.")
        time.sleep(10)
        options()

def get_current_email():
    if os.path.exists(email_file):
        with open(email_file, "r") as file:
            return file.read().strip()
    else:
        return None

def reset_email():
    if os.path.exists(email_file):
        os.remove(email_file)
        print("[+] Temporary email has been reset.")
        print("[+] Generating new temporary email...")
        generate()
    else:
        print("[-] No temporary email to reset.")
        time.sleep(10)
        options()

def delete_email():
    if os.path.exists(email_file):
        with open(email_file, "r") as file:
            email = file.read().strip()
        os.remove(email_file)
        print(f"[+] {email}: Temporary email has been deleted.")
        options()
    else:
        print("[-] No temporary email to delete.")
        time.sleep(10)
        options()

def exiting():
    print("[+] Exiting...")
    quit()
