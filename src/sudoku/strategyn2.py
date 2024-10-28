from abstractstrategy import AbstractStrategy


class StrategyN2(AbstractStrategy):

    def get_name(self):
        return "Stratégie N2"

    def _get_deduction(self, grille):
        res = {}
        valeurs_possible = range(1, 10)
        for groupe in self.groupes_de_no_cases:
            # valeur -> liste des carré du groupe pouvant avoir cette
            # TODO: initialisation pas requise?
            map_possibi = {key: [] for key in valeurs_possible}
            for no_case in groupe:
                c = grille.map_de_carre[no_case]
                if c.est_vide():
                    for i in c.valeurs_possible:
                        map_possibi[i].append(c)

            dict_filtre = {k: v for k, v in map_possibi.items() if len(v) == 1}
            dict_inverse = {v[0]: k for k, v in dict_filtre.items()}
            #elements_filtrees = [liste_liee_deduite[0] for liste_liee_deduite in map_possibi.values() if len(liste_liee_deduite) == 1]
            res.update(dict_inverse)
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
