import requests
import time

def request_with_retry(url, retries=3, delay=2):
    for _ in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"[!] Error: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)
    raise Exception("[!] Failed to retrieve data after several retries.")

def validate_choice(prompt, valid_choices):
    choice = input(prompt)
    while choice not in valid_choices:
        print("[!] Invalid choice. Please select a valid option.")
        choice = input(prompt)
    return choice
