const username = document.getElementById("user");
const password = document.getElementById("pass");
const submitBtn = document.getElementById("submit");

submitBtn.onclick = function () {
    console.log(username.value)
    console.log(password.value)
}



// 1) შექმენით სახელისა და პაროლის შესტანი ველი და დამადასტურებელი ღილაკი. როდესაც ღილაკზე მოხდება დაჭერა (გამოიყენეთ onclick ატრიბუტი external javascript-ში) წამოიღეთ მომხარებლის სახელი და და პაროლი, გააერთიანეთ ისინი და გამოიტანეთ კონსოლში, კომენტარებით ახსენით კოდის ყველაა ნაწილს, ასევ დაიცავით საუკეთესო პრაქტიკები