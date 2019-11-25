from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)  #creates an app

mongo_store = PyMongo(app, uri="mongodb://18.141.0.98/goodread")


@app.route('/')
def webprint():
    return render_template('hompage.html')



@app.route("/monmon")
def mongostuff():
    # standuser = mongo.db.books
    nezuko = mongo_store.db.metadata
    # name = standuser.find_one({"name": "Giss"})
    # results = standuser.find({"name": "some book"})
    # demons = nezuko.distinct('categories')
    # demons = nezuko.find('png')
    # demons = nezuko.distinct('categories')
    demons = nezuko.distinct('categories')

    newarr = []

    # db.metadata.find({'categories': {$elemMatch: {$elemMatch: {$eq: "Reference"}}}}).count()
    # for x in uniques:

    # Method 2 of printing Cursor stuff
    # blah = ""
    # for curse in demons:
    #     blah += str(curse)

    # return str(blah)
    # Method 1 of printing Cursor Stuff
    # dump(results) to ddeal with Cursor


    return dumps(demons)

if __name__ == "__main__":
    app.run(debug=True)
