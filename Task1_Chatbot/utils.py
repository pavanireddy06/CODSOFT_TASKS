"""
utils.py
---------
Utility functions for the Rule-Based Chatbot
"""

from datetime import datetime
import os


# ----------------------------
# Date
# ----------------------------

def get_date():
    """Returns current date."""
    return datetime.now().strftime("%d-%m-%Y")


# ----------------------------
# Time
# ----------------------------

def get_time():
    """Returns current time."""
    return datetime.now().strftime("%I:%M:%S %p")


# ----------------------------
# Greeting According to Time
# ----------------------------

def time_greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "🌞 Good Morning"

    elif hour < 17:
        return "☀️ Good Afternoon"

    elif hour < 21:
        return "🌇 Good Evening"

    else:
        return "🌙 Good Night"


# ----------------------------
# Help Menu
# ----------------------------

def help_menu():

    return """
====================================================

🤖 AVAILABLE COMMANDS

👋 hello
👋 hi
👋 hey

📅 date

🕒 time

💻 python

☕

java

🤖 ai

📚 machine learning

🧠 deep learning

🌐 html

🎨 css

⚡ javascript

⚛ react

🗄 sql

🐙 git

📂 github

😂 joke

💡 motivate me

🎲 fact

🧮 calculate 20+30

📊 stats

📜 history

❓ help

🚪 exit

====================================================
"""


# ----------------------------
# Save Chat History
# ----------------------------

def save_history(user, bot):

    with open("chat_history.txt", "a", encoding="utf-8") as file:

        file.write(f"You : {user}\n")
        file.write(f"Bot : {bot}\n")
        file.write("-" * 50 + "\n")


# ----------------------------
# View Chat History
# ----------------------------

def view_history():

    if not os.path.exists("chat_history.txt"):
        return "No conversation history found."

    with open("chat_history.txt", "r", encoding="utf-8") as file:
        history = file.read()

    if history.strip() == "":
        return "History is empty."

    return history


# ----------------------------
# Conversation Statistics
# ----------------------------

stats = {
    "questions": 0,
    "jokes": 0,
    "facts": 0,
    "quotes": 0,
    "calculations": 0
}


def increment(command):

    if command in stats:
        stats[command] += 1


def get_stats():

    return f"""
========================

Conversation Statistics

Questions Asked : {stats['questions']}

Jokes Requested : {stats['jokes']}

Facts Viewed : {stats['facts']}

Motivation Quotes : {stats['quotes']}

Calculations : {stats['calculations']}

========================
"""