from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import os
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import json
import re

# Imports to read from given source

# loading intents file for intent recognition

json_file_path='.//bot/kb.json'

if os.path.exists(json_file_path):
    with open(json_file_path) as intent_file:
        intents = json.load(intent_file)
        # print(intents)
else:
    messagebox.showerror("Error","Unable to locate JSON file.")
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

def chat_bot(message):
    tokenized = preprocess(message)
    result = None
    confidence = 0

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            tokenized_pattern = preprocess(pattern)
            if tokenized_pattern == tokenized:
                result = intent['tag']
                confidence = 1.0
                break
            elif re.search(r'\b' + tokenized_pattern + r'\b', tokenized):
                result = intent['tag']
                confidence += 0.2
            elif tokenized_pattern in tokenized:
                result = intent['tag']
                confidence += 0.1

    response = ""
    if confidence >= 0.2 and result is not None:
        for intent in intents['intents']:
            if intent['tag'] == result:
                response = intent['responses'][0]
                break
    else:
        response = "Sorry, I did not understand you"

    return response


# main chat interface
def send():
    message = entryField.get("1.0",'end-1c')
    entryField.delete("1.0",'end')
    ChatLog.config(state='normal')
    ChatLog.insert('end', "User: " + message + '\n')
    ChatLog.config(foreground='gray')

    response = chat_bot(message)
    ChatLog.insert('end', "ChatBot: " + response + '\n')

    ChatLog.config(state='disabled')
    ChatLog.yview('moveto', '1.0')

root = Tk()
root.title("E-Lawyer")

# Set background color and add background image (replace 'background_image.png' with your image file)
# background_image = PhotoImage(file='back2.png')
# background_label = Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)

ChatLog = Text(root, bd=0, bg="white", height="8", width="50", font="Arial", relief=GROOVE, borderwidth=5, wrap=WORD)
ChatLog.config(state='disabled')

label = Label(root, text="ChatBot", font=('Arial', 16, 'bold'), bg='#32a8a6', fg='white', padx=20, pady=10)  # Add label for a cleaner layout

# Create a themed style to apply a shadow effect
style = ttk.Style()
style.configure("TButton", relief="flat", borderwidth=5, font=('Arial', 12, 'bold'), background='#4CAF50', foreground='white')
style.map("TButton", background=[("active", '#45a049')])

SendButton = ttk.Button(root, text="Send", command=send, style="TButton")
SendButton.grid(row=2, column=1, pady="10", padx="20", sticky='nsew')

# Entry field shadow effect
entryField = Text(root, bd=0, bg="white", height="3", width="50", font="Arial", relief=GROOVE, borderwidth=5, wrap=WORD)
entryField.grid(row=2, column=0, pady="10", padx="20", sticky='nsew')

# Add a shadow effect to the widgets
# def add_shadow(widget):
#     shadow = ttk.Frame(widget, style="TFrame", height=widget.winfo_reqheight(), width=widget.winfo_reqwidth())
#     shadow.place(x=widget.winfo_x(), y=widget.winfo_y())

# add_shadow(entryField)
# add_shadow(SendButton)
# add_shadow(ChatLog)

# Grid layout
label.grid(row=0, column=0, columnspan=2, pady="10")
ChatLog.grid(row=1, column=0, columnspan=2, pady="20", padx="20", sticky='nsew')

# Adjust row and column weights for resizing
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Make Enter key trigger the send function
entryField.bind("<Return>", lambda event=None: send())


root.mainloop()