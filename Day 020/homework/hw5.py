"""5) მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები"""

pin = "1234"
attempts = 3
while attempts > 0:
    user_input = input("Enter your PIN: ")
    if user_input == pin:
        print("Access Granted")
        break
    else:
        attempts -= 1
        print(f"Incorrect PIN. You have {attempts} attempts left.")
    if attempts == 0:
        print("Access Denied")
        break