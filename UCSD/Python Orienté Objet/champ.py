class Summoner:

    # Constructeur
    def __init__(self,pseudo,health,attack,weapon):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = weapon
        print("Bienvenue au joueur ", self.pseudo ," | health: ", self.health, " | attaque: ", self.attack)

    #Getters
    
    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health
    
    def get_attack(self):
        return self.attack

    def get_weapon(self):
        return self.weapon
    
    #Setters

    def set_weapon(self,weapon):
        self.weapon = weapon

    #Methode

    def damage(self, damage):
        self.health -= damage
        print("Aie...vous venez de subir ", damage, "degats")

    def attack_player(self, target_player):
        target_player.damage(self.get_attack())
    
