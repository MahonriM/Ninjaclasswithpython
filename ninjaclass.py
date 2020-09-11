#Made by Mahonri M
#Visit my website:https://mahonrim.github.io/
class ninjas():
    id=0
    nombre=""
    rango=""
    sexo='M'
class situacion(ninjas):
    def __init__(self,nombre,status):
        self.nombre=nombre
        self.status=status
        print("El ninja llamado {0} esta {1}".format(nombre,status))
naruto=ninjas()
naruto.id=1
naruto.nombre="Naruto"
naruto.rango="Kage"
naruto.sexo="M"
situacion(naruto.nombre,"casado")
print("El nombre del ninja es {0} y su rango es {1}".format(naruto.nombre,naruto.rango))
