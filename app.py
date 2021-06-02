<<<<<<< HEAD
<<<<<<< Updated upstream
from flask import Flask, redirect, render_template, request, jsonify
=======
from flask import Flask
>>>>>>> Stashed changes
=======
from flask import Flask, redirect, render_template, request
>>>>>>> 52a9544bcae65f4cfdedd697866553033c4b6528

import os


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, "shoppinglist.sqlite")
)
app.config.from_mapping(
	TESTING = True
)

# ensure the instance folder exists
try:
	os.makedirs(app.instance_path)
except OSError:
	pass

from database.database import init_app
init_app(app)

from handlers.routes import configure_routes
configure_routes(app)

if __name__ == '__main__':
    app.run()
