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
            self.env.grille[self.state.y][self.state.x] = None
            self.env.grille[futurY][futurX] = self
            self.state.x = futurX
            self.state.y = futurY
    
    def collision(self,bille) :
        '''
        En cas de collision avec une autre bille les deux
        s'échangent leur direction. 
        '''
        self.state.bougera = False
        bille.state.bougera = False
        direction_tmp = self.state.direction
        self.state.direction = bille.state.direction
        self.bille.direction = direction_tmp 

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
        if self.env.grille[futurY][futurX] == None :
            #signifie donc que la voie est libre !
            self.state.bougera = True
        else :
            #du coup occupé
            self.state.bougera = False
            self.collision()
        self.update(futurX,futurY)

