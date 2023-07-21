class Potion:
    def __init__(self, nom,type_potion,valeur):
        self.nom = nom
        self.type_potion=type_potion
        self.valeur = valeur 

    def utiliser(self, joueur,bonus_type):
        match bonus_type:
            case "bonus_attaque":
                joueur.points_dattaque += self.random_bonus
            case "bonus_vie":
                joueur.points_de_vie += self.random_bonus
            case "bonus_defense":
                joueur.points_de_defense += self.random_bonus
            case "bonus_chance_critique":
                joueur.chance_de_crit += self.random_bonus

    def __str__(self):
        return f"Nom : {self.nom}, type: {self.type_potion}, valeur: {self.valeur}"