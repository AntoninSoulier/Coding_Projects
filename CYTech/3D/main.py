from vec3 import vec3
from vec4 import vec4
from mat4 import mat4

v = vec3(3,4,5)
w = vec3(2,1,0)

s = vec4(4,2,5,1)
b = vec4(3,2,5,0)
c = vec4(1,9,1,1)
m = vec4(0,0,5,1)

matrice = mat4(s,b,c,m)
matrice.print()
print(" ")
s.print()

print(" ")

tmp = matrice.mat_vec_mul(s)
tmp.print()