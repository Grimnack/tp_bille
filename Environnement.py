class Environnement(object):
    """docstring for Environnement"""
    def __init__(self, tailleX, tailleY,torique=False):
        super(Environnement, self).__init__()
        self.grille = [[None] * tailleX for _ in range(tailleY)]
        self.torique = torique