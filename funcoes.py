def org_data(dic):
    anos = {}
 
    for key in sorted(dic.keys()):
        anos[key] = dic[key]

    return anos


def ord_quant_value(dic, quant):
    key = []
    valores = []
    resultado = {}

    for value in sorted(dic, key = dic.get, reverse=True):
        key.append(value)    
        valores.append(dic[value])
    for x in range(quant):
        resultado[key[x]] = valores[x]
            
    return resultado


def org_valor(valor):
    final = ''
    for c in valor:
        if 48 <= ord(c) <= 57 or ord(c) == 44:
            final += c

    return float(final.replace(',', '.'))


def citacaoAutor(texto):
    texto = texto.split()
    primeiro_nome = texto[0]
    ultimo_nome = texto[-1][0]

    texto = f'{primeiro_nome} {ultimo_nome}.'
    return texto