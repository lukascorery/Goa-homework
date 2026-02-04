// 1) წინაზე შესრულბულ useEffect-ის დავალება შეცვალეთ და .then (promsie-მეთოდის) ნაცვლად გამოიყენეთ async/await სინტაქსი (ასინქონიაზცია) მაგრამ გაითვალისწინეთ ის რომ არ შეიძლება useEffect-ზე გადაცემული callback ფუნქცია არ შეიძლება იყოს ასქრიონული, ამიტომ გადაეცით სინქრონული ფუნქცია რომელიც ასინქრონულ ფუქნციას გამოიძახებს ან პირდაპირ შექმენით ასქრიონული ფუნქცია useEffect-ში არსებულ arrow ფუქნციაში და მერე იქვე გამოიძახეთ


import { useState, useEffect } from "react";

function App () {
        const [dataType, setDataType] = useState("users");
        const [data, setData] = useState([]);
        useEffect(() => {
            async function fetchData() {
                const response = await fetch(`placeholder`);
                const json = await response.json();
                setData(json);
            }
            fetchData();
        }, [dataType]);

    return ( 
    <>
    <button onClick={() => setDataType("users")}>Users</button>
    <button onClick={() => setDataType("posts")}>Posts</button>
    <button onClick={() => setDataType("comments")}>Comments</button>
    <h2>{dataType}</h2>
    <ul>
        {data.map((item, index) => 
            <li key={index}>{JSON.stringify(item)}</li>
        )}
    </ul>
    </>
    )
}

export default App;


