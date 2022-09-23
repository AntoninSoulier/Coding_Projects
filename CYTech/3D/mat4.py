from vec4 import vec4

class mat4:

    def __init__(self,v1,v2,v3,v4):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.v4 = v4
        self.listeVec = [v1,v2,v3,v4]

    def print(self):
        print("|",self.v1.get_x()," ", self.v2.get_x()," ", self.v3.get_x()," ",self.v4.get_x(),"|")
        print("|",self.v1.get_y()," ", self.v2.get_y()," ", self.v3.get_y()," ",self.v4.get_y(),"|")
        print("|",self.v1.get_z()," ", self.v2.get_z()," ", self.v3.get_z()," ",self.v4.get_z(),"|")
        print("|",self.v1.get_w()," ", self.v2.get_w()," ", self.v3.get_w()," ",self.v4.get_w(),"|")

    def scalar_mul(self,k): 
        matrice = mat4(self.v1.multiplication(k), self.v2.multiplication(k), self.v3.multiplication(k), self.v4.multiplication(k))
        return matrice
            
    def mat_vec_mul(self,vecteur):
        res = vec4(
            self.v1.get_x() * vecteur.get_x() + self.v2.get_x() * vecteur.get_y() + self.v3.get_x() * vecteur.get_z() + self.v4.get_x() * vecteur.get_w(),
            self.v1.get_y() * vecteur.get_x() + self.v2.get_y() * vecteur.get_y() + self.v3.get_y() * vecteur.get_z() + self.v4.get_y() * vecteur.get_w(),
            self.v1.get_z() * vecteur.get_x() + self.v2.get_z() * vecteur.get_y() + self.v3.get_z() * vecteur.get_z() + self.v4.get_z() * vecteur.get_w(),
            self.v1.get_w() * vecteur.get_x() + self.v2.get_w() * vecteur.get_y() + self.v3.get_w() * vecteur.get_z() + self.v4.get_w() * vecteur.get_w()
        )
        return res
    
    def mat_mat_mul(self,matrice):
        m = mat4()
