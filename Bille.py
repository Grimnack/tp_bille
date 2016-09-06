class Bille(object):
    """
    docstring for Bille

    Une bille possède une couleur 

    """
    def __init__(self, color, indice, state, env):
        super(Bille, self).__init__()
        self.color = color
        self.indice = indice
        self.state = state
        self.env = env

    def update(self,futurX,futurY):
        if self.state.bougera :
            self.env.grille[self.state.x][self.state.y] = None
            self.env.grille[futurX][futurY] = self
            self.state.x = futurX
            self.state.y = futurY

    def demiTour(self) :
        """
        C'est pas beau à voir mais c'est ça
        """
        if self.state.direction == 'N' :
            self.state.direction = 'S'
        elif self.state.direction == 'S':
            self.state.direction = 'N'
        elif self.state.direction == 'O':
            self.state.direction = 'E'
        elif self.state.direction == 'E':
            self.state.direction = 'O'
        elif self.state.direction == 'NO':
            self.state.direction = 'SE'
        elif self.state.direction == 'NE':
            self.state.direction = 'SO'
        elif self.state.direction == 'SO':
            self.state.direction = 'NE'
        elif self.state.direction == 'SE':
            self.state.direction = 'NO'

    def nextPos(self) :
        """
        Donne les coordonnées de la future case souhaitée 
        """
        if self.state.direction == None :
            return (self.state.x,self.state.y)    
        elif self.state.direction == 'N' :
            return (self.state.x , self.state.y - 1) 
        elif self.state.direction == 'S':
            return (self.state.x , self.state.y + 1)
        elif self.state.direction == 'O':
            return (self.state.x - 1 , self.state.y)
        elif self.state.direction == 'E':
            return (self.state.x + 1 , self.state.y)
        elif self.state.direction == 'NO':
            return (self.state.x - 1 , self.state.y - 1)
        elif self.state.direction == 'NE':
            return (self.state.x + 1 , self.state.y - 1)
        elif self.state.direction == 'SO':
            return (self.state.x - 1 , self.state.y + 1)
        elif self.state.direction == 'SE':
            return (self.state.x + 1 , self.state.y + 1)
        
    def decide(self) :
        """
        Deux cas de figure, la bille perçoit où elle doit aller :
            soit c'est libre : elle garde sa direction et avancera à l'update
            soit c'est occupé : elle inverse sa direction et n'avancera pas à l'update
        """
        futurX,futurY = self.nextPos()
        if self.env.grille[futurX][futurY] == None :
            #signifie donc que la voie est libre !
            self.state.bougera = True
        else :
            #du coup occupé
            self.state.bougera = False
            self.demiTour()
        self.update(futurX,futurY)

