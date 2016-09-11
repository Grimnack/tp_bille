import Environnement as env
import random 
import Bille as b
import State as s
import Window as w
import random
from tkinter import *

class SMA(object):
    """docstring for SMA
    Il n'y a pas d'implementation en python mais on lui donne le même comportement qu'un observable
    """
    def __init__(self,gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,delay,scheduling,nbTicks,trace,seed,refresh,nbParticles,torique):
        super(SMA, self).__init__()
        self.env = env.Environnement(gridSizeX,gridSizeY,torique=torique)
        self.delay = delay
        self.scheduling = scheduling
        self.nbTicks = nbTicks
        self.nbActualTicks = 1
        self.trace = trace
        self.refresh = refresh
        self.lesBilles = []
        lesDirections = [(0,-1),(0,1),(1,-1),(1,1),(1,-1),(1,1),(-1,-1),(-1,1)]
        self.colors = ['red','firebrick', 'magenta2','green','yellow','magenta','blue','black', 'chocolate']
        indiceColor = 0
        random.seed(seed)
        self.fenetre = w.Window(gridSizeX=gridSizeX,gridSizeY=gridSizeY,canvasSizeX=canvasSizeX,canvasSizeY=canvasSizeY)
        self.fenetre.grille()
        for i in range(nbParticles) :
            (x,y) = self.env.getFreeXYAlea()
            color = self.colors[indiceColor]
            indiceColor = (indiceColor + 1)%(len(self.colors))
            direction = random.choice(lesDirections)
            state = s.State(x,y,direction)
            bille = b.Bille(color, i, state, self.env)
            self.fenetre.place_bille(bille,i)
            self.env.ajouteBille(bille)
            self.lesBilles.append(bille)

        print("Placement aléatoire des billes (tour 0)")
        self.affiche()

    def affiche(self):
        self.fenetre.can.after(self.refresh,self.theloop)
        self.fenetre.can.mainloop()

    def theloop(self):
        #1. Nettoie l'écran        
        self.fenetre.can.delete("all")
        self.fenetre.grille()

        #2. Les billes décident de leur nouvelles positions
        if self.scheduling in ("random","rand","aleatoire","alea","aléatoire","shuffle"):
            random.shuffle(self.lesBilles)

        for bille in self.lesBilles:
            bille.decide()
            self.fenetre.place_bille(bille,bille.indice)

        print("Fin du tour n°"+str(self.nbActualTicks))

        #Fin du programme ou pas
        # 0 = infini
        # Voir si on a atteint le nombre de ticks demandés par l'utilisateur
        if((self.nbTicks == 0) or (self.nbActualTicks < self.nbTicks)):
            self.nbActualTicks = self.nbActualTicks + 1
            self.fenetre.can.after(self.refresh,self.theloop)



simulation = SMA(gridSizeX=100,gridSizeY=100,canvasSizeX=1200,canvasSizeY=900,delay="LUL",scheduling="random",nbTicks=0,trace="LUL",seed="LUL",refresh=1,nbParticles=1000,torique=False)





