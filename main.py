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

password = input("Enter your password: ")
strength = check_password_strength(password)

if strength <= 2:
    print("Weak password")
    print("Suggestion: Try using a longer password with uppercase, lowercase, digits, and symbols.")
elif strength <= 4:
    print("Medium strength password")
    print(f"Suggestion: Consider using a password like: {suggest_password()}")
else:
    print("Strong password")
