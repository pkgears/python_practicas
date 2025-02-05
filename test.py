class Carro:

  def __init__(self, marca = ""):
    self._marca = marca

  def speed(self):
    return 100
  
  # def marca(self):
  #   return self.marca
  

carro = Carro(marca="Nissan")

print(carro._marca)
