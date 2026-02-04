// https://www.codewars.com/kata/5938f5b606c3033f4700015a/train/javascript

function alphabetWar(fight) {

  let field = "";


  for (let i = 0; i < fight.length; i++) {
    if (fight[i] === "*") continue;
    if (fight[i - 1] === "*") continue;
    if (fight[i + 1] === "*") continue;

    field += fight[i];
  }


  const leftSide = "sbpw"; 
  const rightSide = "zdqm"; 

  let leftScore = 0;
  let rightScore = 0;

  for (let char of field) {
    if (leftSide.includes(char)) {
      leftScore += leftSide.indexOf(char) + 1;
    } else if (rightSide.includes(char)) {
      rightScore += rightSide.indexOf(char) + 1;
    }
  }


  if (leftScore > rightScore) {
    return "Left side wins!";
  } else if (rightScore > leftScore) {
    return "Right side wins!";
  } else {
    return "Let's fight again!";
  }
}