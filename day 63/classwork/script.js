// 2) შექმენით სათაური, შესატანი ველი და ღილაკი. როდესაც მოხდება ღილაკზე დაჭერა სათურის ტექსტი უნდა განახლდეს და გახდეს <Hello მომხმარებლის სახელი> გამოიყენეთ external javascript და ყველაფერი ახსენით კომენტარებით

const userInput = document.getElementById("username")

const h1 = document.getElementById("h1")
const submitBtn = document.getElementById("mysubmit")


function getUsername () {
    let username = userInput.value;
    h1.textContent = "hello " + username;

}

submitBtn.onclick = getUsername
