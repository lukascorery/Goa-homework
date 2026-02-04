// 2) კალკულატორის კომპონენტი დაშალეთ 2 კომპონენტად: Container & Presentational. Container კომპონენტში დატოვეთ მხოლოდ მდგოამროებები, ფუნქციები და ა.შ ლოგიკასთან ასოცირებული ნაწილი ხოლო Presentational-ში კი უნდა მოხდეს მხოლოდ ui-ის დარენდრება, მიღებული prop-ის მიხევიდთ container კოპმონეტით

import React, { useState } from "react";
import CalculatorUI from "./cw2,1";

function CalculatorContainer() {
  const [num1, setNum1] = useState("");
  const [num2, setNum2] = useState("");
  const [result, setResult] = useState(null);

  function addNumbers() {
    setResult(Number(num1) + Number(num2));
  }

  return (
    <CalculatorUI
      num1={num1}
      num2={num2}
      result={result}
      onNum1Change={setNum1}
      onNum2Change={setNum2}
      onAdd={addNumbers}
    />
  );
}

export default CalculatorContainer;

// 3) წინა Frontend-is გაკვეთილის მესამე საკლასო დავალებას დაუმატეთ კიდევ ერთი loading მდგომარეობა რომელიც თავიდან იქნება true (ესეიგი თავიდან მართლია რომ იტივრთება საიტი) და როდეასც მოხდება საიტის ჩატვირთვა (ანუ როცა api-იდან წამოღებული მონაცემებით გაანახლებთ ცარიელ products/info მდგომარეობის მნიშვნელობას) მაშინ setLoading(false) შეცვალეთ ჩატვირთვის მდგომარეობა და გახადეთ მცადრი. თუ loading მდგომაროების მნიშვნელობა ჭეშმარიტია მაშინ მხოლოდ ერთი div დაარენდრეთ ...Loading ტექსტით. დაამატე try-except error  

 function App() {
  const [info, setInfo] = useState([]);
  const [loading, setLoading] = useState(true);


    useEffect(() => {
        const fetchData = async () => {
            const response = await fetch('https://fakestoreapi.com/products');
            const data = await response.json();
            setInfo(data);
            setLoading(false);
        }
        fetchData(); 
        try {
        } catch (error) {
            console.error("Error fetching data: ", error);
        }

    }, [])
    if (loading) {
      return <div>...Loading</div>;
    }  
    return (
    <>
    <div>   
        {info.map((item, index) => { 
            return (
            <>  
            <Product product={item} key={index} />
            <hr/>
            </> );
        })}
    </div>
</>
)
}