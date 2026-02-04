# 1) შექმენით ბანკომატის სიმულაცია შემდეგი ფუნქციონალით:

# •    საწყისი ბალანსი: 1000 ლარი
# •    მთავარი მენიუ (while ციკლით):
# ბალანსის შემოწმება
# თანხის შეტანა
# თანხის გატანა
# ბოლო 5 ტრანზაქციის ნახვა
# გასვლა
# •    ყოველ ოპერაციაზე:
# იყენებს try-except ბლოკს:
# ValueError - არასწორი რიცხვის შეტანა
# არასწორი მენიუს არჩევანი
# თანხის გატანისას ამოწმებს საკმარისი ბალანსის არსებობას
# შეტანისას და გატანისას ამოწმებს დადებითი რიცხვის შეყვანას
# •    ინახავს ტრანზაქციების ისტორიას სიაში: [{'type': 'შეტანა/გატანა', 'amount': თანხა, 'balance': ახალი_ბალანსი}, ...]
# •    აჩვენებს ბოლო 5 ტრანზაქციას ფორმატირებული სახით
# •    გასვლისას აჩვენებს საბოლოო ბალანსს და ტრანზაქციების რაოდენობას


balance = 1000
transactions = []

# def show_menu():
#     print("მთავარი მენიუ:")
#     print("1. ბალანსის შემოწმება")
#     print("2. თანხის შეტანა")
#     print("3. თანხის გატანა")
#     print("4. ბოლო 5 ტრანზაქციის ნახვა")
#     print("5. გასვლა")

# while True:
#     show_menu()
#     choice = input("აირჩიეთ ოპერაცია (1-5): ")

#     if choice == '1':
#         print(f"თქვენი მიმდინარე ბალანსია: {balance} ლარი")

#     elif choice == '2':
#         choice2






    

def choice2 ():
    amount = int(input("შეიყვანეთ თანხა: "))
    if amount <= 0:
        raise ValueError("გთხოვთ, შეიყვანოთ დადებითი რიცხვი.")
    balance += amount
    transactions.append({'type': 'შეტანა', 'amount': amount, 'balance': balance})
    print(f"{amount} ლარი წარმატებით დაემატა თქვენს ბალანსს.")
    return


def tchoice ():
    amount = int(input("შეიყვანეთ გასატანი თანხა: "))
    if amount <= 0:
        raise ValueError("გთხოვთ, შეიყვანოთ დადებითი რიცხვი.")
    if amount > balance:
                print("მონაცემი არ არის საკმარისი ბალანსი.")
    else:
        balance -= amount
        transactions.append({'type': 'გატანა', 'amount': amount, 'balance': balance})
        print(f"{amount} ლარი წარმატებით გაიტანეთ თქვენს ბალანსიდან.")

def fchoice():
    amount = int(input("შეიყვანეთ გატანილი თანხა: "))
    if amount <= 0:
         raise ValueError("გთხოვთ, შეიყვანოთ დადებითი რიცხვი.")
    if amount > balance:
        print("მონაცემი არ არის საკმარისი ბალანსი.")
    else:
        balance -= amount
        transactions.append({'type': 'გატანა', 'amount': amount, 'balance': balance})
        print(f"{amount} ლარი წარმატებით გაიტანეთ თქვენს ბალანსიდან.")

def fichoice():
    print("ბოლო 5 ტრანზაქცია:")
    for transaction in transactions[-5:]:
        print(f"{transaction['type']}: {transaction['amount']} ლარი, ახალი ბალანსი: {transaction['balance']} ლარი")
    
def lastchoice ():
    print(f"გასვლა... საბოლოო ბალანსი: {balance} ლარი")
    print(f"სულ ტრანზაქციების რაოდენობა: {len(transactions)}")
    try:
        raise ValueError("არასწორი მენიუს არჩევანი. გთხოვთ, აირჩიოთ 1-დან 5-მდე.")
    except ValueError as ERROR:
        print(f"შეცდომა: {ERROR}")