from flask import Flask,render_template,request
import os

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    data = request.get_json()
    name = data.get("name", "Guest")
    return jsonify({"message": f"Hello {name}! 🚀"})

    
@app.route("/about")
def about(): 
    return render_template("about.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
