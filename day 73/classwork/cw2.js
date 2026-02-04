// 2) შექმენით თარიღის ობიექტი, რომელშიც შეინახავთ 2023 წლის სექტემბერის 5 რიცხვს. ამისთვის გადაეცით date ობიექტის სტირნგის სახით თარიღი, კომენტარებით დაწერთ კიდევ როგორ შეიძლება date ობიექტს გადავცეთ თარიღი და თუ არ გადავცემთ არგუმენტს რა მოხდება. შექმნილი date ობიექტი შეინახეთ hireDate ცვლადში და ცალცალკე კონსოლში გამოიტანეთ წელი, თვე, რიცხვი, კვირის დღე, საათები, წუთები და წამები

const hireDate = new Date("2023-09-05");
console.log(hireDate.getFullYear());
console.log(hireDate.getMonth() );
console.log(hireDate.getDate());
console.log(hireDate.getDay());
console.log(hireDate.getHours());
console.log(hireDate.getMinutes());
console.log(hireDate.getSeconds());

// სხვა ვარიანტები date ობიექტის შექმნისთვის:
const hireDate1 = new Date(2023, 8, 5); 

//თუ არ მივცემთ არგუმენტს, მაშინ date ობიექტი შექმნება მიმდინარე თარიღისა და დროის მიხედვით
