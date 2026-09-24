import hashlib


def hash_password(password):
    if isinstance(password, str):
        password = password.encode('utf-8')
    return hashlib.sha256(password).hexdigest()


def log(msg):
    print(f"[LOG] {msg}")
