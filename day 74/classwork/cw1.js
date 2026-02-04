// 1) შექმენით 3 product კლასის მქონე div ელემენტი, პირველ ელემენტს მიანიჭეთ ასევე გასნხვავბული id და ჩაწერეთ მასში 2 თქვენთვის სასურველი ელემენტი, შემდეგ გამოიყეენთ ყველა ეს document-ის მეთოდი: getElementsByTagName, getElementsByClassName, previousElementSibling, nextgElementSibling, firstChild, lastChild და კომენტარებით ახსენით როგორ მუშაობს თითოეული, ასევე დაწერეთ თუ რა არის DOM


// DOM (Document Object Model) არის ვებგვერდის სტრუქტურის მოდელი, რომელიც წარმოადგენს HTML დოკუმენტის ელემენტებს ობიექტების სახით, რაც საშუალებას აძლევს პროგრამებს და სკრიპტებს დოკუმენტის სტრუქტურასთან ურთიერთობას და მის მოდიფიცირებას.

const divsByTag = document.getElementsByTagName("div");
const divsByClass = document.getElementsByClassName("product");
const firstchild = document.body.firstChild;
const lastchild = document.body.lastChild;
const firstDiv = document.body.children[0];

