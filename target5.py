string = input("Escreva uma frase: ")

lista_caracteres = list(string)

tamanho = len(lista_caracteres)
for i in range(tamanho // 2):
    temp = lista_caracteres[i]
    lista_caracteres[i] = lista_caracteres[tamanho - i - 1]
    lista_caracteres[tamanho - i - 1] = temp

string_invertida = ''.join(lista_caracteres)

print(string_invertida)