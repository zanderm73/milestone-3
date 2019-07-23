import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'milestone_3'
app.config["MONGO_URI"] = 'mongodb+srv://zanderm73:Alex4302@myfirstcluster-8q4gk.mongodb.net/milestone_3?retryWrites=true'

mongo = PyMongo(app)

# renders home page of all recipes
@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template('recipes.html', dfgf_recipes=mongo.db.dfgf_recipes.find())
    
# renders add_recipe page    
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           dfgf_recipes=mongo.db.dfgf_recipes.find())    

# adds the data that was input by the user on the add_recipe page to the mongoDB database
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe = mongo.db.dfgf_recipes
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))

# renders full recipe page based off unique ObjectID
@app.route('/view_recipe')
@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
            the_recipe = mongo.db.dfgf_recipes.find_one({"_id": ObjectId(recipe_id)})
            return render_template('eachrecipe.html', recipe=the_recipe)
            
# renders the edit recipe page         
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.dfgf_recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('editrecipe.html', recipe=the_recipe)

# collects the information of the recipe and allows to be editied on site that then updates the database
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.dfgf_recipes
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'cooking_time':request.form.get('cooking_time'),
        'calories':request.form.get('calories'),
        'ingredients':request.form.get('ingredients'),
        'cooking_instructions': request.form.get('cooking_instructions'),
        'is_dairy_free':request.form.get('is_dairy_free'),
        'is_gluten_free':request.form.get('is_gluten_free'),
        'recipe_author':request.form.get('recipe_author')
    })
    return redirect(url_for('get_tasks'))

# allows the deletion of recipes from the site and databse
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.dfgf_recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_tasks'))

 # renders about_us page   
@app.route('/about_us')
def about_us():
    return render_template("aboutus.html")

# allows the user to vote if they have used the recipe    
@app.route('/upvote/<recipe_id>')
def upvotes(recipe_id):
    mongo.db.dfgf_recipes.find_one_and_update({'_id': ObjectId(recipe_id)},
        {'$inc': {'upvotes': 1}})
    return redirect(url_for('view_recipe', recipe_id=recipe_id)) 

# filters to show only recipes that are dairy free
@app.route('/dairy_free')
def dairy_free():
    return render_template('dairyfree.html', dfgf_recipes=mongo.db.dfgf_recipes.find())

# filters to show only recipes that are gluten free
@app.route('/gluten_free')
def gluten_free():
    return render_template('glutenfree.html', dfgf_recipes=mongo.db.dfgf_recipes.find())

# filters to show only recipes that are dairy and gluten free    
@app.route('/dairy_gluten_free')
def dairy_gluten_free():
    return render_template('dairyglutenfree.html', dfgf_recipes=mongo.db.dfgf_recipes.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)