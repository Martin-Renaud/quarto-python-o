

class Carre:

    def __init__(self, no_case):
        self.no_case = no_case
        self.valeur = None
        self.valeurs_possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.liste_de_carre_contraints = list()

    def est_decouvert(self):
        return self.valeur is None and len(self.valeurs_possible) == 1

    def est_vide(self):
        return self.valeur is None

    def est_definit(self):
        return self.valeur is not None

    def assigne_carre_contraints(self, liste_de_carre_contraints):
        self.liste_de_carre_contraints.extend(liste_de_carre_contraints)

    def enleve_possibilite(self, valeur):
        assert valeur is not None
        #if self.no_case == 68:
        #    print(f'Valeur interdite sur case {self.no_case} : {valeur}')

        if valeur in self.valeurs_possible:
            self.valeurs_possible.remove(valeur)

    def initialize_valeur(self, valeur):
        assert self.valeur is None
        #assert len(self.valeurs_possible) == 9

        self.set_valeur_interne(valeur)

    def assigne_valeur(self, valeur):
        assert self.valeur is None
        #assert len(self.valeurs_possible) == 1
        assert valeur in self.valeurs_possible

        self.set_valeur_interne(valeur)

    def set_valeur_interne(self, valeur):
        self.valeur = valeur
        self.valeurs_possible = [valeur]
        for carre in self.liste_de_carre_contraints:
            carre.enleve_possibilite(valeur)

    def __str__(self):
        return f'#{self.no_case}-{self.valeur}'