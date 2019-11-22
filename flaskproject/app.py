from flask import Flask
from flask import render_template

app = Flask(__name__)  #creates an app

@app.route('/')
def webprint():
    return render_template('web.html')

if __name__ == "__main__":
    app.run(debug=True)
