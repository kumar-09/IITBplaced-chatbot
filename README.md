<p align="center">
  <img src="assets/logo.png" alt="Placement Chatbot Logo" width="200"/>
</p>

<h1 align="center">Placed</h1>
<p align="center">
  An intelligent, desktop-based chatbot to query and explore scraped placement data.
</p>

---

## 📖 Overview
Placement Chatbot is a Python-powered desktop application that allows students to query placement/job data in a natural language format.  
It uses **semantic search** over pre-scraped data to quickly find relevant jobs, programs, and departments.

---

## 🚀 Features
- **Interactive Chat Interface** (built with PyQt5)
- **Semantic Search** using embeddings
- **Data Cleaning** (HTML stripped from descriptions)
- **Scalable Architecture** for future expansion
- **Local Vector Database** for lightning-fast search
- **Extensible Design** — easily integrate other APIs or datasets

---

## 📂 Project Structure
IITBplaced_chatbot/
├── assets/ # Images, logos
├── data/ # Raw & processed JSON data
├── chatbot/ # Core chatbot logic & UI
├── main.py # App entry point
├── config.py # Configurations
├── requirements.txt # Dependencies
└── README.md # Documentation