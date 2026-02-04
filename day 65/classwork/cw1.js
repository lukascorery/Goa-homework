// 1)  შექმენით 3 ობიექტი: მებრძოლის, პროდუქტის და პიროვნების. თითეულში უნდა იყოს მინიუმუმ 3 კუთვნილება და 1 მეთოდი, კომენტარებით დაწერეთ რა არის ობიექტი, როგორ იქმება და რაში ვიყენებთ. ასევე ახსენით თქვენი სიტყვებით docment-ის ობიექტი

const Fighter = {
    name: "Samurai",
    Health: 150,
    Damage: 100,
    Speed: 30,
    opponetHealth: 100, 
    attack: function (opponet) {
        console.log(`Dealt damage to ${opponet}`)
        console.log(`opponent current health ${opponet.Health}`)
        
    }
}

console.log(Fighter.Health)
console.log(Fighter.Damage)
console.log(Fighter.Speed)
console.log(Fighter.name)

