// https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/javascript

function sumDigPow(a, b) {
  let result = [];

  for (let num = a; num <= b; num++) {
    let str = String(num);
    let sum = 0;

    for (let i = 0; i < str.length; i++) {
      let digit = Number(str[i]);
      sum += digit ** (i + 1); 
    }

    if (sum === num) result.push(num);
  }

  return result;
}
 