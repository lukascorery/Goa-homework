// 1) შექმენით account ობიექტი რომელშიც კუთვნილების სახელები იქნება გამოსახულებები, კუთვნიელბის სახელები იყოს რაიმე ცვლადები და ზოგ შემთხვევაში string-ების კონკატინაცია, შექმენით deposit რომელიც ობიექტის this.balance კუთვნილებას გაზრდით amount პარამეტრით, ეს მეთოდი 2-ჯერ გამოიძახეთ, შემდეგ შექემნით person ობიექტი რაიმე სხვა კუთვნილებებითა და balance-ით, შემდეგ ამ ორი 2 ობიექტის Object.assign() მეთოდით გაერთიანებით შექმენით personAccount ობიექტი სამივე ობიექტი გამოიტანეთ კონსოლში. შემდეგ dataArr მასივი 3 ელემენტი და მოახდინეთ მისი დესქტრურირება სამივე ელემენტი შეინახეთ 3 სხვასხვა ცვლადშ და გამოიტანეთ კონსოლში, კომენტარებით ახსენით ყველაფერი


let something = "luka"
let surname = "shavadze"
let fullname = `${something} ${surname}`

const account = {
    firstname: [something],
    lastName: "shavadze",
    balance: 1000,
}

const deposit = {
    [fullname]: something,
    lastName: "shavadze",
    balance: 200,


    deposit() {
        this.balance += 500;
    }
}   
deposit.deposit();
newBalance = Object.assign(account, deposit);

console.log(newBalance);