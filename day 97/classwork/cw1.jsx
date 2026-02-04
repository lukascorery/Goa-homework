//1) შექმენით კალკულატორის კომპონენტი რომელიც გამოიტანს ფორმას 2 შესატანი ველით, ღილაკით და პარაგრაფით. ღილაკზე დაჭერისას (მოხდება ფორმის დადასტურება onSubmit-ზე handler ფუნქციის გამოძახება) უნდა შეიკრიბოს შესტან ველებში მყოფი რიცხვები და განახლდეს ჯამის მდგომარეობაში შენახული ამჟამინდელი მნიშვნელობა (რომელიც თავიდან ნულია) პარაგრაფში უნდა გამოვიდეს ჯამის მდგომარეობა Sum: ტექსთან ერთად

import React, { useState } from "react";

function Calculator() {
  const [num1, setNum1] = useState("");
  const [num2, setNum2] = useState("");
  const [result, setResult] = useState(null);

  function addNumbers() {
    setResult(Number(num1) + Number(num2));
  }

  return (
    <div>
      <h2>Calculator</h2>

      <input type="number" value={num1} onChange={(e) => setNum1(e.target.value)}/>

      <input type="number" value={num2} onChange={(e) => setNum2(e.target.value)}/>

      <button onClick={addNumbers}>Add</button>

      <p>Result: {result}</p>
    </div>
  );
}

export default Calculator;
