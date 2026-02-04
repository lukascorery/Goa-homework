// 


class Account {
    constructor(fname, lName, email, password, balance) {
        this.fname = fistName;
        this.lName = lastName;
        this.email = email;
        this.password = password;
        this.balance = balance;
        Account.accounts += 1
    }
    static accounts = 0;
    deposit(amount) {
        this.balance += amount;
    }
    get password() {
        return "********";
    }
}
    
    

firstAcc = new Account("luka", "shavadze", "luka.shavadze@example.com", "password123", 1000);
secondAcc = new Account("ana", "beridze", "ana.beridze@example.com", "password456", 2000);
console.log(firstAcc);