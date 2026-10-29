correct_password = "python123"
attempt = 1
password = input("Enter password: ")
while password != correct_password and attempt < 3:
    print("Incerrect password. Try again.")
    password = input("Enter password: ")
    attempt += 1
if password != correct_password:
    print("Too many attempts.")
else:
    print("Welcome!")
