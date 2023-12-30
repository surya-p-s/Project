from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import os
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re

# Libaries Imports to read from given source
import PyPDF2
import docx
import requests
from bs4 import BeautifulSoup

# Initialize NLP components
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

# Function to preprocess text
def preprocess(text):
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

# Function to read PDF document
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            text += reader.getPage(page_num).extractText()
        return text

# Function to read docx document
def read_docx(file_path):
    doc = docx.Document(file_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text

def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to fetch and parse web content
def fetch_web_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # will raise an HTTPError if the HTTP request returned an unsuccessful status code
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.get_text()
    except requests.HTTPError as e:
        return "Error: " + str(e)
    

# Global variable to store all data
all_data = []

# Function to load data from files and web
def load_data(sources):
    global all_data
    for source in sources:
        if isinstance(source, str):  # If the source is a file path
            if source.endswith('.pdf'):
                all_data.append(read_pdf(source))
            elif source.endswith('.docx'):
                all_data.append(read_docx(source))
            elif source.endswith('.txt'):
                all_data.append(read_text(source))
            else:
                print(f"Unsupported file format: {source}")
        elif isinstance(source, dict) and 'url' in source:  # If the source is a web URL
            all_data.append(fetch_web_content(source['url']))


def chat_bot(message):
    tokenized = preprocess(message)
    result = 0
    confidence = 0

    for data in all_data:
        if tokenized in preprocess(data):
            return "Here is something I found: " + data[:200]  # Example response

    return "Sorry, I did not understand you or find relevant information."

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

# Load the data
sources = [
    # 'path_to_file1.pdf', 
    # 'path_to_file2.docx',
    {'url': 'https://legislative.gov.in/'}
]
load_data(sources)
root.mainloop()