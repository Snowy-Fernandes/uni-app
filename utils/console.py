import os

os.system("")

CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
END = "\033[0m"


def say(text, color="", level=0):
    print("\t" * level + color + text + END)


def ask(text, color="", level=0):
    return input("\t" * level + color + text + END).strip()
