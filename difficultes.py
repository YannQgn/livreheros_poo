class Difficulte:
    def __init__(self, nom):
        self.nom = nom
        self.points_de_vie = 0
        self.points_dattaque = 0
        self.points_de_defense = 0
        self.chance_de_crit = 0


class DifficulteInconnue(Difficulte):
    def __init__(self):
        super().__init__("Inconnu")
        self.points_de_vie = 0
        self.points_dattaque = 0
        self.points_de_defense = 0
        self.chance_de_crit = 0


class Facile(Difficulte):
    def __init__(self):
        super().__init__("Facile")
        self.points_de_vie = 50
        self.points_dattaque = 5
        self.points_de_defense = 5
        self.chance_de_crit = 5


class Moyen(Difficulte):
    def __init__(self):
        super().__init__("Moyen")
        self.points_de_vie = 0
        self.points_dattaque = 0
        self.points_de_defense = 0
        self.chance_de_crit = 0


class Difficile(Difficulte):
    def __init__(self):
        super().__init__("Difficile")
        self.points_de_vie = -50
        self.points_dattaque = -5
        self.points_de_defense = -5
        self.chance_de_crit = -5


class Hardcore(Difficulte):
    def __init__(self):
        super().__init__("Hardcore")
        self.points_de_vie = -100
        self.points_dattaque = -10
        self.points_de_defense = -10
        self.chance_de_crit = -10
