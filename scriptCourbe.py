import SMA
import time

# Pour simplifier on va seulement augmenter le nombre de bille 
# dans un même environnement
# On va mesurer le temps cpu pour une instance de 1000 ticks

for nbParticles in range(1000) :
    temps1 = time.clock()
    SMA.SMA(gridSizeX=100,gridSizeY=100,canvasSizeX=800,canvasSizeY=600,refresh=1,scheduling="",nbTicks=10,trace=False,grid=False,seed=None,delay=1,nbParticles=nbParticles,torique=False)
    temps2 = time.clock()
    print(str(nbParticles)+" "+str((temps2-temps1)/10))