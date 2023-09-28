# lib/helpers.py

games_database = [
    {"id": 1, "title": "Game 1", "price": 19.99},
    {"id": 2, "title": "Game 2", "price": 29.99},
    {"id": 3, "title": "Game 3", "price": 39.99},
]

user_credits = 0

my_games = []

def list_my_games():
    print("My Games:")
    for game in my_games:
        print(f"ID: {game['id']}, Title: {game['title']}, Price: ${game['price']}")

def check_credits():
    print(f"Your current credits: ${user_credits}")

def exit_program():
    print("Goodbye!")
    exit()
