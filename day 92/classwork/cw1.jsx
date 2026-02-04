import {useState} from "react";

function App () {
    const [state, setState] = useState({count: 0, name: "Counter"});

    function addCount () {
        setState(prev => ({...prev, count: prev.count + 1}));
    }

    function subCount () {
        setState(prev => ({...prev, count: prev.count - 1}));
    }

    return (
        <div>
            <button onClick={addCount}>Add</button>
            <button onClick={subCount}>Subtract</button>
            <p>{state.name}: {state.count}</p>
        </div>
    )
}

export default App;