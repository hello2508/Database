from flask import Flask, render_template, jsonify, url_for
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)  #creates an app

mongo_store = PyMongo(app, uri="mongodb://18.141.0.98/goodread")
#mongo_store = PyMongo(app, uri="mongodb://localhost:27017/nezukodb")
metadata = mongo_store.db.metadata
# logs = mongo_store.logs

@app.route('/')
def webprint():
    return render_template('hompage.html')

@app.route("/monstercat/<category>")
def monstercat(category):
    # name = standuser.find_one({"name": "Giss"})
    # results = standuser.find({"name": "some book"})
    # demons = nezuko.distinct('categories')
    # demons = nezuko.find('png')
    # demons = nezuko.distinct('categories')
    # demons = nezuko.distinct('categories')

    newarr = []
    print('hello world')
    # categories = metadata.find({'categories': {"$elemMatch": {"$elemMatch": {"$eq": category} } }}, {'asin': 1, '_id': 0 })
    categories = metadata.find({'categories': {"$elemMatch": {"$elemMatch": {"$eq": category} } }}, {'imUrl': 1, 'asin': 1, '_id': 0 })

    # for x in categories:
    #     newarr.append(x['asin'])

    # Method 2 of printing Cursor stuff
    # blah = ""
    # for curse in demons:
    #     blah += str(curse)

    # return str(blah)
    # Method 1 of printing Cursor Stuff
    # dump(results) to ddeal with Cursor


    return render_template('monstercat.html', categories=categories)
    #     f'''
    #     <h1>{category}</h1>
    #     <img src="{metadata[newarr[0]].imUrl}" >
    # '''

@app.route('/category')
def categorypage():
    return render_template('categorypage2.html')

if __name__ == "__main__":
    app.run(debug=True)
