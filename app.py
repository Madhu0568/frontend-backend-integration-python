from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Frontend Backend Integration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 40px;
        }
        input {
            display: block;
            margin: 10px 0;
            padding: 8px;
            width: 250px;
        }
        button {
            padding: 8px 15px;
        }
        #response {
            margin-top: 15px;
            color: green;
        }
    </style>
</head>
<body>

<h2>Contact Form</h2>

<form id="contactForm">
    <input type="text" id="name" placeholder="Enter Name" required>
    <input type="email" id="email" placeholder="Enter Email" required>
    <button type="submit">Submit</button>
</form>

<p id="response"></p>

<script>
document.getElementById("contactForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    fetch("/submit", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ name: name, email: email })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = data.message;
    });
});
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    name = data.get("name")
    email = data.get("email")

    return jsonify({
        "message": f"Form submitted successfully! Name: {name}, Email: {email}"
    })

if __name__ == "__main__":
    app.run(debug=True)
