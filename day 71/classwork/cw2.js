// 2) for ციკლის მეშვეობით გადაუარეთ რიცხვებს 1-იდან 10-მდე, თითოეული რიცხვისთვის ობიექტის კონსტრუქტორით (აიღეთ კონსტრუქტორი for ციკლის გაშვებამდე) შექმენით ობიექტი რომელსაც ექნება 2 კუთვნილება რიცხვი და even (ან ლუწია თუ კენტი) თუ რიცხვი ლუწი იქნება მაშინ even კუთვნილების მნიშვნელობა უნდა იყოს true ხოლო სხვა შემთხვევაში false, ეს ყველა ობიექტი უნდა დაამატოთ nubmers მასივში


function Numbers(number, even) {
    this.number = number;
    this.even = even;

}

let numebrs = [];

for (let i = 0; i < 10; i++) {
    let even = i % 2 === 0;
    const newObject = new Numbers(i, even)
    numbers.push(newObject);

}
