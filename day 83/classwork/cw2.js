// 2) შექმენით promise ობიექტი, რომელიც arrow ფუნქციას 2 პარამეტრით: resolve, reject. ამ ფუნქციაში შექმენით ცვლადი internetRequest = true, setTimeout-ის მეშვეობით 3 წამის შემდეგ გამოიძახეთ ფუნქცია რომელიც if-ით შეამოწმებს internetRequest-ის ცვლადს, თუ მართალია ეს ცვლადი მაშინ მოახინდეთ resolve სხვა შემთხვევაში კი reject. promise-ის დასრულებამდე ყოველ ნახევარ წამში შეამომწეთ promise-ის მდოგმარეობა


let promise = new Promise((resolve, reject) =>{
    let internetRequest = false

    setTimeout(() => {
        if (internetRequest === true) {
            resolve ("promise success")
        }else (internetRequest === false)
            reject("promise failed")
    })

    let interval = setInterval(() => {
        console.log("promise is pending...")
    }, 500);

    setTimeout(() => {
        clearInterval (interval)
    }, 3000);

})


//promise არის ობიექტი რომელიც ოპერაციებს ახორციელებს და გვაძლევს საშუალებას გავაკონტროლოთ მათი შესრულების შედეგი (წარმატება ან წარუმატებლობა).