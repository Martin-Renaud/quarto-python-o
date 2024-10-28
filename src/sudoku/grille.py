from carre import Carre
from constraintbuilder import ConstraintBuilder
import numpy as np

"""
  1  2  3    4  5  6    7  8  9
 10 11 12   13 14 15   16 17 18
 19 20 21   22 23 24   25 26 27
  
 28 29 30   31 32 33   34 35 36 
 37 38 39   40 41 42   43 44 45
 46 47 48   49 50 51   52 53 54
 
 55 56 57   58 59 60   61 62 63
 64 65 66   67 68 69   70 71 72
 73 74 75   76 77 78   79 80 81
"""


class Grille:

    def __init__(self):

        map_cases_contraintes = ConstraintBuilder().contraintes
        self.map_de_carre = {}
        self.nb_carre_decouvert = 0
        for no_case in range(1, 82):
            c = Carre(no_case)
            self.map_de_carre[no_case] = c

        for no_case in range(1, 82):
            no_cases_contraintes = map_cases_contraintes[no_case]
            liste_de_carre_contraints = list()
            for no_case_contrainte in no_cases_contraintes:
                liste_de_carre_contraints.append(self.map_de_carre[no_case_contrainte])
            self.map_de_carre[no_case].assigne_carre_contraints(liste_de_carre_contraints)

    def __str__(self):

        carres = list(self.map_de_carre.values())
        liste = [v.valeur for v in carres]
        tableau = np.reshape(liste, (9, 9))

        res = ""
        for index_l, l in enumerate(tableau, start=1):
            for index_c, carre_val in enumerate(l, start=1):
                if carre_val is None:
                    res = res + "."
                else:
                    res = res + str(carre_val)
                if index_c in (3, 6):
                    res = res + " | "
                else:
                    res = res + " "
            res = res + "\n"
            if index_l in (3, 6):
                res = res + "---------------------\n"
        return res

    def print_details(self):
        print('No Case - [valeurs possible]')
        for no_case, carre in self.map_de_carre.items():
            if not carre.est_definit():
                print(f"{no_case} - {carre.valeurs_possible}")


    def assigne_case_depart(self, no_case, valeur):
        assert no_case >= 1
        assert no_case <= 81
        assert valeur in range(1, 10)
        self.nb_carre_decouvert = self.nb_carre_decouvert + 1
        self.map_de_carre[no_case].initialize_valeur(valeur)

    def assigne_case(self, no_case, valeur):
        assert no_case >= 1
        assert no_case <= 81
        assert valeur in range(1, 10)
        self.nb_carre_decouvert = self.nb_carre_decouvert + 1
        self.map_de_carre[no_case].assigne_valeur(valeur)

    def est_pleine(self):
        return self.nb_carre_decouvert == 81
