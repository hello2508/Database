from flask import Flask, render_template, jsonify, url_for
# from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)  #creates an app

### Kenneth's EC2 instance
mongo_store = MongoClient("mongodb://18.141.0.98/")
metadata = mongo_store.goodread.metadata

@app.route('/')
def webprint():
    return render_template('hompage.html')


@app.route('/categorypage/<categoryname>')
def categorypage(categoryname):
    categories = metadata.find({'categories': {"$elemMatch": {"$elemMatch": {"$eq": categoryname} } }}, {'imUrl': 1, 'asin': 1, '_id': 0 })

    categories = [i for i in categories]
    # to set limit to how many you want to add
    limit = 10
    # return render_template('categorypage2.html')
    return render_template('categorypage2.html', categories=categories[:limit])

@app.route('/book/<asin>')
def book(asin):
    return


if __name__ == "__main__":
    app.run(debug=True)
