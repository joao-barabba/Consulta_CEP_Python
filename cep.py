import requests


cep = input("Digite o CEP: ")
r = requests.get("http://viacep.com.br/ws/{}/json/".format(cep))

data= r.json()

print('CEP: {}'.format(data['cep']))
print('Bairro: {}'.format(data['bairro']))
print('Cidade: {}'.format(data['localidade']))
print('Cidade: {}'.format(data['uf']))

exit()
