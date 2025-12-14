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


password = input("Enter your password: ")
strength = check_password_strength(password)

if strength <= 2:
    print("Weak password")
elif strength <= 4:
    print("Medium strength password")
else:
    print("Strong password")
