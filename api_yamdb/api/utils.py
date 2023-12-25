import random

from .models import User

SALT = "salted_2024"


def generate_confirmation_code(user: User) -> str:
    username = user.username
    str_time = user.created_at.ctime()
    seed = f"{username}_{str_time}_{SALT}"
    random.seed(seed)
    rand = random.randint(100000, 999999)
    return str(rand)


def check_confirmation_code(code: str, data: User) -> bool:
    return generate_confirmation_code(data) == code
