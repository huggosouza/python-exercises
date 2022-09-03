class Janela:
    def __init__(self):
        self.largura = 0
        self.altura = 0
        self.transparente = False
        self.marca = ""
    
    def exibirAtributos(self):
        print(f"Largura: {self.largura}\nAltura: {self.altura}\nTransparente: {self.transparente}\nMarca: {self.marca}")

    
janela_quarto = Janela()

janela_quarto.largura = 25
janela_quarto.altura = 50
janela_quarto.transparente = False
janela_quarto.marca = "Sanvid"

janela_quarto.exibirAtributos()