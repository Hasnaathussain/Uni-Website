document.addEventListener("DOMContentLoaded", function() {
    loadFaculty();
    loadResearch();
    loadPrograms();

    const contactForm = document.getElementById("contact-form");
    contactForm.addEventListener("submit", handleContactSubmit);
});

function loadFaculty() {
    fetch("/api/faculty")
        .then(response => response.json())
        .then(data => {
            const facultyList = document.querySelector(".faculty-list");
            data.forEach(member => {
                const div = document.createElement("div");
                div.className = "faculty-item";
                div.innerHTML = `
                    <h3>${member.name}</h3>
                    <h3>${member.Designation}</h3>
                    <img src="${member.image}" alt="${member.name}" style="width:100%; max-height:200px; object-fit: cover;">
                    <button class="toggle-button">Show More</button>
                    <div class="toggle-content">
                        <p><b>Qualifications:</b> ${member.Qualifications}</p>
                        <p><b>Publications:</b> <a href="${member.Publications}" target="_blank" rel="noopener noreferrer">${member.Publications}</a></p>                        <p><b>Area:</b> ${member.Area}</p>
                        <p><b>Email:</b> <a href="mailto:${member.email}">${member.email}</a></p>
                        <p><b>Office:</b> ${member.office || 'N/A'}</p>
                        <p><b>Phone:</b> ${member.phone || 'N/A'}</p>
                    </div>
                `;
                facultyList.appendChild(div);
                div.querySelector(".toggle-button").addEventListener("click", function() {
                    const content = this.nextElementSibling;
                    content.style.display = content.style.display === "block" ? "none" : "block";
                    this.textContent = content.style.display === "block" ? "Show Less" : "Show More";
                });
            });
        })
        .catch(error => console.error("Error loading faculty:", error));
}

function loadResearch() {
    fetch("/api/research")
        .then(response => response.json())
        .then(data => {
            const researchList = document.querySelector(".research-list");
            data.forEach(area => {
                const div = document.createElement("div");
                div.className = "research-item";
                div.innerHTML = `
                    <h3>${area.title}</h3>
                    <button class="toggle-button">Show More</button>
                    <div class="toggle-content">
                        <p>${area.description}</p>
                        <p><b>Principal Investigator:</b> ${area.pi || 'N/A'}</p>
                        <p><b>Keywords:</b> ${area.keywords || 'N/A'}</p>
                    </div>
                `;
                researchList.appendChild(div);
                div.querySelector(".toggle-button").addEventListener("click", function() {
                    const content = this.nextElementSibling;
                    content.style.display = content.style.display === "block" ? "none" : "block";
                    this.textContent = content.style.display === "block" ? "Show Less" : "Show More";
                });
            });
        })
        .catch(error => console.error("Error loading research areas:", error));
}

function loadPrograms() {
    fetch("/api/programs")
        .then(response => response.json())
        .then(data => {
            const programsList = document.querySelector(".programs-list");
            data.forEach(program => {
                const div = document.createElement("div");
                div.className = "program-item";
                div.innerHTML = `
                    <h3>${program.name}</h3>
                    <button class="toggle-button">Show More</button>
                    <div class="toggle-content">
                        <p><b>Prerequisite qualifications:</b> ${program.Prerequisite}</p>
                        <p><b>Duration:</b> ${program.duration}</p>
                        <p><b>Credits:</b> ${program.credits}</p>
                        <p>${program.description}</p>
                    </div>
                `;
                programsList.appendChild(div);
                div.querySelector(".toggle-button").addEventListener("click", function() {
                    const content = this.nextElementSibling;
                    content.style.display = content.style.display === "block" ? "none" : "block";
                    this.textContent = content.style.display === "block" ? "Show Less" : "Show More";
                });
            });
        })
        .catch(error => console.error("Error loading programs:", error));
}

function handleContactSubmit(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    fetch("/api/contact", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        event.target.reset();
    });
}

function openTab(evt, tabName) {
    let i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}
// ... (your existing JavaScript code) ...

// Theme Toggle
// Theme Toggle
const themeToggle = document.getElementById("theme-toggle");

function applyTheme(theme) {
  document.body.dataset.theme = theme;
  localStorage.setItem("theme", theme);
}

function toggleTheme() {
  const currentTheme =
    document.body.dataset.theme === "dark" ? "light" : "dark";
  applyTheme(currentTheme);
}

themeToggle.addEventListener("click", toggleTheme);

// Apply the saved theme on page load
const savedTheme = localStorage.getItem("theme") || "light";
applyTheme(savedTheme);
