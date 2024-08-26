import tkinter as tk
from tkinter import messagebox, ttk
from email_manager import generate_email, check_inbox, reset_email, delete_email, get_current_email, read_email


banner = '''\n
      #####    #     #      #     #    #    ### #           #####  ####### #     #     
     #     #  ##    ##      ##   ##   # #    #  #          #     # #       ##    #     
     #     # # #   # #      # # # #  #   #   #  #          #       #       # #   #     
      ######   #     #      #  #  # #     #  #  #          #  #### #####   #  #  #     
           #   #     #      #     # #######  #  #          #     # #       #   # # ### 
     #     #   #     #      #     # #     #  #  #          #     # #       #    ## ### 
      #####  ##### #####    #     # #     # ### #######     #####  ####### #     # ### 

'''

def console_ui():
    while True:
        print(banner)
        print('''\n
          [1] Generate Temporary Email 
          [2] Check Inbox
          [3] Reset Email
          [4] Delete Email
          [5] Exit
        ''')

        choice = input('[~] Enter your choice: ')
        if choice == '1':
            generate_email()
        elif choice == '2':
            check_inbox()
        elif choice == '3':
            reset_email()
        elif choice == '4':
            delete_email()
        elif choice == '5':
            break
        else:
            print("[!] Invalid choice. Please select a valid option.")


def update_email_label(label):
    email = get_current_email()
    if email:
        label.config(text=email)
    else:
        email = generate_email()
        label.config(text=email)

def copy_email_to_clipboard(root):
    email = get_current_email()
    if email:
        root.clipboard_clear()
        root.clipboard_append(email)
        messagebox.showinfo("Success", "Email copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No email to copy!")

def refresh_inbox(tree):
    email = get_current_email()
    if email:
        inbox_messages = check_inbox()
        tree.delete(*tree.get_children())  # Clear previous inbox items
        for i, msg in enumerate(inbox_messages):
            tree.insert('', 'end', iid=i, text=f"Message {i+1}",
                        values=(msg['from'], msg['subject'], msg['id']))

def on_inbox_item_click(event, tree):
    selected_item = tree.selection()
    if selected_item:
        item_id = tree.item(selected_item)['values'][2]  # Extract message ID
        email = get_current_email()
        username, domain = email.split('@')
        read_email(username, domain, item_id)

def start_gui():
    root = tk.Tk()
    root.title("Temp Mail")
    root.geometry("600x500")
    root.configure(bg="#2b2b2b")

    # Email Display Frame
    email_frame = tk.Frame(root, bg="#2b2b2b")
    email_frame.pack(pady=20)

    email_label = tk.Label(email_frame, text="Your Temporary Email Address", fg="#ffffff", bg="#2b2b2b", font=("Arial", 14))
    email_label.pack()

    email_display = tk.Label(email_frame, text="No email generated yet", fg="#00e676", bg="#1e1e1e", font=("Arial", 12), wraplength=400, relief="solid", padx=10, pady=5)
    email_display.pack(pady=10)

    # Button Frame
    button_frame = tk.Frame(root, bg="#2b2b2b")
    button_frame.pack(pady=10)

    copy_button = ttk.Button(button_frame, text="Copy", command=lambda: copy_email_to_clipboard(root))
    copy_button.grid(row=0, column=0, padx=10)

    refresh_button = ttk.Button(button_frame, text="Refresh Inbox", command=lambda: refresh_inbox(inbox_tree))
    refresh_button.grid(row=0, column=1, padx=10)

    change_button = ttk.Button(button_frame, text="Change Email", command=lambda: reset_email())
    change_button.grid(row=0, column=2, padx=10)

    delete_button = ttk.Button(button_frame, text="Delete Email", command=lambda: delete_email())
    delete_button.grid(row=0, column=3, padx=10)

    # Inbox Frame
    inbox_frame = tk.Frame(root, bg="#2b2b2b")
    inbox_frame.pack(pady=20, fill='x')

    inbox_label = tk.Label(inbox_frame, text="Inbox", fg="#ffffff", bg="#2b2b2b", font=("Arial", 12))
    inbox_label.pack()

    inbox_tree = ttk.Treeview(inbox_frame, columns=('Sender', 'Subject', 'ID'), show='headings', selectmode='browse')
    inbox_tree.heading('Sender', text='Sender')
    inbox_tree.heading('Subject', text='Subject')
    inbox_tree.column('ID', width=0, stretch=tk.NO)  # Hide the ID column

    inbox_tree.pack(fill='x', padx=10, pady=5)
    inbox_tree.bind('<Double-1>', lambda event: on_inbox_item_click(event, inbox_tree))

    # Automatically generate email if none exists
    update_email_label(email_display)
    refresh_inbox(inbox_tree)

    root.mainloop()
