"""
=========================================
CodSoft Rule-Based AI ChatBot
Version : 2.0
Author  : Pavani S K Reddy
=========================================
"""

from colorama import Fore, Style, init
from difflib import get_close_matches

from responses import (
    responses,
    random_greeting,
    random_joke,
    random_quote,
    random_fact
)

from calculator import calculate

from utils import (
    get_date,
    get_time,
    time_greeting,
    help_menu,
    save_history,
    view_history,
    increment,
    get_stats
)

init(autoreset=True)


# ======================================
# Banner
# ======================================

print(Fore.CYAN + r"""

 ██████╗ ██████╗ ██████╗ ███████╗ ██████╗ ███████╗████████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔═══██╗██╔════╝╚══██╔══╝
██║     ██║   ██║██║  ██║███████╗██║   ██║█████╗     ██║
██║     ██║   ██║██║  ██║╚════██║██║   ██║██╔══╝     ██║
╚██████╗╚██████╔╝██████╔╝███████║╚██████╔╝██║        ██║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝        ╚═╝

""")

print(Fore.YELLOW + "=" * 65)
print(Fore.GREEN + "        🤖 Welcome to CodSoft AI ChatBot 🤖")
print(Fore.YELLOW + "=" * 65)

name = input(Fore.CYAN + "\nEnter your name : ").strip()

print(
    Fore.GREEN +
    f"\n{time_greeting()}, {name}! 😊"
)

print(Fore.MAGENTA + "\nType 'help' to see all available commands.\n")


# ======================================
# Commands
# ======================================

commands = [

    "hello",
    "hi",
    "hey",

    "time",
    "date",

    "python",
    "java",
    "ai",

    "machine learning",
    "deep learning",

    "data science",

    "git",
    "github",

    "sql",

    "html",
    "css",
    "javascript",
    "react",

    "joke",

    "motivate me",

    "fact",

    "calculate",

    "history",

    "stats",

    "help",

    "exit"

]


print(Fore.YELLOW + "-" * 65)

while True:

    user = input(Fore.CYAN + f"\n{name}: ").strip().lower()

    # Count every user input
    increment("questions")

    # ============================
    # Exit
    # ============================

    if user == "exit":

        reply = f"Goodbye {name}! 👋 Have a wonderful day."

        print(Fore.GREEN + "\nBot:", reply)

        save_history(user, reply)

        break

    # ============================
    # Greetings
    # ============================

    elif user in ["hello", "hi", "hey"]:

        reply = random_greeting()

        print(Fore.GREEN + "Bot:", reply)

        save_history(user, reply)

    # ============================
    # Time
    # ============================

    elif user == "time":

        reply = get_time()

        print(Fore.GREEN + "Bot:", reply)

        save_history(user, reply)

    # ============================
    # Date
    # ============================

    elif user == "date":

        reply = get_date()

        print(Fore.GREEN + "Bot:", reply)

        save_history(user, reply)

    # ============================
    # Joke
    # ============================

    elif user == "joke":

        increment("jokes")

        reply = random_joke()

        print(Fore.GREEN + "😂", reply)

        save_history(user, reply)

    # ============================
    # Motivation
    # ============================

    elif user == "motivate me":

        increment("quotes")

        reply = random_quote()

        print(Fore.GREEN + "💡", reply)

        save_history(user, reply)

    # ============================
    # Fact
    # ============================

    elif user == "fact":

        increment("facts")

        reply = random_fact()

        print(Fore.GREEN + "📚", reply)

        save_history(user, reply)

    # ============================
    # Calculator
    # ============================

    elif user.startswith("calculate"):

        increment("calculations")

        expression = user.replace("calculate", "").strip()

        reply = str(calculate(expression))

        print(Fore.GREEN + "🧮 Answer:", reply)

        save_history(user, reply)

    # ============================
    # Help
    # ============================

    elif user == "help":

        reply = help_menu()

        print(Fore.YELLOW + reply)

        save_history(user, "Displayed Help Menu")

    # ============================
    # History
    # ============================

    elif user == "history":

        history = view_history()

        print(Fore.MAGENTA + history)

        save_history(user, "Viewed Chat History")

    # ============================
    # Statistics
    # ============================

    elif user == "stats":

        reply = get_stats()

        print(Fore.CYAN + reply)

        save_history(user, "Viewed Statistics")

            # ============================
    # Knowledge Base
    # ============================

    elif any(key in user for key in responses):

        found = False

        for key in responses:

            if key in user:

                reply = responses[key]

                print(Fore.GREEN + "\n🤖 Bot:", reply)

                save_history(user, reply)

                found = True

                break

    # ============================
    # Typo Detection
    # ============================

    else:

        suggestion = get_close_matches(
            user,
            commands,
            n=1,
            cutoff=0.60
        )

        if suggestion:

            reply = (
                f"Did you mean '{suggestion[0]}' ?\n"
                f"Type '{suggestion[0]}' to continue."
            )

            print(Fore.YELLOW + "\n💡", reply)

            save_history(user, reply)

        else:

            reply = """
Sorry 😔

I don't understand that command.

Type 'help' to see all available commands.

You can ask me about:

• Python
• Java
• AI
• Machine Learning
• Deep Learning
• SQL
• Git
• GitHub
• HTML
• CSS
• JavaScript
• React

You can also use:

• joke
• fact
• motivate me
• calculate 10+20
• date
• time
• history
• stats
"""

            print(Fore.RED + reply)

            save_history(user, reply)