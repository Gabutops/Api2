from flask import request
from flask_restplus import Resource, fields
from flask_restplus.utils import default_id
from sqlalchemy.orm import defaultload

from models.cliente import ClienteModel
from schemas.cliente import ClienteSchema

from server.instance import server

cliente_ns = server.cliente_ns

cliente_schema = ClienteSchema()
cliente_list_schema = ClienteSchema(many =True)

ITEM_NOT_FOUND = "ID não encontrado"

item = cliente_ns.model("Banco_de_Dados_Lab",{
    "Dados_de_RNAsec": fields.String(description = "Dados de RNAsec"),
    "Laudos": fields.String(description = "Laudos",default = ""),
    "Laminas": fields.String(description = "imagens de Laminas"),
    "atualizado": fields.DateTime(description = "Data/Hora da atualização dos dados")})

class Cliente(Resource):

    def get(self, ID):
        cliente_data = ClienteModel.find_by_id(ID)
        if cliente_data:
            return cliente_schema.dump,200
        return{'message':ITEM_NOT_FOUND},404
    
class ClienteList(Resource):
    def get(self,):
        return cliente_list_schema.dump(ClienteModel.find_all()),200
    
    @cliente_ns.expect(item)
    @cliente_ns.doc('Criar um Item')
    def post(self):
        cliente_json = request.get_json()
        cliente_data = cliente_schema.load(cliente_json)

        cliente_data.save_to_db()

        return cliente_schema.dump(cliente_data),201
