from flask import render_template, Blueprint

medium_blueprint = Blueprint('medium_article',__name__) #creates a blueprint for our medium article
@medium_blueprint.route('/articlelist') #listens to URL /articlelist and renders a template file index.html
def index():
 return render_template("index.html")
