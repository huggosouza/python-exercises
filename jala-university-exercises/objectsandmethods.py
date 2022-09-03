class Robot:
    def __init__(self):
        # Criado o atributo color em Robot.
        self.color = 0

    # Criei a função para exibir os atributos
    def showAttributes(self):
        print(self.color)

robot1 = Robot()

# Objeto color alterado para "Red"
robot1.color = "Red"

# Utilizei o método
robot1.showAttributes()