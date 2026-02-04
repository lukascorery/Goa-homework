// 1) შექმენით task ობიექტის კონსტრუქტორი რომელსაც ექნება 5 კუთვნილება: title, desc, state, deadline, complete (მეთოდი), შექმენით მინიმუმ 3 ობიექტი და თითოეულზე გამოიძახეთ complete მეთოდი, საბოლოოდ გამოიტანეთ ყველა, კომენტარებით ახსენით რა არის ობიექტი და ჩამოწერეთ მისი 3-ვე ტიპის თვისება

function Task(title, desc, state, deadline){
    this.title = title
    this.desc = desc
    this.state = state
    this.deadline = deadline
    this.complete =  function(){
        this.state = !this.state
    }
}

let homework = new Task("Homework", "Group 64", false, "2025-07-30")

let classwork = new Task("Classwork", "Group 64", false, "2025-07-30")

let project = new Task("Project", "Group 64", false, "2025-07-30")

homework.complete()
classwork.complete()
project.complete()

console.log(homework)
console.log(classwork)
console.log(project)

// ობიექტი არის მონაცემთა ერთეული, რომელიც შეიცავს თვისებებს და მეთოდებს. თვისებები აღწერენ ობიექტის მდგომარეობას ან მახასიათებლებს, ხოლო მეთოდები განსაზღვრავენ ობიექტის ქცევას ან მოქმედებებს. 


