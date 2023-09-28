import numpy as np
import Libreria_Espacios_Vedctoriales_Complejos_1 as lib
 
def norm(ket):
    norma = round(np.linalg.norm(ket) ** 2, 3)
    return norma
 
def prob(ket, posicion):
    pos = ket[posicion]
    return round(np.abs(pos) ** 2 / norm(ket), 3)

def probt(ket, ket2):
    producto_interno = np.abs(np.dot(ket2.conj(), ket)) ** 2
    return producto_interno
