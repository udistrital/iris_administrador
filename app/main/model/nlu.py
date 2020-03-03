from .. import db, flask_bcrypt


class Nlu(db.Model):
    """ NLU Model for storing nlu related details """
    __tablename__ = "nlu"
    __table_args__ = {"schema": "chat_bot"}

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    type = db.Column("nlu_type", db.String(100), nullable=False)
    name = db.Column("nlu_name", db.String(100), nullable=False)
    value = db.Column("value", db.String(1000), nullable=False)

    def __repr__(self):
        return "<Nlu '{}'>".format(self.type)
