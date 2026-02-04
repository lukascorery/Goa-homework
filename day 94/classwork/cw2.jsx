// 2) აიღეთ 3 ღილაკი: Users, Posts, Comments. თითეულზე დაჭერისას შესაბამისი ტექსტით უნდა განახლდეს აქამდე შექმნილი dataType მდგომარეობის მნიშვნლობა setter ფუნქციით (onClick-ის მოვლენის დროს გამოიძახებთ arrow ფუნქციის საშვალებით) შესაბამისად: users, posts, comments. თქვენ უნდა გამოიყენოთ useEffect კაუჭი რომ მონაცემების წამოღება api-დან მოხდეს მხოლოდ dataType მდგომარეობის შეცვლისას, მონაცემები პრიდაპირ დაარენდერეთ
import {userState, useEffect, use} from "react";

function App () {
        const {dataType, setDataType} = userState("users");

        useEffect(() => {
        fetch(`https://jsonplaceholder.typicode.com`)
        .then(response => response.json())
        .then(json => setData(json))
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