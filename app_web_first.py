from flask import Flask 
app = Flask(__name__)

@app.route('/') 
def Home(): 
    return """ 
    <htlm>
    <head>
        <title>Flask App</title>
    </head>
    <body>
        <h1>Welcome to My Flask App</h1>
        <p>This is a simple web application built with Flask.</p>
    </body>
    </html>
  """

if __name__ == '__main__': 
    app.run(debug=True)
