const $ = require('jquery');
const signup = require('./signup');

test('submit event handler should prevent default form submission', () => {
    // Set up the DOM
    document.body.innerHTML = `
    <form id="signupForm">
      <input type="text" id="name" value="John Doe">
      <input type="email" id="email" value="john.doe@example.com">
      <input type="password" id="password" value="password123">
      <input type="radio" name="inlineRadioOptions" id="role1" value="option1" checked>
      <input type="radio" name="inlineRadioOptions" id="role2" value="option2">
      <button type="submit">Sign Up</button>
    </form>
  `;

    // Call the submit event handler
    const event = $.Event('submit');
    $('#signupForm').trigger(event);

    // Expect the default form submission to be prevented
    expect(event.isDefaultPrevented()).toBe(true);
});