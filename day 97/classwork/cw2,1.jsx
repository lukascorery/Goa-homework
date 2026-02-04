import React from "react";

function CalculatorUI({
  num1,
  num2,
  result,
  onNum1Change,
  onNum2Change,
  onAdd,
}) {
  return (
    <div>
      <h2>Calculator</h2>

      <input
        type="number"
        value={num1}
        onChange={(e) => onNum1Change(e.target.value)}
      />

      <input
        type="number"
        value={num2}
        onChange={(e) => onNum2Change(e.target.value)}
      />

      <button onClick={onAdd}>Add</button>

      <p>Result: {result}</p>
    </div>
  );
}

export default CalculatorUI;
