import Environnement as env
import random 
import Bille as b
import State as s

class SMA(object):
    """docstring for SMA
    Il n'y a pas d'implementation en python mais on lui donne le même comportement qu'un observable
    """
    def __init__(self,gridSizeX,gridSizeY,delay,sheduling,nbTicks,trace,seed,refresh,nbParticles,torique):
        super(SMA, self).__init__()
        self.env = env.Environnement(gridSizeX,gridSizeY,torique=torique)
        self.delay = delay
        self.sheduling = sheduling
        self.nbTicks = nbTicks
        self.trace = trace
        self.refresh = refresh
        self.lesBilles = []
        lesDirections = [(0,-1),(0,1),(1,-1),(1,1),(1,-1),(1,1),(-1,-1),(-1,1)]
        colors = ['red','firebrick','green','yellow','magenta','blue','black']
        indiceColor = 0
        random.seed(seed)
        for i in range(nbParticles) :
            (x,y) = getFreeXYAlea()
            color = self.colors[indiceColor]
            if indiceColor == len(colors) -1 :
                indiceColor = 0
            else :
                indiceColor += 1
            direction = random.choice(lesDirections)
            state = s.State(x,y,direction)
            bille = b.Bille(color, i, state, self.env)
            self.env.ajouteBille(bille)
            self.lesBilles.append(bille)