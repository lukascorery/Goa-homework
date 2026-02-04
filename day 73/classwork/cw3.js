// 3) შექმენით ნებისმიერ ფუნქცია, რომელსაც გამოიძახებთ ყოველ 3 წამში ერთხელ, შემდეგ ეს ისტრუქცია დააკომენტარეთ და ფუნქცია გამოძახეთ ერთხელ ინსტრუქციის წაკითხვიდან 4 წამის შემდეგ, კომენტარებით ახსენით როგორ მუშაობს setInterval და setTimeout ფუნქციები

let myFunction = function() {
    console.log("Hello, world!");
}
setInterval(myFunction, 3000); 

setTimeout(myFunction, 4000); 