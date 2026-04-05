
alert("✅ script.js loaded");

function sendName() {
    const name = document.getElementById("nameInput").value;

    fetch("/hello", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: name })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerText = data.message;
    });
}
