import { useState } from "react";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <input
        type="number"
        value={count}
        onChange={(change) => setCount(Number(change.target.value))}
      />

      <button onClick={() => setCount(count + 1)}>Add</button>
      <button onClick={() => setCount(count - 1)}>Subtract</button>

      <p>Result: {count}</p>
    </div>
  );
}

export default App;
