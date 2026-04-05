
console.log("✅ script.js loaded");

document.addEventListener("DOMContentLoaded", function () {
    console.log("✅ DOM fully loaded");

    const button = document.getElementById("submitBtn");

    button.addEventListener("click", function () {
        console.log("✅ Button clicked");

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
        })
        .catch(error => {
            console.error("❌ Fetch error:", error);
        });
    });
});
