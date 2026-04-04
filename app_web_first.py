from flask import Flask,render_template,request
import os

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    name = None
    if request.method == "POST":
       name = request.form.get("username") 
     
    return render_template("index.html",name=name)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
