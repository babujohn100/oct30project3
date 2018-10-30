from flask import Flask, render_template, request, redirect, url_for
import os
# from flask_pymongo import PyMongo
# from bson.objectid import ObjectId

app = Flask(__name__)

# app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
# app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

# mongo = PyMongo(app)

# def get_category_names():
#     categories = []
#     for category in mongo.db.collection_names():
#         if not category.startswith("system."):
#             categories.append(category)
#     return categories

@app.route("/")
def show_indexpage():
    
    # categories = get_category_names()
     return render_template("index.html")
    
    
@app.route("/search")
def show_search():
    name = request.args.get('username')
    # here search is only a string which can be changed 
    return redirect("/use")
    
@app.route("/user/<username1>")
def show_user(username):
    return username


if __name__ == "__main__":
        app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)


