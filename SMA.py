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
    def __init__(self,gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,delay,scheduling="random",grid,nbTicks=0,trace,seed=None,refresh,nbParticles,torique=False):

        if ( (gridSizeX * gridSizeY) < nbParticles ):
            print("Pas assez d'espace pour places les "+str(nbParticles)+" particules.\nEssayez un plus petit nombre ("+str(gridSizeX * gridSizeY)+" ou moins).")
            return

        super(SMA, self).__init__()
        self.env = env.Environnement(gridSizeX,gridSizeY,torique=torique)
        self.delay = delay
        self.scheduling = scheduling in ("random","rand","aleatoire","alea","aléatoire","shuffle","die","dice")
        self.nbTicks = nbTicks
        self.nbActualTicks = 0
        self.trace = trace
        self.refresh = refresh
        self.grid = grid
        self.lesBilles = []
        lesDirections = [(0,-1),(0,1),(1,-1),(1,1),(1,-1),(1,1),(-1,-1),(-1,1)]
        #self.colors = ['red','firebrick', 'magenta2','green','yellow','magenta','blue','black', 'chocolate']
        #indiceColor = 0
        random.seed(seed)
        self.fenetre = w.Window(gridSizeX=gridSizeX,gridSizeY=gridSizeY,canvasSizeX=canvasSizeX,canvasSizeY=canvasSizeY)
        if self.grid:
            self.fenetre.grille()
        for i in range(nbParticles) :
            (x,y) = self.env.getFreeXYAlea()
            color = "#%06x" % random.randint(0, 0xFFFFFF) #self.colors[indiceColor]
            #indiceColor = (indiceColor + 1)%(len(self.colors))
            direction = random.choice(lesDirections)
            state = s.State(x,y,direction)
            bille = b.Bille(color, i, state, self.env)
            self.fenetre.place_bille(bille,i)
            self.env.ajouteBille(bille)
            self.lesBilles.append(bille)

        if self.trace:
            print("Placement aléatoire des billes (tour 0)")

        self.affiche()

    def affiche(self):
        self.fenetre.can.after(self.delay,self.theloop)
        self.fenetre.can.mainloop()

    def theloop(self):

        self.nbActualTicks = self.nbActualTicks + 1

        # 1. Les billes décident de leur nouvelles positions. L'ordre de décision est séquentiel (toujours la même balle en premier) ou aléatoire.
        if self.scheduling:
            random.shuffle(self.lesBilles)

        for bille in self.lesBilles:
            bille.decide()

        # 2. Mise à jour de l'affichage tous les refresh ticks. Si refresh = 1, l'affichage est mis à jour à chaque fin de tick.
        if(self.nbActualTicks % self.refresh) == 0 :     
            self.fenetre.can.delete("ball")
            self.fenetre.can.delete("text")
            for bille in self.lesBilles :
                self.fenetre.place_bille(bille,bille.indice)

        if self.trace:
            print("Fin du tour n°"+str(self.nbActualTicks))

        # 3. Terminaison
        # 0 = infini
        # Sinon voir si on a atteint le nombre de ticks demandés par l'utilisateur
        
        if((self.nbTicks==0) or (self.nbActualTicks < self.nbTicks)):
            self.fenetre.can.after(self.delay,self.theloop)


SMA(gridSizeX=50,gridSizeY=50,canvasSizeX=1000,canvasSizeY=800,refresh=1,scheduling="",nbTicks=0,trace=False,grid=True,seed=None,delay=100,nbParticles=5000000,torique=False)





