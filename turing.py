class Turing():
    def __init__(self, position_lecture, bande, graphe):
        self.position_lecture = position_lecture
        self.bande = bande
        self.graphe = graphe
        self.etat = graphe["initial"]

    def step(self):
        # return 0 ou 1

        if self.graphe[self.etat] == None: # état final
            return False # il n'y a plus d'étapes
        
        transition = self.graphe[self.etat][self.bande[self.position_lecture]]

        if transition[1] != None: # écrire qqch si on le veut vraiment
            self.bande[self.position_lecture] = transition[1]
        
        if transition[2] == 'L':
            self.position_lecture -= 1
        elif transition[2] == 'R':
            self.position_lecture += 1

        self.etat = transition[0]

        return True # encore des étapes