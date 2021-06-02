from flask import Flask

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
