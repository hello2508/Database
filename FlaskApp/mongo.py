from flask import Flask, render_template, request, redirect
from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)


# Mongo

# mongo_meta = PyMongo(app, uri="mongodb://18.141.0.98/goodread")
client = MongoClient("mongodb://18.141.0.98/goodread")
db = client.mymongodb # Select the database
todos = db.todo # Select the collection name

@app.route("/monmon")
def mongostuff():
    # standuser = mongo.db.books
    nezuko = mongo_meta.db.metadata
    # name = standuser.find_one({"name": "Giss"})
    # results = standuser.find({"name": "some book"})
    # demons = nezuko.distinct('categories')
    # demons = nezuko.find('png')
    demons = nezuko.distinct('categories')

    # Method 2 of printing Cursor stuff
    # blah = ""
    # for curse in demons:
    #     blah += str(curse)

    # return str(blah)
    # Method 1 of printing Cursor Stuff
    # dump(results) to ddeal with Cursor
    return dumps(demons)

# getting the categories
@app.route('/category',  methods=['GET'])
def test():
	if request.method == 'GET':
		data = mongo_meta.db.metadata
		category = data..distinct('categories')
		# Display categories
		cat = todos.find('categories')
		a1 = 'active'
		return render_template('mongo.html', a1=a1, todos-=cat, t=title, h=heading)







if __name__ == "__main__":
	app.run(host="0.0.0.0", port=27017,debug=True)
