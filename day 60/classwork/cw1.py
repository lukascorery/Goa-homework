"""1) შექმენით account კლასი რომელშიც გექნებათ ერთი protected და private ატრიბუტები და მეთდები. დაამატეთ ერთი კლასის მეთოდი რომელიც დაითვლის ამ კლასის მატარებლი ობიექტების რაოდენობას. კომენტარებით დაწერეთ protected და private ატრიბუტების განმარტება და ასევე კლასს და სტატიკიური მეთოდების დანიშნულება"""



class Account:
    __count = 0  

    def __init__(self, username, email, password, balance):
        self.username = username     # public ატრიბუტი – ყველგან ხელმისაწვდომია
        self._email = email          # protected ატრიბუტი – შეთანხმებით, მხოლოდ კლასსა და შვილობილი კლასებში უნდა გამოვიყენოთ
        self.__password = password   # private ატრიბუტი – იმალება გარედან
        self.balance = balance

        Account.__count += 1

   
    def _get_email(self):
        return self._email

    def __get_password(self):
        return self.__password

    
    @classmethod
    def get_count(cls):
        return cls.__count

    
    @staticmethod
    def info():
        return "Account კლასი გამოიყენება მომხმარებლის ანგარიშების შესაქმნელად"


