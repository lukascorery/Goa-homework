// https://www.codewars.com/kata/527e4141bb2ea5ea4f00072f/train/javascript

function twistedSum(n) {
  let total = 0;

  for (let i = 1; i <= n; i++) {
    let numStr = i.toString(); 
    for (let num = 0; num < numStr.length; num++) {
      total += Number(numStr[num]);
    }
  }

  return total;
  }