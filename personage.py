import random
from equipements import BarbareEquipement, HealerEquipement, AnalysteEquipement

class Joueur:
    def __init__(self, nom, classe, equipement, difficulte):
        self.nom = nom
        self.classe = classe
        self.equipement = equipement
        self.difficulte = difficulte
        self.points_de_vie = 100 + difficulte.points_de_vie
        self.points_dattaque = 10 + self.equipement.points_attaque + difficulte.points_dattaque
        self.points_de_defense = 5 + self.equipement.points_defense + difficulte.points_de_defense
        self.chance_de_crit = 10 + difficulte.chance_de_crit

    def afficher_stats(self):
        print("Nom: ", self.nom)
        print("Classe: ", self.classe)
        print("Points de vie: ", self.points_de_vie)
        print("Points d'attaque: ", self.points_dattaque)
        print("Points de défense: ", self.points_de_defense)
        print("Chance de critique:", self.chance_de_crit)
        print("Arme: ", self.equipement.nom)
        print("Difficulté: ", self.difficulte.nom)

    def choisir_direction(self):
        print("Choisissez une direction :")
        print("1. Nord")
        print("2. Est")
        print("3. Sud")
        print("4. Ouest")
        choix_direction = input("Entrez le numéro de la direction : ")
        return choix_direction

    def entrer_salle(self, salle):
        from salle import SallePieges, SalleTresor, SalleCombat  # Importation spécifique ici pour éviter les problèmes de circularité
        print("\nVous entrez dans la salle :", salle.nom)
        print(salle.description)

        if isinstance(salle, SallePieges):
            print("Vous évitez de justesse les pièges mortels !")
        elif isinstance(salle, SalleTresor):
            print("Vous trouvez un coffre rempli de richesses !")
        elif isinstance(salle, SalleCombat):
            print("Un ennemi redoutable vous attaque !")

        print("")

class Barbare(Joueur):
    def __init__(self, nom, difficulte):
        from salle import SallePieges, SalleTresor, SalleCombat  # Importation spécifique ici pour éviter les problèmes de circularité
        equipement = BarbareEquipement()
        super().__init__(nom, "Barbare", equipement, difficulte)
        self.points_dattaque += 10
        self.points_de_defense += 5

    def choisir_direction(self):
        print("Choisissez une direction :")
        print("1. Nord")
        print("2. Est")
        print("3. Sud")
        print("4. Ouest")
        choix_direction = input("Entrez le numéro de la direction : ")
        return choix_direction

class Healer(Joueur):
    def __init__(self, nom, difficulte):
        from salle import SallePieges, SalleTresor, SalleCombat  # Importation spécifique ici pour éviter les problèmes de circularité
        equipement = HealerEquipement()
        super().__init__(nom, "Healer", equipement, difficulte)
        self.points_de_vie -= 20
        self.points_dattaque += 5

    def choisir_direction(self):
        print("Choisissez une direction :")
        print("1. Nord")
        print("2. Est")
        print("3. Sud")
        print("4. Ouest")
        choix_direction = input("Entrez le numéro de la direction : ")
        return choix_direction

class Analyste(Joueur):
    def __init__(self, nom, difficulte):
        from salle import SallePieges, SalleTresor, SalleCombat  # Importation spécifique ici pour éviter les problèmes de circularité
        equipement = AnalysteEquipement()
        super().__init__(nom, "Analyste", equipement, difficulte)
        self.points_de_vie -= 10
        self.points_dattaque += 7
        self.chance_de_crit += 25

    def choisir_direction(self):
        print("Choisissez une direction :")
        print("1. Nord")
        print("2. Est")
        print("3. Sud")
        print("4. Ouest")
        choix_direction = input("Entrez le numéro de la direction : ")
        return choix_direction
