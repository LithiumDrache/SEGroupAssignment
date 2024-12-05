document.addEventListener('DOMContentLoaded', () => {
    const emailStep = document.getElementById('email-step');
    const genderStep = document.getElementById('gender-step');
    const locationStep = document.getElementById('location-step');
    const genreStep = document.getElementById('genre-step');

    const emailBtn = document.getElementById('email-btn');
    const genderBtn = document.getElementById('gender-btn');
    const locationBtn = document.getElementById('location-btn');
    const surveyform = document.getElementById('survey-form');

    const emailError = document.getElementById('email-error-message');
    const genderError = document.getElementById('gender-error-message');
    const locationError = document.getElementById('location-error-message');
    const genreError = document.getElementById('genre-error-message');

    const surveyData = {};

    emailBtn.addEventListener('click', () => {
        const email = document.getElementById('email').value.trim();
        if (email && /\S+@\S+\.\S+/.test(email)) {
            surveyData.email = email;
            emailStep.style.display = 'none';
            genderStep.style.display = 'block';
        } else {
            emailError.style.display = 'block';
        }
    });

    genderBtn.addEventListener('click', () => {
        const selectedGender = document.querySelector('input[name="gender"]:checked');

        if (selectedGender) {
            surveyData.gender = selectedGender.value;

            genderStep.style.display = 'none';
            locationStep.style.display = 'block';
        } else {
            genderError.style.display = 'block';
        }
    });

    locationBtn.addEventListener('click', () => {
        const country = document.getElementById('country').value;
        if (country) {
            surveyData.location = country;
            locationStep.style.display = 'none';
            genreStep.style.display = 'block';
        } else {
            locationError.style.display = 'block';
        }
    });

    surveyForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const genre = document.getElementById('genre').value.trim();
        if (genre) {
            surveyData.genre = genre;
            console.log('Survey Data:', surveyData);
        } else {
            genreError.style.display = 'block';
        }
    });



});