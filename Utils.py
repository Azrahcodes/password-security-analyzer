# utils.py
import hashlib
import requests
import random
import string

def check_password_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(not char.isalnum() for char in password):
        score += 1
    return score

def suggest_password():
    length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def check_pwned_password(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tail = sha1password[:5], sha1password[5:]
    url = f"https://api.pwnedpasswords.com/range/{first5}"
    response = requests.get(url)
    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == tail:
            return int(count)
    return 0
