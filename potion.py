class Potion:
    def __init__(self, nom, type_potion, valeur):
        self.nom = nom
        self.type_potion = type_potion
        self.valeur = valeur

    def utiliser(self, joueur):
        match self.type_potion:
            case "bonus_attaque":
                joueur.points_dattaque += self.valeur
                print(f"Vous avez utilisé la potion et obtenu un bonus d'attaque de {self.valeur} !")
            case "bonus_vie":
                joueur.points_de_vie += self.valeur
                print(f"Vous avez utilisé la potion et obtenu un bonus de vie de {self.valeur} !")
            case "bonus_defense":
                joueur.points_de_defense += self.valeur
                print(f"Vous avez utilisé la potion et obtenu un bonus de défense de {self.valeur} !")
            case "bonus_chance_critique":
                joueur.chance_de_crit += self.valeur
                print(f"Vous avez utilisé la potion et obtenu un bonus de chance critique de {self.valeur} !")
            case "Ptdr T mort !":
                joueur.points_de_vie -= 200
                print(f"Souvenez vous de Indian a Jones , vous perdez {self.valeur} point de vie!")    

    def __str__(self):
        return f"Nom : {self.nom}, type: {self.type_potion}, valeur: {self.valeur}"
