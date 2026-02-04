// 1) ვებგვერდზე მომხმარებელს prompt-ის გამოყენებით შემოტანინეთ თაივსი გამოცდისა და აქტიურობის ქულები, შემდეგ გარდაქმენით ისინი რიცხვებად Numbert ან ParseInt ფუნქციების გამოყენებით, შემდეგ შეკრიბეთ და შეამოწმეთ თუ როემლ კატეროგიაში მოხვდა ეს ქულა, რის მიხედვითაც გამოუტანთ მოსწავლეს შეფასბეას

// A 90-100
// B 80-90
// C 70-80
// D 50-70
// E 30-50
// F <30
let examScore = Number(prompt("enter your exam score: "))
let examScoreTwo = Number(prompt("idr what to ask here: "))

finalExamScore = parseInt(examScore + examScoreTwo)


if (finalExamScore > 90) {
    console.log("A")
}   else if (finalExamScore > 80){
    console.log("B ")
}   else if (finalExamScore > 70){
    console.log("C ")
}   else if (finalExamScore > 50){
    console.log("D ")
}   else if (finalExamScore > 30){
    console.log("E ")
}   else if (finalExamScore < 30){
    console.log("F ")
}






