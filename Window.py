from tkinter import *
import Bille as b
import State as s


class Window(object):
    """docstring for Window"""
    def __init__(self, gridSizeX,gridSizeY,canvasSizeX,canvasSizeY,boxSize=None):
        #super(Window, self).__init__()
        self.gridSizeX = gridSizeX
        self.gridSizeY = gridSizeY
        self.canvasSizeX = canvasSizeX
        self.canvasSizeY = canvasSizeY
        self.boxSize = boxSize
        if boxSize == None :

            self.caseX = self.canvasSizeX / self.gridSizeX
            self.caseY = self.canvasSizeY / self.gridSizeY

        else :
            self.caseX,self.caseY = boxSize

        self.tk = Tk()
        self.tk.title('KKona')

        self.can = Canvas(self.tk, width =self.canvasSizeX, height =self.canvasSizeY, bg ='ivory')
        self.can.pack(side=TOP)

    
    def grille(self) :
        '''
        dessine notre magnifique grille
        '''
        for ligne in range(self.gridSizeY):
            self.can.create_line(0, ligne * self.caseY, self.canvasSizeX, ligne * self.caseY, fill ='blue')  

        for colonne in range(self.gridSizeX):
            self.can.create_line(colonne * self.caseX, 0, colonne * self.caseX, self.canvasSizeY, fill ='green')  
    
    def cercle(self,x, y, r, coul ='black'):
        '''
        tracé d'un cercle de centre (x,y) et de rayon r
        Fonction reprise sur http://python.developpez.com/cours/TutoSwinnen/?page=Chapitre8
        '''
        self.can.create_oval(x-r, y-r, x+r, y+r, outline='black', fill=coul)
        
        
    def place_bille(self,bille,indice) :
        self.cercle(bille.state.x*self.caseX + self.caseX/2, bille.state.y * self.caseY + self.caseY / 2,min(self.caseX,self.caseY)/2 ,coul=bille.color)
        self.can.create_text(bille.state.x*self.caseX + self.caseX/2,bille.state.y * self.caseY + self.caseY / 2,text=str(indice))