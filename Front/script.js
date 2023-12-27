$(document).ready(function(){
    console.log("Fuck you")
})

function moveToNextInput(currentInput, nextInputId) {
    if (currentInput.value.length === currentInput.maxLength) {
        document.getElementById(nextInputId).focus();
    }
}
function moveToPreviousInput(currentInput, previousInputId, nextInputId) {
    if (currentInput.value.length === 0) {
        document.getElementById(previousInputId).focus();
    } else if (currentInput.value.length === currentInput.maxLength) {
        document.getElementById(nextInputId).focus();
    }
}