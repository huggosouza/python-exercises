from random import randint
from datetime import datetime
import json

if __name__ == '__main__':
    def main():
        condition = True
        while condition == True:
            print("------ Digite os dados ------\n")
            escola = str(input("Escola: "))
            nome = str(input("Nome: "))
            telefone = str(input("Telefone: "))
            funcao = str(input("Função: "))
            problema = str(input("Problema: "))
            protocolo = randint(10, 200)
            data_e_hora_atuais = datetime.now()
            data_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
            hora_em_texto = data_e_hora_atuais.strftime('%H:%M')
            
            dicionario = {f"Escola" : escola,
                          "Nome" : nome,
                          "Telefone" : telefone,
                          "Função" : funcao,
                          "Problema" : problema,
                          "Protocolo" : protocolo,
                          "Data" : data_em_texto,
                          "Hora" : hora_em_texto
                          }
            
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