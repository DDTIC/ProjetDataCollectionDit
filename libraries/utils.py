import random

class Utils(object):
    @classmethod
    def divider(cls, n=150):
        return '-' * n

    @classmethod
    def randomize(cls,
                  start,
                  final):
        return random \
            .randint(start, final)

    @classmethod
    def x(cls, x):
        x = x.split(' ')
        last_name = x[-1].upper()
        first_name = x[0].capitalize()
        x = ' '.join([first_name, last_name])
        return x

    ## methode qui permet de concatener plusieurs listes
    def concatenerPlusieursList(*args):
        listeGenerale = []
        for item in args:
            assert isinstance(item, list), 'attention vous devriez passer une liste'
            listeGenerale += item
        return listeGenerale

    ## Attribuer les éléments d'une liste aléatoirement
    @classmethod
    def randomElement(cls, liste):
        assert isinstance(liste, list), 'attention vous devriez passer une liste'
        return random.choice(liste)


