from ma import ma
from models.cliente import ClienteModel

class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ClienteModel
        load_instance = True
        