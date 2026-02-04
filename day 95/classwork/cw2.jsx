import React, { useState, useEffect } from "react";

const ratingStyles = {display: 'flex'};

fetch('https://fakestoreapi.com/products/1')
            .then(res=>res.json())
            .then(json=>console.log(json))
function product ({product}) {
    return (
        <>
            <div>
                <h3>{product.title}</h3>
                <p>${product.price}</p>
                <p>description: {product.decription}</p>
                <p>category: {product.category}</p>
                <div style={ratingStyles}>
                    <p>rate: {product.rating.rate}</p>
                    <p>count: {product.rating.count}</p>  
                </div>
            </div>
        </>
    )
}

function app() {
    const [info, setInfo] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const response = await fetch('https://fakestoreapi.com/products');
            const data = await response.json();
            setInfo(data);
        };
        fetchData();
    }, [])
}

return (
    <>
    <div>
        {info.map((item, index) => {
            return (
            <>
            <product product={item} />
            <hr/>
            </> );
        })}
    </div>
</>
)



function app2(saying) {
    saying = input("What do you want to say? ");
    saying = saying.upper();
    while (saying !== "STOP");
        return "wrong answer";
    
}   