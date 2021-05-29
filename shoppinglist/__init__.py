import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
	    DATABASE=os.path.join(app.instance_path, "shoppinglist.sqlite")
    )
    
    if test_config is None:
        # load the instance config if it exists
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if provided
        app.config.update(test_config)

    from shoppinglist import database

    database.init_app(app)
    
    from shoppinglist import list

    app.register_blueprint(list.bp)

    return app