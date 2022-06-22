from db import db

class ClienteModel(db.Model):
    __tablename__ = 'Banco_de_Dados_Lab'
    
    id = db.Column(db.Integer,primary_key = True)
    RNAsec = db.Column(db.String, nullable = True)
    Laudos = db.Column(db.String, nullable = True)
    Laminas = db.Column(db.String, nullable = True)
    atualizado = db.Column(db.DateTime())
    
    def __init__(self,RNAsec, Laudos,Laminas,atualizado):
        self.RNAsec = RNAsec
        self.Laudos = Laudos 
        self.Laminas = Laminas 
        self.atualizado = atualizado 
    def __repr__(self,):
        return f"ClienteModel(RNAsec={self.RNAsec},Laudos={self.Laudos}, Laminas={self.Laminas}, atualizado={self.atualizado})"
    def json(self,):
        return {
            "Dados_de_RNAsec":self.RNAsec,
            "Laudos":self.Laudos,
            "Laminas":self.Laminas,
            "atualizado":self.atualizado
            }
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()
    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self, ):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()