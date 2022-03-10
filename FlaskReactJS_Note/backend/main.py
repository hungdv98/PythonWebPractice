from flask import Flask
from flask_restx import Api 
from models import Note
from exts import db 
from flask_migrate import Migrate 
from notes import note_ns 

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app, doc="/docs")
    api.add_namespace(note_ns)

    @app.shell_context_processor
    def make_shell_context():
        return {
            "db":db,
            "Note": Note
        }

    return app 

