class Turing:
    def __init__(self, position_lecture, bande, graphe, alphabet):
        self.position_lecture = position_lecture

        # la bande est une liste de **strings**
        # (donc il faut bien mettre des chaînes pour les clés des dictionaires enfants, et quand on écrit dessus)
        self.bande = list(bande)

        self.graphe = graphe
        self.etat = graphe.get("initial", 0)  # au cas où il n'est pas présent
        self.alphabet = alphabet

    def __repr__(self):
        return f"{self.bande}\n{' ' * (self.position_lecture - 1)}^"

    def etape(self):
        if self.graphe[self.etat] == None:  # état final
            return False  # il n'y a plus d'étapes

        transition = self.graphe[self.etat][self.bande[self.position_lecture]]

        if transition[1] != None:  # écrire qqch si on le veut vraiment
            if transition in self.alphabet["blank"] + self.alphabet["other"]:
                self.bande[self.position_lecture] = transition[1]
            else:
                raise RuntimeError(f"Caractère n'appartenant pas à l'alphabet: {transition[1]} (possibles: {self.alphabet['blank'] + self.alphabet['other']})")

        if transition[2] == 'L':
            self.position_lecture -= 1

            if self.position_lecture < 0:
                self.bande = [self.alphabet["blank"] for _ in range(16)] + self.bande
                self.position_lecture += 16

        elif transition[2] == 'R':
            self.position_lecture += 1

            # augmenter la taille du ruban si besoin
            if self.position_lecture == len(self.bande):
                self.bande += [self.alphabet["blank"] for _ in range(16)]
        
        else:
            raise RuntimeError(f"Déplacement inconnu: {transition[2]} (possibles: L, R)")

        self.etat = transition[0]
        
        if self.etat not in self.graphe:
            raise RuntimeError(f"L'état demandé {self.etat} n'est pas dans le graphe (possibles: {', '.join(k for k in self.graphe.keys())})")

        return True  # encore des étapes
