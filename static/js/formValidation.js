// Picking out the form ids
const firstName = document.querySelector('#fname');
const lastName = document.querySelector('#lname');
const emailEl = document.querySelector('#emailAddress');
const passwordEl = document.querySelector('#password');
const confirmPasswordEl = document.querySelector('#passwordConfirm');
const form = document.querySelector('#signup');

// Developing utility functions
const isRequired = value => value === '' ? false : true;
const isBetween = (length, min, max) => length < min || length > max ? false : true;
const isEmailValid = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};
const isPasswordSecure = (password) => {
    const re = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
    return re.test(password);
};

// Function that shows success/error
const showError = (input, message) => {
    // get the form-field element
    const formField = input.parentElement;
    // add the error class
    formField.classList.remove('success');
    formField.classList.add('error');

    // show the error message
    const error = formField.querySelector('small');
    error.textContent = message;
};

const showSuccess = (input) => {
    // get the form-field element
    const formField = input.parentElement;

    // remove the error class
    formField.classList.remove('error');
    formField.classList.add('success');

    // hide the error message
    const error = formField.querySelector('small');
    error.textContent = '';
}

// Validate the names
const checkFirstName = () => {

    let valid = false;
    const min = 2,
        max = 25;
    const fname = firstName.value.trim();

    if (!isRequired(fname)) {
        showError(firstName, 'First Name cannot be blank.');
    } else if (isBetween(firstName.length, min, max)) {
        showError(firstName, `First Name must be between ${min} and ${max} characters.`);
    } else {
        showSuccess(firstName);
        valid = true;
    }
    return valid;
}

const checkLastName = () => {

    let valid = false;
    const min = 2,
        max = 25;
    const lname = lastName.value.trim();

    if (!isRequired(lname)) {
        showError(lastName, 'Last Name cannot be blank.');
    } else if (!isBetween(lastName.length, min, max)) {
        showError(lastName, `Last Name must be between ${min} and ${max} characters.`);
    } else {
        showSuccess(lastName);
        valid = true;
    }
    return valid;
}

// Validate email
const checkEmail = () => {
    let valid = false;
    const email = emailEl.value.trim();
    if (!isRequired(email)) {
        showError(emailEl, 'Email cannot be blank.');
    } else if (!isEmailValid(email)) {
        showError(emailEl, 'Email is not valid.')
    } else {
        showSuccess(emailEl);
        valid = true;
    }
    return valid;
}

// Validate password
const checkPassword = () => {

    let valid = false;

    const password = passwordEl.value.trim();

    if (!isRequired(password)) {
        showError(passwordEl, 'Password cannot be blank.');
    } else if (!isPasswordSecure(password)) {
        showError(passwordEl, 'Password must has at least 8 characters that include at least 1 lowercase character, 1 uppercase characters, 1 number, and 1 special character in (!@#$%^&*)');
    } else {
        showSuccess(passwordEl);
        valid = true;
    }

    return valid;
};

// Validate confirm password
const checkConfirmPassword = () => {
    let valid = false;
    // check confirm password
    const confirmPassword = confirmPasswordEl.value.trim();
    const password = passwordEl.value.trim();

    if (!isRequired(confirmPassword)) {
        showError(confirmPasswordEl, 'Please enter the password again');
    } else if (password !== confirmPassword) {
        showError(confirmPasswordEl, 'Confirm password does not match');
    } else {
        showSuccess(confirmPasswordEl);
        valid = true;
    }

    return valid;
};

const debounce = (fn, delay = 500) => {
    let timeoutId;
    return (...args) => {
        // cancel the previous timer
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        // setup a new timer
        timeoutId = setTimeout(() => {
            fn.apply(null, args)
        }, delay);
    };
};

form.addEventListener('input', debounce(function (e) {
    switch (e.target.id) {
        case 'fname':
            checkFirstName();
            break;
        case 'lname':
            checkLastName();
            break;
        case 'emailAddress':
            checkEmail();
            break;
        case 'password':
            checkPassword();
            break;
        case 'confirmPassword':
            checkConfirmPassword();
            break;
    }
}));

// Adding an event listener to the form
form.addEventListener('submit', (e) => {
    // prevent the form from submitting
    e.preventDefault();

    // validate forms
    let isfirstnameValid = checkFirstName(),
        islastnameValid = checkLastName(),
        isEmailValid = checkEmail(),
        isPasswordValid = checkPassword(),
        isConfirmPasswordValid = checkConfirmPassword();

    let isFormValid = isfirstnameValid &&
        islastnameValid &&
        isEmailValid &&
        isPasswordValid &&
        isConfirmPasswordValid;

    // submit to the server if the form is valid
    if (isFormValid) {

    }
})