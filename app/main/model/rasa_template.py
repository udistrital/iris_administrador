from .. import db, flask_bcrypt


class RasaTemplate(db.Model):
    """ Rasa_Template Model for storing Rasa_Template related details """
    __tablename__ = "rasa_template"
    __table_args__ = {"schema": "chat_bot"}

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    tem_name = db.Column("tem_name", db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return "<RasaTemplate '{}'>".format(self.tem_name)
