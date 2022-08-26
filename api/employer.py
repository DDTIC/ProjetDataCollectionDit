from fastapi import FastAPI
from bd.traitementBd import EmployerModel
from bd.connexionBd import Connexion
app = FastAPI()

@app.get("/home")
def apiListeEmployer(listeEmployer):
    return listeEmployer

