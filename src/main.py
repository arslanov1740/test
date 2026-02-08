import os
from dotenv import load_dotenv

def print_author():
    load_dotenv()
    author = os.getenv("AUTHOR")
    print(f"Автор проекта: {author}")

print_author()
