from random import randint
import json

if __name__ == '__main__':
    def main():
        condition = True
        while condition == True:
            print("------ Digite os dados ------\n")
            escola = str(input("Escola: "))
            nome = str(input("Nome: "))
            cpf = str(input("CPF: "))
            matricula = str(input("Matrícula: "))
            email = str(input("E-mail: "))
            telefone = str(input("Telefone: "))
            funcao = str(input("Função: "))
            problema = str(input("Problema: "))
            protocolo = randint(10, 200)
            
            dicionario = {"Escola" : escola,
                          "Nome" : nome,
                          "CPF" : cpf,
                          "Matrícula" : matricula,
                          "E-mail" : email,
                          "Telefone" : telefone,
                          "Função" : funcao,
                          "Problema" : problema,
                          "Protocolo" : protocolo}
            
            saveData(dicionario=dicionario)
    
    def saveData(dicionario):
        with open("data.txt", 'a') as f: 
            for key, value in dicionario.items(): 
                f.write('%s: %s\n' % (key, value))
            f.write("\n")
            
        with open("data.json", 'a') as f: 
            json_object = json.dumps(dicionario, indent = 4, ensure_ascii=False)
            f.write(json_object)
            
    main()