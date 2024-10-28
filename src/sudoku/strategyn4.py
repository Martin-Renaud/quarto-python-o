from abstractstrategy import AbstractStrategy

"""

Pattern:
Il est impossible de déduire quelque chose de la grille v(assumant que N1 et N3 ont passer sans rien trouver)

Donc cette "stratégie" consiste a trouver la case avec le moins de possibilité et en choisir une au hasard.

Si c'est un mauvaus choix, il va y avoir une erreur d'assertion.

"""

class StrategyN4(AbstractStrategy):

    def get_name(self):
        return "Stratégie N4"


    def _get_deduction(self, grille):

        # carre -> liste des valeurs qu'il ne peut contenir
        res = dict()
        groupes = self.get_groupes_de_carre(grille)
        groupes_tries = sorted(groupes, key=len)
        moins_risque = groupes_tries[0]
        premier_carre = moins_risque[0]
        res[premier_carre] = premier_carre.valeurs_possible[0]
        return res

    def _print_deduction(self, deduction):
        if len(deduction) == 0:
            print('Pas de déduction trouvée.')
            return

        for carre, valeur in deduction.items():
            print(f'Case {carre.no_case} est {valeur}')

    def _apply_deduction(self, grille, deduction):

        for carre, valeur in deduction.items():
            grille.assigne_case(carre.no_case, valeur)
