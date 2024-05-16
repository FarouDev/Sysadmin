import subprocess
import tkinter as tk
from tkinter import scrolledtext

# Function to execute system commands and capture the output
def get_system_info():
    info = {}
    info['Computer name'] = subprocess.getoutput('echo %COMPUTERNAME%')
    info['Current user'] = subprocess.getoutput('echo %USERNAME%')
    info['List of users'] = subprocess.getoutput('net user')
    info['Domain'] = subprocess.getoutput('echo %USERDOMAIN%')
    info['IP addresses'] = subprocess.getoutput('ipconfig | findstr /R /C:"IPv4 Address"')
    return info

# Function to update the text area with system information
def display_info():
    info = get_system_info()
    text_area.delete('1.0', tk.END)
    for key, value in info.items():
        text_area.insert(tk.END, f"{key}:\n{value}\n\n")

# Create the main window
root = tk.Tk()
root.title("whoami beta v.01 ")

# Create a scrolled text area widget
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
text_area.pack(padx=10, pady=10)

# Create a button to trigger the information display
display_button = tk.Button(root, text="Display Info", command=display_info)
display_button.pack(pady=10)

# Run the application
root.mainloop()
