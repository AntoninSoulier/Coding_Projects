class vec4:

    #Constructeur
    def __init__(self,x,y,z,w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_z(self):
        return self.z

    def get_w(self):
        return self.w

    def multiplication(self, k):
        return(k*self.x, k*self.y, k*self.z, k*self.w)

    def hom2cart(self):
        return(self.x/self.w, self.y/self.w, self.z/self.w)
    
    def print(self):
        print("[",self.x,",",self.y,",",self.z,",",self.w,"]")