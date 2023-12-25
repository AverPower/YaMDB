import random
from datetime import datetime

SALT = "salted"


def generate_confirmation_code(username: str) -> str:
    str_time = datetime.now().strftime("%D")
    seed = f"{username}_{str_time}_{SALT}"
    random.seed(seed)
    rand = random.randint(100000, 999999)
    return str(rand)


def check_confirmation_code(code: str, username: str) -> bool:
    return generate_confirmation_code(username) == code
