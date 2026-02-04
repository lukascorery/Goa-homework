const btn = document.getElementById("btn")

const checkbox = document.getElementById("check_box")

console.dir(checkbox)




// alert()
// prompt()
// confirm()


btn.onclick = function() {
    console.dir(`terms and conditions checkbox state ` (checkbox.checked))
    let response =  confirm("are you sure?")
    console.log(response)
}