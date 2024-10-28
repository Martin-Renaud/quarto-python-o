from abstractstrategy import AbstractStrategy


class StrategyN1(AbstractStrategy):

    def get_name(self):
        return "Stratégie N1"

    def _get_deduction(self, grille):
        res = {}
        for no_case, carre in grille.map_de_carre.items():
            if carre.est_decouvert():
                res[carre] = carre.valeurs_possible[0]
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
