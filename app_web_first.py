from flask import Flask,render_template,request,jsonify
import os

app = Flask(__name__)

@app.route("/hello", methods=["POST"])
def hello():
    print("✅ /hello endpoint hit")
    data = request.get_json()
    print(data)
    name = data.get("name", "Guest")
    return jsonify({"message": f"Hello {name}! 🚀"})

@app.route("/")
def home():
    return render_template("index.html", title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/skills")
def skills():
    return render_template("skills.html", title="Skills")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
