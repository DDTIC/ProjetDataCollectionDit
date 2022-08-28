from sqlalchemy import create_engine

class Connexion:
    @classmethod
    def getConnexion(cls):
        ## Création base de données sqlite
        engine = create_engine('sqlite:///projetDataCollectionBd.db', echo=False)

        return engine
