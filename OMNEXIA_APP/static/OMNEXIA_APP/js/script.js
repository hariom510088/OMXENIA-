document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("contactForm");
  const responseMsg = document.getElementById("responseMsg");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const response = await fetch("/send-message/", {
      method: "POST",
      headers: { "X-CSRFToken": csrftoken },
      body: new URLSearchParams(data),
    });

    const result = await response.json();
    responseMsg.textContent = result.message;
    form.reset();
  });
});
