from tkinter import *
import Bille as b
import State as s


class Window(object):
    """docstring for Window"""
    def __init__(self, gridSizeX=20,gridSizeY=10,canvasSizeX=1337,canvasSizeY=420,boxSize=None):
        super(Window, self).__init__()
        self.gridSizeX = gridSizeX
        self.gridSizeY = gridSizeY
        self.canvasSizeX = canvasSizeX
        self.canvasSizeY = canvasSizeY
        self.boxSize = boxSize
        if boxSize == None :

            self.caseX = self.canvasSizeX // self.gridSizeX
            self.caseY = self.canvasSizeY // self.gridSizeY

        else :
            self.caseX,self.caseY = boxSize

        self.fenetre = Tk()

        self.can = Canvas(self.fenetre, width =self.canvasSizeX, height =self.canvasSizeY, bg ='ivory')
        self.can.pack(side =TOP)


        for ligne in range(self.gridSizeY):
            self.can.create_line(0, ligne * self.caseY, self.canvasSizeX, ligne * self.caseY, fill ='blue')  

        for colonne in range(self.gridSizeX):
            self.can.create_line(colonne * self.caseX, 0, colonne * self.caseX, self.canvasSizeY, fill ='green')  
    
    def grille(self) :
        '''
        dessine notre magnifique grille
        '''
        for ligne in range(self.gridSizeY):
            self.can.create_line(0, ligne * self.caseY, self.canvasSizeX, ligne * self.caseY, fill ='blue')  

        for colonne in range(self.gridSizeX):
            self.can.create_line(colonne * self.caseX, 0, colonne * self.caseX, self.canvasSizeY, fill ='green')  
    
    def cercle(self,x, y, r, coul ='black',tag='tamere'):
        '''
        tracé d'un cercle de centre (x,y) et de rayon r
        Fonction reprise sur http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre8
        '''
        self.can.create_oval(x-r, y-r, x+r, y+r, outline=coul, fill=coul, tags=tag)
        
    def place_bille(self,bille) :
        self.cercle(bille.state.x*self.caseX + self.caseX//2, bille.state.y * self.caseY + self.caseY // 2,min(self.caseX,self.caseY)/2 ,coul =bille.color)
 


window = Window()
state = s.State(1,3,'N')
bille = b.Bille('red',0,state,None)
window.place_bille(bille)
window.can.delete('tamere')
window.fenetre.mainloop()