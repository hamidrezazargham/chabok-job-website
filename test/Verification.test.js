const Verification = require('./Verification');

test('moveToNextInput should move focus to the next input when current input is full', () => {
    // Set up the DOM
    document.body.innerHTML = `
    <input type="text" id="digit1" maxlength="1">
    <input type="text" id="digit2" maxlength="1">
    <input type="text" id="digit3" maxlength="1">
    <input type="text" id="digit4" maxlength="1">
  `;

    // Call the function
    const input1 = document.getElementById('digit1');
    const input2 = document.getElementById('digit2');
    Verification.moveToNextInput(input1, 'digit2');

    // Expect the focus to be moved to the next input
    expect(document.activeElement).toBe(input2);
});