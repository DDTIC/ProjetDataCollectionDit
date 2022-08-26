#import pymysql as pymysql
import sqlite3

class Connexion:
    @classmethod
    def getConnexion(cls):
        ## création de la base de données
        conn = sqlite3.connect('projetDataCollection.bd')

        return conn