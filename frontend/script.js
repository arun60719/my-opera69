const searchBar = document.getElementById('searchBar');
const loadLinkBtn = document.getElementById('loadLinkBtn');
const miniScreensContainer = document.getElementById('miniScreensContainer');
const loginBtn = document.getElementById('loginBtn');
const loginModal = document.getElementById('loginModal');
const closeButton = document.querySelector('.close-button');
const loginEmailInput = document.getElementById('loginEmail');
const loginPasswordInput = document.getElementById('loginPassword');
const loginSubmitBtn = document.getElementById('loginSubmit');
const loginError = document.getElementById('loginError');

let userId = localStorage.getItem('userId');
const numberOfScreens = 1000;
let miniScreenStates = {};

function generateMiniScreens(states = {}) {
    miniScreensContainer.innerHTML = '';
    for (let i = 0; i < numberOfScreens; i++) {
        const miniScreen = document.createElement('div');
        miniScreen.classList.add('mini-screen');
        const iframe = document.createElement('iframe');
        const savedUrl = states[i] || '';
        iframe.src = savedUrl;
        miniScreen.appendChild(iframe);
        miniScreensContainer.appendChild(miniScreen);
    }
}

loadLinkBtn.addEventListener('click', () => {
    const link = searchBar.value;
    for (let i = 0; i < numberOfScreens; i++) {
        miniScreenStates[i] = link;
    }
    generateMiniScreens(miniScreenStates);
    if (userId) {
        fetch(/api/users/${userId}/mini_screens, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(miniScreenStates),
        });
    }
});

loginBtn.addEventListener('click', () => {
    loginModal.style.display = 'block';
});

closeButton.addEventListener('click', () => {
    loginModal.style.display = 'none';
});

window.addEventListener('click', (event) => {
    if (event.target == loginModal) {
        loginModal.style.display = 'none';
    }
});

loginSubmitBtn.addEventListener('click', async () => {
    const email = loginEmailInput.value;
    const password = loginPasswordInput.value;

    const response = await fetch('/api/users/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
    });

    const data = await response.json();

    if (response.ok) {
        userId = data.user_id;
        localStorage.setItem('userId', userId);
        loginModal.style.display = 'none';
        await loadPreviousStates();
    } else {
        loginError.textContent = data.message;
    }
});

async function loadPreviousStates() {
    if (userId) {
        const response = await fetch(/api/users/${userId}/mini_screens);
        const data = await response.json();
        miniScreenStates = data;
        generateMiniScreens(miniScreenStates);
    } else {
        generateMiniScreens(); // Generate empty screens if not logged in
    }
}

// Initial load
loadPreviousStates();
generateMiniScreens(); // Generate initial empty screens