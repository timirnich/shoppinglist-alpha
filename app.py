from flask import Flask, redirect, render_template, request

import os


app = Flask(__name__)
app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, "shoppinglist.sqlite")
)

import database
database.init_app(app)

@app.route('/')
def index():
	db = database.get_db()
	shoppinglist = db.execute(
		"SELECT item"
		"FROM shoppinglist"
	).fetchall()
	return render_template('index.html', shoppinglist_formatted=list(shoppinglist))

@app.route('/addentry', methods=['POST'])
def add_value():
	item = request.form['value']
	print("Received entry " + item + ", adding to shopping list...")
	db = database.get_db()
	db.execute(
		"INSERT INTO shoppinglist (item, quantity) VALUES (?, ?)",
		(item, 1)
	)
	db.commit()
	return redirect("/", code=302)

@app.route('/removeentry', methods=['POST'])
def remove_value():
	item = request.form['value']
	print("Received entry " + item + ", removing from shopping list...")
	db = database.get_db()
	db.execute(
		"DELETE FROM shoppinglist WHERE item = ?",
		(item)
	)
	return redirect("/", code=302)

if __name__ == '__main__':
    app.run()
