#Case du plateau de jeu
class Case:
    
    #constructeur
    def __init__(self,status):
        self.status = status

    #getter
    def get_status(self):
        return self.status

    #setter
    def set_status(self, status):
        self.status = status
        