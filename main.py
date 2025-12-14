from Utils import check_password_strength, suggest_password, check_pwned_password

password = input("Enter your password: ")
strength = check_password_strength(password)
leak_count = check_pwned_password(password)

if leak_count > 0:
    print(f"⚠️ This password has been leaked {leak_count} times! Consider changing it.")
else:
    print("✅ Good news! This password was NOT found in known data breaches.")


if strength <= 2:
    print("Weak password")
    print("Suggestion: Try using a longer password with uppercase, lowercase, digits, and symbols.")
elif strength <= 4:
    print("Medium strength password")
    print(f"Suggestion: Consider using a password like: {suggest_password()}")
else:
    print("Strong password")
