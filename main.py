from config import create_app
from db import db

app = create_app()


db.init_app(app)


if __name__ == "__main__":
    app.run()
