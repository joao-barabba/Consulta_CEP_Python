import requests
import os

os.system('clear')#Limpando o terminal

cep = input("Digite o CEP: ")
r = requests.get(f"viacep.com.br/ws/{cep}/json/")

data = r.json()

print(f"CEP:{data['logradouro']}")