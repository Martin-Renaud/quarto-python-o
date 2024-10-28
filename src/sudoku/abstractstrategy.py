from abc import ABC, abstractmethod
import numpy as np

class AbstractStrategy(ABC):

    def __init__(self):
        tableau = np.arange(1, 82).reshape(9, 9)

        self.groupes_de_no_cases = list()
        self.groupes_de_no_cases.append(tableau[0:3, 0:3].flatten().tolist())
        self.groupes_de_no_cases.append(tableau[0:3, 3:6].flatten().tolist())
        self.groupes_de_no_cases.append(tableau[0:3, 6:9].flatten().tolist())
        self.groupes_de_no_cases.append(tableau[3:6, 0:3].flatten().tolist())
        self.groupes_de_no_cases.append(tableau[3:6, 3:6].flatten().tolist())
        self.groupes_de_no_cases.append(tableau[3:6, 6:9].flatten().tolist())
        self.groupes_de_no_cases.append(tableau[6:9, 0:3].flatten().tolist())
        self.groupes_de_no_cases.append(tableau[6:9, 3:6].flatten().tolist())
        self.groupes_de_no_cases.append(tableau[6:9, 6:9].flatten().tolist())
        for i in range(0, 9):
            self.groupes_de_no_cases.append(tableau[i, :])
            self.groupes_de_no_cases.append(tableau[:, i])

    def get_groupes_de_carre(self, grille, inclure_trouves=False):
        res = list()
        for groupe in self.groupes_de_no_cases:
            ce_groupe = list()
            for no_case in groupe:
                c = grille.map_de_carre[no_case]
                if c.est_vide() or inclure_trouves:
                    ce_groupe.append(c)
            if len(ce_groupe) > 0:
                res.append(ce_groupe)

        assert len(res) > 0
        return res

    @abstractmethod
    def get_name(self):
        pass

    def resolve(self, grille, verbose = False):

        deduction = self._get_deduction(grille)
        if verbose:
            print(self.get_name() + " :")
            self._print_deduction(deduction)
        self._apply_deduction(grille, deduction)
        return len(deduction) > 0


    @abstractmethod
    def _get_deduction(self, grille):
        pass

    @abstractmethod
    def _print_deduction(self, deduction):
        pass

    @abstractmethod
    def _apply_deduction(self, grille, deduction):
        pass


