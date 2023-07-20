class Monstre:
    def __init__(self, nom,classe,points_de_vie,points_dattaque,points_de_defense,chance_de_crit):
        
        self.nom = nom
        self.classe = classe #trach mob ou boss
        self.points_de_vie = points_de_vie
        self.points_dattaque = points_dattaque
        self.points_de_defense = points_de_defense
        self.chance_de_crit = chance_de_crit
    def __str__(self):
        return f"Nom : {self.nom}, Classe : {self.classe}, Points de vie : {self.points_de_vie}, Points d'attaque : {self.points_dattaque}, Points de défense : {self.points_de_defense}, Chance de coup critique : {self.chance_de_crit}"


class Potion:
    def __init__(self, nom,valeur):
        self.nom = nom
        self.valeur = valeur 
