# Importando o FastApi
from fastapi import FastAPI

app = FastAPI()
teste = ('uma variavel de texto retonando em json')

# dicionário de dados para teste
dicDados = {
    'sede': {'rua': 'rua Ismael dias da Silva', 'numero': '113', 'cep': '12120015'},
    'end1': {'rua': 'rua Ismael ', 'numero': '11213', 'cep': '43343'},
    'end2': {'rua': 'rua dias da Silva', 'numero': '4343', 'cep': '4333'},
    'end3': {'rua': 'rua Silva', 'numero': '32', 'cep': '54545'},
}

# rotas


@app.get("/teste")
def hello_root():
    return {'messege': 'Hello World'}


@app.get("/novo")
def hello_root():
    return {'mensagem   ': f'teste: {teste}'}


@app.get('/enderecos')
def Numenderecos():
    return {'numeros de endereços': len(dicDados)}

# aqui agnt cria os dados que recebemos por parametro, na url será enviado para agnt /um numero que é de acordo com o id do nosso dado


@app.get('/enderecos/{id_endereco}')
def enderecos(id_endereco: str):
    if id_endereco in dicDados:
        return dicDados[id_endereco]
    else:
        return {'Id de Endereço errado'}
