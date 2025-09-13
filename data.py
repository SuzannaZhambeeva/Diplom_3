import random

def get_user_data():
    email = f"testuser_{random.randint(1, 10000)}@example.com"
    password = "TestPass123"
    return email, password


def get_existing_user():
    email = "TestUser07@mail.ru"
    password = "qwerty123"
    return email, password
