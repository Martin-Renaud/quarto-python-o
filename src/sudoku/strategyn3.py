from abstractstrategy import AbstractStrategy

"""

Pattern:
Lorsque dans un groupe, il y a une sous-groupe de N cases avec N possibilités identiques, 
les cases du sous-groupe vont forcément se partager ces valeurs.

Ca permet de retirer les valeurs possibles de ce sous-groupes aux autres cases.
"""

class StrategyN3(AbstractStrategy):

    def get_name(self):
        return "Stratégie N3"


    def _get_deduction(self, grille):

        # carre -> liste des valeurs qu'il ne peut contenir
        res = dict()
        groupes = self.get_groupes_de_carre(grille)
        for g in groupes:
            # Valeurs possibles -> liste des carrés avec ces valeurs
            vals_to_carre = dict()
            for c in g:
                key = ','.join(map(str, c.valeurs_possible))
                if key not in vals_to_carre:
                    vals_to_carre[key] = list()
                vals_to_carre[key].append(c)
            for (k, v) in vals_to_carre.items():
                key = list(map(int, k.split(',')))
                if len(key) == len(v):
                    for c in g:
                        if c not in v:
                            res[c] = key
        return res

    def _print_deduction(self, deduction):
        if len(deduction) == 0:
            print('Pas de déduction trouvée.')
            return

        for carre, valeurs in deduction.items():
            print(f'Case {carre.no_case} ne peut pas prendre ces valeurs:  {valeurs}')

    def _apply_deduction(self, grille, deduction):

        for carre, valeurs in deduction.items():
            for v in valeurs:
                carre.enleve_possibilite(v)
