from flask import Flask, render_template, jsonify, url_for
# from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)  #creates an app

# mongo_store = PyMongo(app, uri="mongodb://18.141.0.98/goodread")
# mongo_store = PyMongo(app, uri="mongodb://localhost:27017/nezukodb")
# metadata = mongo_store.db.metadata


mongo_store = MongoClient("mongodb://localhost:27017")
metadata = mongo_store.nezukodb.metadata
logs = mongo_store.nezukodb.logs
# logs = mongo_store.logs

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


if __name__ == "__main__":
    app.run(debug=True)
