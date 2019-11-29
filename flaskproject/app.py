from flask import Flask, render_template

app = Flask(__name__)  #creates an app

@app.route('/')
def webprint():
    return render_template('hompage.html')

if __name__ == "__main__":
    app.run(debug=True)
