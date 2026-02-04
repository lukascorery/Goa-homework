// https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/javascript

function expandedForm(num) {
  let str = String(num);
  let len = str.length;
  let parts = [];

  for (let i = 0; i < len; i++) {
    let digit = Number(str[len - 1 - i]);
    let value = digit;

    for (let main = 0; main < i; main++) {
      value = value * 10;
    }

    if (value) {
      parts.push(String(value));
    }
  }

  return parts.reverse().join(" + ");
}



