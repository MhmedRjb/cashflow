from werkzeug.security import generate_password_hash

# Example code for hashing passwords
hashed_password_1 = generate_password_hash('hashed_password_1')
hashed_password_2 = generate_password_hash('hashed_password_2')

print(f'Hashed password 1: {hashed_password_1}')
print(f'Hashed password 2: {hashed_password_2}')
