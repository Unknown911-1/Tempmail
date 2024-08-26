# Temporary Email Generator

## Overview

This Python script provides functionality for managing temporary email addresses. It allows you to generate a new temporary email address, check inbox messages, reset or delete the temporary email, and more. This script is useful for managing disposable email addresses for various purposes.

## Features

- **Generate Temporary Email**: Creates a new temporary email address.
- **Check Inbox**: View received emails and read them.
- **Reset Email**: Delete the current temporary email and generate a new one.
- **Delete Email**: Permanently delete the current temporary email and generate a new one.
- **Refresh Inbox**: Update the inbox view with the latest messages.
- **Copy Email**: Copy the displayed email address to the clipboard.
- **Graphical User Interface (GUI)**: Includes a GUI for easier interaction with the temporary email service.
- **Command-Line Interface (CLI)**: Supports a CLI for use in terminal environments.

## Prerequisites

- Python 3.x
- `requests` library
- `tkinter` library (comes pre-installed with Python, used for GUI)
- `pyperclip` library (for clipboard functionality)

To install the required libraries, you can use pip:

```bash
pip install -r requirements.txt
```

## Usage

### Running the GUI

1. **Run the Script**

   Execute the script using Python:

   ```bash
   python tempmail.py
   ```

2. **Using the GUI**

   - **Generate a New Email**: Click on the "Change Email" button if no email is currently displayed.
   - **Check Inbox**: Click on "Refresh Inbox" to view the latest messages.
   - **Delete Email**: Click on "Delete Email" to delete the current email and generate a new one.
   - **Copy Email**: Click on "Copy" to copy the displayed email address to the clipboard.
   - **Interact with Inbox**: Double-click on a message in the inbox to read its content.

### Running the CLI

1. **Run the Script with CLI Option**

   Execute the script with the `cli` argument:

   ```bash
   python tempmail.py cli
   ```

2. **Select an Option**

   You'll be presented with a menu. Enter the number corresponding to the action you want to perform:

   1. **Generate a new temporary email.**
   2. **Check inbox for received messages.**
   3. **Reset the current temporary email.**
   4. **Delete the current temporary email.**
   5. **Exit the application.**

3. **Follow the Prompts**

   The script will prompt you to make further choices based on the option selected.

## How It Works

- **Generate**: If no temporary email exists, a new one is generated using the [1secmail API](https://www.1secmail.com/).
- **Check Inbox**: Retrieves and displays messages from the temporary email's inbox.
- **Reset**: Deletes the current email file and generates a new temporary email.
- **Delete**: Deletes the current email file and generates a new temporary email.
- **Refresh**: Updates the inbox view with the latest messages.
- **Copy**: Copies the displayed email address to the clipboard (GUI only).

## Notes

- The temporary email address is stored in `email.txt` in the current directory.
- Ensure that the `email.txt` file is handled securely as it contains sensitive information.
- The GUI provides a user-friendly interface for managing the temporary email.
- The CLI provides a terminal-based interface for managing the temporary email.

## License

This project is licensed under the MIT License.

## Support This Project

If you find this script useful and would like to support further development, consider donating using cryptocurrency!

### Bitcoin
Address: `32VaadWB1EkD18hoE8t5pGqRmyD5g4CV9A`

[![Bitcoin QR Code](https://github.com/user-attachments/assets/83bbedff-f793-4797-9a50-391ab8a2a838)](https://github.com/user-attachments/assets/83bbedff-f793-4797-9a50-391ab8a2a838)

### Ethereum
Address: `0x673ffaA78F49CF7f3627178EDaf512F58160e3ED`

[![Ethereum QR Code](https://github.com/user-attachments/assets/e537afb6-cc0f-4ef6-9beb-0a9002a32014)](https://github.com/user-attachments/assets/e537afb6-cc0f-4ef6-9beb-0a9002a32014)

### USDT (TRC-20)
Address: `TMcVnY3CyqEfgqCwhunzGjJdwsR4WSZZc9`

[![USDT QR Code](https://github.com/user-attachments/assets/d4666b3a-bbca-42d5-85c0-df4e21b96203)](https://github.com/user-attachments/assets/d4666b3a-bbca-42d5-85c0-df4e21b96203)
```