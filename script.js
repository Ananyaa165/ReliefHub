document.addEventListener('DOMContentLoaded', () => {
  
  fetch('header.html')
    .then(res => res.text())
    .then(data => {
      document.getElementById('header').innerHTML = data;

      
      const menuBtn = document.getElementById("menu-btn");
      if (menuBtn) {
        menuBtn.addEventListener("click", () => {
          const menu = document.getElementById("mobile-menu");
          if (menu) {
            menu.classList.toggle("hidden");
          }
        });
      }
    });

  
  fetch('footer.html')
    .then(res => res.text())
    .then(data => {
      document.getElementById('footer').innerHTML = data;
    });

  
  const form = document.getElementById('travelForm');
  const output = document.getElementById('output');
  const radioLabels = document.querySelectorAll('.radio-label');

  if (form) {
    radioLabels.forEach(label => {
      label.addEventListener('click', () => {
        radioLabels.forEach(l => l.classList.remove('highlighted'));
        label.classList.add('highlighted');
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();

      const name = document.querySelector('#name').value;
      const email = document.querySelector('#email').value;
      const destination = document.querySelector('#destination').value;
      const travelTime = document.querySelector('input[name="travelTime"]:checked')?.value || "Not selected";

      output.classList.remove('hidden');
      output.innerHTML = `
        <h2 class="text-xl font-semibold text-green-600 mb-4">Submitted Information</h2>
        <p><strong>Full Name:</strong> ${name}</p>
        <p><strong>Email:</strong> ${email}</p>
        <p><strong>Destination:</strong> ${destination}</p>
        <p><strong>Preferred Time:</strong> ${travelTime}</p>
      `;
    });
  }

  
  const container = document.getElementById("destinations");
  if (container) {
    fetch("https://jsonplaceholder.typicode.com/posts?_limit=6")
      .then(res => res.json())
      .then(data => {
        data.forEach(post => {
          const div = document.createElement("div");
          div.className = "bg-blue-50 rounded-lg shadow-md p-4";
          div.innerHTML = `<h3 class="font-bold text-xl mb-2">${post.title}</h3><p>${post.body}</p>`;
          container.appendChild(div);
        });
      });
  }
});
