const playerScoreP = document.getElementById("playerScoreP")
const compScoreP = document.getElementById("compScoreP")
const compChoiceP = document.getElementById("compChoiceP")
const resultDisplay = document.getElementById("gameRes")

const options = ["rock", "paper", "scissors"]

let playerScore = 0
let compScore = 0

function gameLog(clickEvent) {
    let randomNumber = Math.floor(Math.random() * 3)
    let computerDecison = options[randomNumber]
    let playerChoice = clickEvent.target.textContent.toLowerCase()

    compChoiceP.textContent = "Computer choice: " + computerDecison

    if (
        (playerChoice === "rock" && computerDecison === "scissors") ||
        (playerChoice === "scissors" && computerDecison === "paper") ||
        (playerChoice === "paper" && computerDecison === "rock")
    ) {
        resultDisplay.textContent = "You win!"
        playerScore++
    } else if (playerChoice === computerDecison) {
        resultDisplay.textContent = "It's a draw!"
    } else {
        resultDisplay.textContent = "Computer wins!"
        compScore++
    }

    playerScoreP.textContent = "Your score: " + playerScore
    compScoreP.textContent = "Computer score: " + compScore
}

 