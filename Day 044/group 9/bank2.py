accounts = []
current_user = None

def create_account():
    global accounts, current_user 
    fullname = input("შეიყვანეთ სახელი და გვარი: ").strip().lower()
    if not fullname:
        print("სახელი ვერ იქნება ცარიელი")
        return
    if any(acc["fullname"] == fullname for acc in accounts):
        print("ანგარიში ამ სახელით უკვე არსებობს")
        return
    pass1 = input("შეიყვანეთ პაროლი (მინიმუმ 8 სიმბოლო): ")
    pass2 = input("გაიმეორეთ პაროლი: ")
    if len(pass1) < 8:
        print("პაროლი უნდა იყოს მინიმუმ 8 სიმბოლო")
        return
    if pass1 != pass2:
        print("პაროლები არ ემთხვევა")
        return
    accounts.append({
        "fullname": fullname,
        "password": pass1,
        "balance": 0,
        "transfers": []
    })
    current_user = accounts[-1]
    print(f"ანგარიში წარმატებით შეიქმნა და შესული ხართ, {fullname}")

def login():
    global accounts, current_user
    fullname = input("შეიყვანეთ სახელი და გვარი: ").strip().lower()
    password = input("შეიყვანეთ პაროლი: ")
    for acc in accounts:
        if acc["fullname"] == fullname and acc["password"] == password:
            current_user = acc
            print(f"შეხვედით წარმატებით, {fullname}")
            return
    print("მონაცემები არასწორია")

def request_money():
    amount_str = input("შეიყვანეთ მოთხოვნილი თანხა: ")
    if not amount_str.isdigit():
        print("არასწორი თანხა")
        return
    amount = int(amount_str)
    if amount <= 0:
        print("არასწორი თანხა")
        return
    current_user["balance"] += amount
    print(f"დაირიცხა {amount}₾ ანგარიშზე")

def transfer_money():
    recipient_name = input("მიმღების სახელი და გვარი: ").strip().lower()
    recipient = None
    for acc in accounts:
        if acc["fullname"] == recipient_name:
            recipient = acc
            break
    if recipient is None:
        print("მიმღების ანგარიში ვერ მოიძებნა")
        return
    amount_str = input("შეიყვანეთ თანხა გადასარიცხად: ")
    if not amount_str.isdigit():
        print("არასწორი თანხა")
        return
    amount = int(amount_str)
    if amount <= 0 or amount > current_user["balance"]:
        print("არასაკმარისი თანხა")
        return
    confirm = input(f"ნამდვილად გსურთ {amount}₾-ის გადარიცხვა {recipient_name}-ზე? (yes/no): ").lower()
    if confirm != "yes":
        print("გადარიცხვა გაუქმდა")
        return
    current_user["balance"] -= amount
    recipient["balance"] += amount
    print(f"გადარიცხვა შესრულდა. {amount}₾ გადაირიცხა {recipient_name}-ზე")
    current_user["transfers"].append(f"{amount}₾ - გადარიცხვა {recipient_name}-ზე")

def mobile_transfer():
    while True:
        print("")
        print("|მობილურზე ჩარიცხვა|")
        print("1) ჩარიცხვა")
        print("2) უკან დაბრუნება")
        choice = input("აირჩიეთ: ")
        if choice == "2":
            print("დაბრუნდით მთავარ მენიუში")
            break
        elif choice == "1":
            while True:
                amount_str = input("შეიყვანეთ ჩასარიცხი თანხა მობილურზე: ")
                if not amount_str.isdigit():
                    print("არასწორი თანხა")
                    continue
                amount = int(amount_str)
                if amount <= 0:
                    print("თანხა უნდა იყოს მეტი ნულზე")
                    continue
                if amount > current_user["balance"]:
                    print("არასაკმარისი თანხა ანგარიშზე")
                    continue
                confirm = input(f"ნამდვილად გსურთ {amount}₾-ის ჩარიცხვა? (yes/no): ").lower()
                if confirm == "yes":
                    current_user["balance"] -= amount
                    print(f"მობილური ბალანსი შეივსო {amount}₾-ით")
                    current_user["transfers"].append(f"{amount}₾ - მობილურის ჩარიცხვა")
                    break
                else:
                    print("ჩარიცხვა გაუქმდა")
                    break
        else:
            print("არასწორი არჩევანი")

def view_transfers():
    print("")
    print("|ჩატარებული ტრანზაქციები|")
    if not current_user["transfers"]:
        print("ტრანზაქციები არ მოიძებნა")
    else:
        for transaction in current_user["transfers"]:
            print(transaction)

def main_menu():
    while True:
        print("")
        print("|მთავარი მენიუ|")
        print(f"გამარჯობა, {current_user['fullname']}!")
        print(f"ბალანსი: {current_user['balance']}₾")
        print("1) ფულის მოთხოვნა")
        print("2) გადარიცხვა")
        print("3) მობილურზე ჩარიცხვა")
        print("4) ტრანზაქციების ნახვა")
        print("5) გამოსვლა")
        print("")
        choice = input("აირჩიეთ ოპერაცია: ")
        if choice == "1":
            request_money()
        elif choice == "2":
            transfer_money()
        elif choice == "3":
            mobile_transfer()
        elif choice == "4":
            view_transfers()
        elif choice == "5":
            confirm = input("ნამდვილად გსურთ გამოსვლა? (yes/no): ").lower()
            if confirm == "yes":
                print("გამოსვლა შესრულდა")
                break
        else:
            print("არასწორი არჩევანი")

while True:
    print("")
    print("|აირჩიეთ|")
    print("1) შესვლა")
    print("2) ანგარიშის შექმნა")
    print("3) გასვლა")
    print("")
    menu = input("შეიყვანეთ არჩევანი: ")
    if menu == "1":
        login()
        if current_user:
            main_menu()
            current_user = None
    elif menu == "2":
        create_account()
        if current_user:
            main_menu()
            current_user = None
    elif menu == "3":
        print("ნახვამდის")
        break
    else:
        print("არასწორი არჩევანი")


