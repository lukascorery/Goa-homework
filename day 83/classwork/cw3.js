// 3) მოცემული api-დან fetch-ის, promise, try, catch მეშვეობით წამოიღეთ ინფორმაცია და გამოიტანეთ კონსოლში

const username = document.querySelector("input")
const button = document.querySelector("button")
const div = document.querySelector("div")



button.addEventListener("click", () => {
    let githubUser = username.value;

    let promise  = fetch(`https://api.github.com/users/${githubUser}`)


    promise
        .then((response) => response.json())
        .then((renderInfo))
        .catch((error) => console.log(error))


    console.log(promise);

}) 

function renderInfo(userInfo) {
    div.innerHTML = 
    `
    <h1> ${userInfo.name} </h1>
    <img src="${userInfo.avatar_url}" class="mainimg" alt="user avatar" />
    <p> ${userInfo.bio} </p>
    <p> Followers: ${userInfo.followers} </p>
    <p> Following: ${userInfo.following} </p>
    <a href="${userInfo.html_url}" > Visit Profile </a>
    `
}
