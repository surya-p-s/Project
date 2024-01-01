import tkinter as tk
from tkinter import scrolledtext
import PyPDF2
import docx
import requests
from bs4 import BeautifulSoup
import re
import nltk
nltk.download('punkt')

# ... (Include the functions `preprocess`, `read_pdf`, `read_docx`, `read_text`, `fetch_web_content` here)
def preprocess(text):
    return text.lower()

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ' '.join([reader.getPage(i).extractText() for i in range(reader.numPages)])
    return text

def read_docx(file_path):
    doc = docx.Document(file_path)
    return ' '.join(paragraph.text for paragraph in doc.paragraphs)

def read_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def fetch_web_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

def find_in_text(query, content, window=100):
    query = query.lower()
    start = content.find(query)
    if start == -1:
        return "Sorry, I couldn't find anything relevant."
    else:
        start = max(0, start - window)
        end = min(len(content), start + len(query) + 2*window)
        snippet=content[start:end]
        # remove extra tab space
        snippet=re.sub(r'\t',' ',snippet)
        # remove empty lines
        snippet=re.sub(r'\n\s*\n','\n',snippet)
        return snippet

# Example file paths and URL (replace with your actual files and URL)
# pdf_path = 'your_file.pdf'
# docx_path = 'your_file.docx'
# txt_path = 'your_file.txt'
url = 'https://knowindia.india.gov.in/profile/fundamental-rights.php#:~:text=These%20are%3A,opportunity%20in%20matters%20of%20employment'

# Load your data here and print to check
# try:
#     pdf_content = read_pdf(pdf_path)
#     print("PDF content loaded")
# except Exception as e:espon
#     print(f"Failed to load PDF: {e}")

# try:
#     docx_content = read_docx(docx_path)
#     print("DOCX content loaded")
# except Exception as e:
#     print(f"Failed to load DOCX: {e}")

# try:
#     txt_content = read_text(txt_path)
#     print("Text content loaded")
# except Exception as e:
#     print(f"Failed to load text: {e}")

try:
    web_content = fetch_web_content(url)
    print("Web content loaded")
except Exception as e:
    print(f"Failed to load web content: {e}")

content = ' '.join([web_content])
processed_content = preprocess(content)

# GUI
def send():
    user_query = entry.get()
    # print("User query:", user_query)  # Debug print
    entry.delete(0, tk.END)
    chat_log.configure(state='normal')  # Ensure the chat log is writable
    chat_log.insert(tk.END, "You: " + user_query + '\n')
    response = find_in_text(user_query, processed_content)
    # print("Response:", response)  # Debug print
    chat_log.insert(tk.END, "Bot: " + response + '\n')
    chat_log.yview(tk.END)  # Scroll to the end
    chat_log.configure(state='disabled')  # Disable editing again


root = tk.Tk()
root.title("Chatbot")

entry = tk.Entry(root)
entry.pack()
entry.bind("<Return>", lambda event: send())

send_button = tk.Button(root, text="Send", command=send)
send_button.pack()

chat_log = scrolledtext.ScrolledText(root, state='disabled')
chat_log.pack()

root.mainloop()
