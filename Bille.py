class Bille(object):
    """
    docstring for Bille

    Une bille possède une couleur 

    """
    def __init__(self, color, indice, state, env,trace=False):
        super(Bille, self).__init__()
        self.color = color
        self.indice = indice
        self.state = state
        self.env = env
        self.trace = trace

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
        if self.trace :
            print("Colision de la bille "+str(self.indice)+" avec la bille "+str(bille.indice)+" en ("+str(bille.state.x)+","+str(bille.state.y)+")")
        self.state.bougera = False
        bille.state.bougera = False
        direction_tmp = self.state.direction
        self.state.direction = bille.state.direction
        bille.state.direction = direction_tmp 


    def nextPos(self) :
        '''
        Une direction est un couple d'int qui est sauvegardé dans l'objet State.
        '''
        (futurX,futurY) = (self.state.x + self.state.direction[0],self.state.y + self.state.direction[1])
        if self.env.torique :
            if futurY == -1 :
                futurY = len(self.env.grille)-1
            if futurY == len(self.env.grille) :
                futurY = 0
            if futurX == -1 :
                futurX = len(self.env.grille[0]) -1
            if futurX == len(self.env.grille[0]) :
                futurX = 0
        else :
            list_direction = list(self.state.direction)
            if futurX == -1 :
                futurX = 1
                list_direction[0] = - list_direction[0]
            if futurX == len(self.env.grille[0]) :
                futurX = len(self.env.grille[0]) - 2
                list_direction[0] = - list_direction[0]
            if futurY == -1 :
                futurY = 1  
                list_direction[1] = - list_direction[1]
            if futurY == len(self.env.grille) :
                futurY = len(self.env.grille) - 2
                list_direction[1] = - list_direction[1]
            self.state.direction = tuple(list_direction)

        return (futurX,futurY)
        
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
            self.collision(self.env.grille[futurY][futurX])
        self.update(futurX,futurY)

