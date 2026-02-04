//1) შექმენით შესატანი ველი, რომელზეც დაამტებთ onChange მოვლენას რომ დაადგინოთ რაიმე ტექსტის ცვლილება ველში, მას უტოლებთ jsx გამოსახუელბას ფუნქციით რომელიც გამოიძახებს setUser-ს ფუქნციას, ამისთვის უნდა გქონდეთ დაიმპორტებული useState და აღებული user მდგომარეობა რომელიც თავიდან ცარიელი სტრინგის ტოლია. შესტანი ველის მნიშვნლობის ატრიბუტიც გაუტელეთ user მდგომარეობას და კომენტარებით დაწერეთ თქვენი აზრით როგორ გაძლევთ input-ის მნიშვნლობის ცვლადთან მიბმა უფრო მეტ კონტროლს კომპონენტზე


import { useState } from "react";

function App() {
    const [user, setUser] = useState("");
    return (
        <input placeholder="username" value={user} onChange={target => setUser(main.target.value)} />
    );
}
export default App;

