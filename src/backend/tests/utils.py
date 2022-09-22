def weak_password_generator(username: str) -> str:
    return hex(hash(username))
