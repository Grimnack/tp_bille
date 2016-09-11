import random
import Bille as b
import Window as w

class Environnement(object):
    """docstring for Environnement"""
    def __init__(self, tailleX, tailleY,torique=False):
        super(Environnement, self).__init__()
        self.grille = [[None] * tailleX for _ in range(tailleY)]
        self.torique = torique
        self.lesCouples = None

    def genereCouplesXY(self) :
        '''
        ajoute a self la liste des couples X Y possible par rapport aux dimensions de la grille
        '''
        lesCouples = []
        for y in range(len(self.grille)) :
            for x in range(len(self.grille[0])) :
                lesCouples.append((x,y))
        random.shuffle(lesCouples)
        self.lesCouples = lesCouples

    def getFreeXYAlea(self) :
        '''
        donne une coordonnée libre aléatoire
        '''
        if self.lesCouples == None :
            self.genereCouplesXY()
        return self.lesCouples.pop()

    def ajouteBille(self,bille):
        self.grille[bille.state.y][bille.state.x] = bille 