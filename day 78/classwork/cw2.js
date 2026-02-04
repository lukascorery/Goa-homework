// 2) შექმენით textarea მესიჯის შემოტანის ველი, დაამატეთ მასზე keydown მოვლენის მსმენელი და როდესაც მომხმარებელი რაიმე სიბოლოს შეიტანს ამ ველში მაშინვე დაუთვალეთ ახალი სიმბოლოების რაოდენობა და უჩვენეთ რამდენი აქვს 200-იანი სიმბოლოების ლიმიტიდან გამოყენებული, თუ ლიმიტს გადასცდება პარაგრაფი უნდა გაწთილდეს, სხვა შემთხვევაში უნდა იყოს მწვანე

let textarea = document.getElementById("message");
let counter = document.getElementById("counter");

textarea.addEventListener("keydown", function() {

    let symbolCount = textarea.value.length;

    counter.textContent =  `${symbolCount}/200`;

    if (symbolCount > 200) {
        counter.style.color = "red";
    } else {
        counter.style.color = "green";
    }
});
