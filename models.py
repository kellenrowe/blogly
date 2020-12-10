from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DFLT_USR_IMG = 'http://shorturl.at/adCL2'


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """ User class """

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                           nullable=False)
    last_name = db.Column(db.String(50),
                          nullable=False)
    pic_url = db.Column(db.Text,
                        nullable=False,
                        default=DFLT_USR_IMG)

    @property
    def full_name(self):
        """ returns full name of user """

        return f"{self.first_name} {self.last_name}"
