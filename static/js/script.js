// Add click event to survey buttons
document.querySelectorAll('.survey-btn').forEach(button => {
    button.addEventListener('click', () => {
        alert('Redirecting to Survey...');
        // Replace this alert with the actual survey URL or modal opening code
    });
});

document.addEventListener('DOMContentLoaded', () => {
    const emailStep = document.getElementById('email-step');
    const ageStep = document.getElementById('age-step');
    const genderStep = document.getElementById('gender-step');
    const emailForm = document.getElementById('email-form');
    const ageForm = document.getElementById('age-form');
    const genderForm = document.getElementById('gender-form');
    const errorMessage = document.getElementById('error-message');

    // Store survey data
    let surveyData = {};

    // Handle Email Form Submission
    emailForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const email = document.getElementById('email').value;

        if (validateEmail(email)) {
            errorMessage.style.display = 'none';
            surveyData.email = email;
            emailStep.style.display = 'none';
            ageStep.style.display = 'block'; // Show age step
        } else {
            errorMessage.style.display = 'block';
        }
    });

    // Handle Age Form Submission
    ageForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const selectedAge = document.querySelector('input[name="age"]:checked');

        if (selectedAge) {
            surveyData.age = selectedAge.value;
            ageStep.style.display = 'none';
            genderStep.style.display = 'block'; // Show gender step
        } else {
            alert("Please select an age range to proceed.");
        }
    });

    // Handle Gender Form Submission
    genderForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const selectedGender = document.querySelector('input[name="gender"]:checked');

        if (selectedGender) {
            surveyData.gender = selectedGender.value;
            console.log("Survey Data:", surveyData); // Debugging
            alert(`Gender "${selectedGender.value}" selected. Proceeding to the next step...`);
            // Proceed to the next step (e.g., fashion preferences)
        } else {
            alert("Please select a gender to proceed.");
        }
    });

    // Email Validation Function
    function validateEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }
});
