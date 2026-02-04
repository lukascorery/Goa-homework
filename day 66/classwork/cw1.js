function endresult() {
    let check1 = document.getElementById("check1")
    let check2 = document.getElementById("check2")
    let result = document.getElementById("result")

    let val1 = check1.checked;
    let val2 = check2.cheked;
    let result_end = val1 && val2;

    result.textContent = "result: " + result;
}