// 1) შექმენით ფორმა, სადაც მომხმარებელი შეიყვანს სრულ სახელს, ელფოსტას და ტელეფონის ნომერს. ფორმის გაგზავნისას ეს ინფორმაცია დაემატოს ქვემოთ არსებულ  ცხრილში ახალ რიგად. გამოიყენეთ JavaScript-ში შექმნილი container და presentational ფუნქციები, რომლებსაც ექნებათ განსხვავებული დანიშნულება, container  ფუნქცია მოამზადებს მონაცემებს და შექმნის tr ელემენტს, ხოლო presentational ფუნქცია დაამატებს მას ცხრილში. კომენტარებით ახსენით თითოეული ფუნქციის როლი


const myForm = document.querySelector("userForm");
const dataTable = document.querySelector("dataTable");

function presentational(data) {
  const row = `
    <tr>
      <td>${data.username}</td>
      <td>${data.email}</td>
      <td>${data.telephone}</td>
    </tr>
  `;
  dataTable.innerHTML += row;
}


function container(event) {
    event.preventDefault();
    const username = myForm.elements.username.value;
    const email = myForm.elements.email.value;
    const telephone = myForm.elements.telephone.value;

    const person = {
        username: username,
        email: email,
        telephone: telephone
  };

  presentational(person);
  myForm.reset();
}

myForm.addEventListener("submit", container);
