from flask import Flask, render_template, request, redirect, url_for
import os
from flask_pymongo import PyMongo
from datetime import datetime
from bson.objectid import ObjectId

# from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

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
    return redirect("/user/"+name)
    
@app.route("/user/<username1>", methods=["GET", "POST"])
def show_user(username1):
    if request.method=="POST":
        form_values = request.form.to_dict()
        # line 37 is for putting values into dictionary
        form_values["calorie"]=int(request.form["steps"])*0.04
        form_values["date"] = datetime.today()
        _id = mongo.db[username1].insert(form_values)
        # line 39 is for inserting/updating the values into Mongo Database
        return redirect(username1+"/calorie/"+str(_id))
    walks = mongo.db[username1].find()
    print(walks)
    return render_template("userstepsandhistory.html", username1=username1, walks=walks)
    
@app.route("/<username1>/calorie/<calorie_id>")
def show_calorie(username1, calorie_id):
    walk = mongo.db[username1].find_one({"_id": ObjectId(calorie_id)})
    return render_template("calorie.html", walk=walk)




if __name__ == "__main__":
        app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)


