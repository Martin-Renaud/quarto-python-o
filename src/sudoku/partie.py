from strategyn1 import StrategyN1
from strategyn2 import StrategyN2
from strategyn3 import StrategyN3
from strategyn4 import StrategyN4
import grillesrepository as gr
from grille import Grille


class Partie:

    def __init__(self):

        self.liste_strategies = list()
        self.liste_strategies.append(StrategyN1())
        self.liste_strategies.append(StrategyN2())
        self.liste_strategies.append(StrategyN3())
        self.liste_strategies.append(StrategyN4())

    def jouer(self):

        grille = gr.prepare_extreme1()

        print(grille)

        while not grille.est_pleine():

            progres = False
            for strategie in self.liste_strategies:
                if strategie.resolve(grille, True):
                    progres = True
                    break
            print('---------------------------\n')
            print(grille)
            if not progres:
                print("Incapable de déduire de l'information - le problème est trop difficile... pour l'instant.")
                grille.print_details()
                break


print("=======")
p = Partie()
p.jouer()
