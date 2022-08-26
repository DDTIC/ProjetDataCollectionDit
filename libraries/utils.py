import random


class Utils(object):
    @classmethod
    def divider(cls, n=54):
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
            listeGenerale += item
        return listeGenerale

    ## Attribuer les éléments d'une liste aléatoirement
    @classmethod
    def randomElement(cls, liste):
        assert isinstance(liste, list)
        return random.choice(liste)

    '''
    @classmethod
    def randomElement(cls, liste, *key):
        assert isinstance(liste, list)
        if len(key) == 0:
            return random.choice(liste)
        else:
            for item in key:
                choix = random.choice(liste)
                return choix[item]
    '''

