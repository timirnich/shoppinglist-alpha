from flask import redirect, render_template, request
from flask import Blueprint

from shoppinglist.database import get_db

bp = Blueprint("list", __name__)

@bp.route('/')
def index():
	db = get_db()
	shoppinglist = db.execute(
		"SELECT item"
		"FROM shoppinglist"
	).fetchall()
	return render_template('index.html', shoppinglist_formatted=list(shoppinglist))

@bp.route('/addentry', methods=['POST'])
def add_value():
	item = request.form['value']
	print("Received entry " + item + ", adding to shopping list...")
	db = get_db()
	db.execute(
		"INSERT INTO shoppinglist (item, quantity) VALUES (?, ?)",
		(item, 1)
	)
	db.commit()
	return redirect("/", code=302)

@bp.route('/removeentry', methods=['POST'])
def remove_value():
	item = request.form['value']
	print("Received entry " + item + ", removing from shopping list...")
	db = get_db()
	db.execute(
		"DELETE FROM shoppinglist WHERE item = ?",
		(item)
	)
	return redirect("/", code=302)

