correct_username = "admin"
correct_password = "python123"

username = input("Enter a username: ")
password = input("Enter a password: ")

if username == correct_username and password == correct_password:
    print("Access granted")
else:
    print("Access denied")
