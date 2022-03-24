import requests
import os

os.system('clear')#Limpando o terminal

cep = input("Digite o CEP: ")
r = requests.get("viacep.com.br/ws/{}/json/".format(cep))

os.system('clear')

data = r.json()

print('CEP: {}'.format(data['cep']))
print('Bairro: {}'.format(data['bairro']))
print('Cidade: {}-{}'.format(data['localidade','uf']))
      