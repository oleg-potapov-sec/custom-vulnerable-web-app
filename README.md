# Custom Vulnerable Web Application

## Overview
While learning about web server security protocols and HTML, I was eager to reinforce my understanding on a practical level. I decided to build a simple, dynamic webpage from scratch to observe firsthand how both secure and unsecured methods affect data. The complexity of this application is designed to grow continuously alongside my understanding of new security solutions.

## Current State & Baseline Analysis
The application is currently in its foundational stage, utilizing **Python, HTML, JSON, and SQL**. It is intentionally lacking advanced security controls at this very moment, so that I can establish an unencrypted traffic baseline. I am actively using **Burp Suite** and **Wireshark** to analyze client-server communication, HTTP requests, and network packets within this local environment.

## Security Implementation Roadmap
I am treating this as a vulnerable application and am in the process of manually securing the backend architecture. Upcoming security implementations include:
- [ ] Password Hashing and Salting
- [ ] Secure Session Tokens and Management
- [ ] Symmetric and Asymmetric Encryption Integration
- [ ] Input Validation and Sanitization

## Tools & Technologies Used
* **Backend:** Python, SQL
* **Frontend:** HTML, JSON
* **Server:** Abyss Web Server Local Host
* **Security & Analysis:** Burp Suite, Wireshark, Kali Linux (VM)
* **Development Environment:** Anaconda (Spyder IDE)
