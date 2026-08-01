import random

# ----------------------------
# Greetings
# ----------------------------

greetings = [
    "Hello! 👋 Nice to meet you.",
    "Hi there! 😊",
    "Hey! Welcome.",
    "Hello! How can I help you today?",
    "Greetings! Hope you're having a great day!"
]

# ----------------------------
# Jokes
# ----------------------------

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did Python go to therapy? Too many exceptions.",
    "Why do Java developers wear glasses? Because they don't C#.",
    "Debugging: Being the detective in a crime movie where you're also the criminal.",
    "A SQL query walks into a bar and asks two tables, 'Can I JOIN you?'",
    "Why did the developer go broke? Because he used up all his cache.",
    "There are only 10 kinds of people in the world: those who understand binary and those who don't.",
    "What's a programmer's favorite place? The Foo Bar.",
    "Why was the computer cold? It forgot to close Windows.",
    "Real programmers count from 0."
]

# ----------------------------
# Motivation
# ----------------------------

quotes = [
    "Success doesn't come from what you do occasionally. It comes from what you do consistently.",
    "Dream big. Start small. Act now.",
    "Every expert was once a beginner.",
    "The future depends on what you do today.",
    "Never stop learning because life never stops teaching.",
    "Consistency beats motivation.",
    "Small progress is still progress.",
    "Believe in yourself.",
    "Work hard in silence. Let success make the noise.",
    "Your only limit is your mindset."
]

# ----------------------------
# Interesting Facts
# ----------------------------

facts = [
    "Python was created by Guido van Rossum in 1991.",
    "Artificial Intelligence is a branch of Computer Science.",
    "The first computer bug was an actual moth.",
    "Git was created by Linus Torvalds.",
    "Python is one of the most popular programming languages in the world.",
    "Machine Learning is a subset of Artificial Intelligence.",
    "Deep Learning uses neural networks with multiple hidden layers.",
    "SQL stands for Structured Query Language.",
    "GitHub hosts millions of repositories.",
    "Linux powers most of the world's servers."
]

# ----------------------------
# Knowledge Base
# ----------------------------

responses = {

    "python":
    "Python is a high-level, interpreted programming language widely used in AI, Data Science, Web Development, and Automation.",

    "java":
    "Java is an object-oriented programming language known for portability using the JVM.",

    "ai":
    "Artificial Intelligence enables machines to simulate human intelligence such as learning, reasoning, and decision-making.",

    "machine learning":
    "Machine Learning is a subset of AI where systems learn patterns from data without being explicitly programmed.",

    "deep learning":
    "Deep Learning is a subset of Machine Learning based on artificial neural networks.",

    "data science":
    "Data Science combines statistics, programming, and machine learning to analyze data.",

    "github":
    "GitHub is a cloud platform used for hosting Git repositories and collaborating on software projects.",

    "git":
    "Git is a distributed version control system created by Linus Torvalds.",

    "sql":
    "SQL is used to create, manage, and query relational databases.",

    "html":
    "HTML is the standard markup language used for creating web pages.",

    "css":
    "CSS is used to style HTML webpages.",

    "javascript":
    "JavaScript makes websites interactive.",

    "react":
    "React is a JavaScript library for building user interfaces.",

    "how are you":
    "I'm doing great! Thanks for asking. 😊",

    "your name":
    "I'm CodSoft AI ChatBot Version 2.0.",

    "bye":
    "Goodbye! Have a wonderful day! 👋"
}

# ----------------------------
# Random Response Functions
# ----------------------------

def random_greeting():
    return random.choice(greetings)


def random_joke():
    return random.choice(jokes)


def random_quote():
    return random.choice(quotes)


def random_fact():
    return random.choice(facts)