import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

diferente_zero = []
for dado in dados:
    if dado['valor'] != 0.0:
        diferente_zero.append(dado)

menor_valor = min(diferente_zero, key=lambda x: x['valor'])

print(menor_valor['valor'])