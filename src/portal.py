#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 22:14:44 2026

@author: op
"""


import cgi
import json
import os

# 1. Map out paths to your files in the htdocs folder
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, 'users.json')
TEMPLATE_FILE = os.path.join(SCRIPT_DIR, 'dashboard.html')

# 2. Print the required web headers so Abyss knows HTML text is coming
print("Content-Type: text/html\r\n\r\n")

form = cgi.FieldStorage()
# Clean up extra spaces so blank inputs are properly rejected
username = form.getvalue('username', '').strip()
password = form.getvalue('password', '').strip()
action = form.getvalue('action') 

def load_users():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_users(users_data):
    with open(DB_FILE, 'w') as f:
        json.dump(users_data, f, indent=4)

# 3. Form validation check
if not username or not password:
    print("<body style='font-family:Arial; text-align:center; padding-top:50px;'>")
    print("<h3>Error: Username or password cannot be blank.</h3><a href='index.html'>← Back</a>")
    print("</body>")
    exit()

users = load_users()

# 4. Handle Registration Mode
if action == "register":
    if username in users:
        print(f"<h3>Error: Username '{username}' already exists!</h3><a href='index.html'>← Back</a>")
    else:
        users[username] = password  
        save_users(users)
        print(f"<h3>Registration Successful! You can now log in, {username}.</h3><a href='index.html'>← Go to Login</a>")

# 5. Handle Login Mode (Template Engine Logic)
elif action == "login":
    if username in users and users[username] == password:
        
        # Check if your separate dashboard layout file exists on your Mac
        if os.path.exists(TEMPLATE_FILE):
            # A. Open the layout file in read-only mode ('r')
            with open(TEMPLATE_FILE, 'r') as f:
                template_content = f.read()  # Read raw layout string into RAM
            
            # B. Modify the text on-the-fly: replace placeholder with real student name
            final_html = template_content.replace("{{STUDENT_NAME}}", username)
            
            # C. Spit the completed HTML data stream out into Abyss's hands
            print(final_html)
        else:
            print("<h3>Error: Dashboard template file (dashboard.html) is missing on the server.</h3>")
            
    else:
        print("<h3>Error: Invalid username or password.</h3><a href='index.html'>← Back</a>")

