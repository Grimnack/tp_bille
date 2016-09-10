import Environnement as env

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
