import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = []
    for _ in range(length):
        password.append(random.choice(characters))
    password = ''.join(password)
    return password

# Example usage
password_length = int(input('enter the number of characters should be: '))
random_password = generate_password(password_length)
print("generated password: " + random_password)
