// 3) შექმენით რიცხვების მასივსი და გამოიყენეთ მომცეული მეთოდებიდან ყველა თან ახსენით როგორ მუშაობენ

// pop
// shift
// -unshift
// slice
// splice
// indefOf
// lastIndexOf
// includes
// find
// findIndex

let numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];


let lastElement = numbers.pop();

let firstElement = numbers.shift();

let newLength = numbers.unshift(0);

let slicedArray = numbers.slice(1, 4);

let splicedElements = numbers.splice(2, 2, 99, 100);

let index = numbers.indexOf(99);

let lastIndex = numbers.lastIndexOf(100);

let hasElement = numbers.includes(50);


let foundElement = numbers.find(num => num > 50);

let foundIndex = numbers.findIndex(num => num > 50);
