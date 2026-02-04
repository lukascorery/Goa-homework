// 4) შექმენით to do list გვერდი, რომელზეც გექნებათ შესატანი ველი და ღილაკი, ასევე სია რომელშიც გამოიტანთ იმ ელემენტებს რომლებსაც მომხმარებლი ჩაწერს შესატან ველში, ელეემნტი უნდა დაემატოს მხოლოდ მაშინ როდესაც მომხამრებელი დასმატებელ ელემენტს ღილაკზე დაკლიკებით დაადასტურებს

const addBtn = document.querySelector("button")
const taskInput = document.getElementById("task")
const tasks = document.querySelector("ul")

addBtn.onclick = function () {

    let newTask = document.createElement("li")
    let completed = document.createElement("input")

    completed.type = "checkbox"
    newTask.textContent = taskInput.value;

    taskInput.value = 0;

    tasks.appendChild(completed)
    
    newTask.onclick = function () {
        newTask.remove()
        
    }

    tasks.appendChild(newTask)

}
