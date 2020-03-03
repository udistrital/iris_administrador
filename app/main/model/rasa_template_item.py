from .. import db, flask_bcrypt


class RasaTemplateItem(db.Model):
    """ rasa_template_item Model for storing rasa_template_item related details """
    __tablename__ = "rasa_template_item"
    __table_args__ = {"schema": "chat_bot"}

    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    item_type = db.Column("item_type", db.String(100), nullable=False)
    item_value = db.Column("item_value", db.String(100), nullable=False)
    tem_id = db.Column("tem_id", db.Integer, nullable=True)

    def __repr__(self):
        return "<RasaTemplateItem '{}'>".format(self.id)
