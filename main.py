# Grupo 1

# Discentes:
# Laysla Dayane Vieira Fernandes
# Mezack Kleberson de Sousa Alves
# Noany Gabriely de Oliveira

import json
import matplotlib.pyplot as plt
import funcoes as f

with open('Base de dados\diarias.json', 'r', encoding='UTF-8-sig') as file:
    base = json.load(file)


# 1 - Quais as quantidades de requisições por ano no período de 2010 a 2018?

def perg1(dados):
    anos = {}
 
    for linha in dados:
        ano = linha['ano_requisicao']
        if 2010 <= ano <= 2018:
            if ano in anos.keys():
                anos[ano] += 1
            else:
                anos[ano] = 1
 
    return f.org_data(anos)

# Gráfico 1 <linha>
resp1 = perg1(base)

x = resp1.keys()
y = resp1.values()

plt.figure(figsize=(10, 6))
plt.plot(x, y, '.-r')
plt.title('Viagens por ano', fontsize=18)
plt.ylabel('Quantidade de viagens', fontsize=12)
plt.xlabel('Anos', fontsize=12)
plt.grid()

plt.savefig('pergunta1.png')


# 2 - Quais os 10 proponentes com maior quantidade de requisições
# de todo o conjunto de registros?

def perg2(dados):
    proponentes = {}

    for linha in dados:
        proponente = linha['nome_proponente']
        proponente = f.citacaoAutor(proponente)

        if proponente in proponentes.keys():
            proponentes[proponente] += 1
        else:
            proponentes[proponente] = 1
    
    return f.ord_quant_value(proponentes, 10)

# Gráfico 2 <barra>
resp2 = perg2(base)

x = resp2.keys()
y = resp2.values()

y_cord = list(range(len(y)))

plt.figure(figsize=(12, 8))
plt.barh(y_cord , y, height=0.5, color= 'purple')
plt.title('Os dez proponentes com mais requisições', fontsize=20)
plt.ylabel('Nomes', fontsize=14)
plt.xlabel('Quantidade de requisições', fontsize=14)
plt.yticks(y_cord, x)

plt.savefig('pergunta2.png')


# 3 - Qual a quantidade de requisições nacionais e internacionais de 2010 a 2018?

def perg3(dados):
    tipos = {}
    internacional = {}
    nacional = {}

    for linha in dados:
        tipo = linha['internacional']
        ano = linha['ano_requisicao']
        if tipo == 'NÃO':
            if 2010 <= ano <= 2018:
                if ano in nacional.keys():
                    nacional[ano] += 1
                else:
                    nacional[ano] = 1
        elif tipo == 'SIM':
            if 2010 <= ano <= 2018:
                if ano in internacional.keys():
                    internacional[ano] += 1
                else:
                    internacional[ano] = 1

    internacional = f.org_data(internacional)
    nacional = f.org_data(nacional)

    tipos['Internacional'] = internacional
    tipos['Nacional'] = nacional

    return tipos

# Gráfico 3 <linha>
resp3 = perg3(base)

dados_internacionais = resp3['Internacional']
x1 = dados_internacionais.keys()
y1 = dados_internacionais.values()

dados_nacionais = resp3['Nacional']
x2 = dados_nacionais.keys()
y2 = dados_nacionais.values()

plt.figure(figsize=(10, 6))
plt.plot(x1, y1, linewidth=2, marker='o', color='Purple', label='Internacional')
plt.plot(x2, y2, linewidth=2,marker='o', color='tab:orange', label='Nacional')
plt.title('Requisições de viagens nacionais e internacionais', fontsize=18)
plt.xlabel('Anos', fontsize=12)
plt.ylabel('Quantidade de viagens', fontsize=12)
plt.legend(fontsize=12)
plt.grid()

plt.savefig('pergunta3.png')



# 4 - Quais as médias dos valores recebidos das requisições por ano entre 2010 a 2018?


def perg4(dados):
    media = {}
    valores = {}
    quant = perg1(dados)

    for linha in dados:
        ano = linha['ano_requisicao']
        valor = linha['valor_recebido']

        valor = f.org_valor(valor)
        
        if 2010 <= ano <= 2018:
            if ano in valores.keys():
                valores[ano] = round(valores[ano] + valor, 2)
            else:
                valores[ano] = valor

    for x in valores.keys():
        media[x] = valores[x] / quant [ano]

    return f.org_data(media)

# Gráfico 4 <barra>
resp4 = perg4(base)

x = resp4.keys()
y = resp4.values()

x_cord = list(range(len(x)))

plt.figure(figsize=(12, 8))
plt.bar(x_cord, y, width= 0.5, color= 'green')
plt.title('Valores médios recebidos por viagem', fontsize=20)
plt.ylabel('Valores(R$)', fontsize=14)
plt.xlabel('Anos', fontsize=14)
plt.xticks(x_cord, x)

for index, val in enumerate(y):
    txt = f'{val:.2f}'
    txt = txt.replace('.', ',')
    txt = txt
    
    if val > 1000:
        cord_x = index - 0.35
    else:
        cord_x = index - 0.3
    
    cord_y = round(val + 40)

    plt.text(x=cord_x, y=cord_y, s=txt, fontsize=12)

plt.savefig('pergunta4.png')


# 5 - Qual a porcentagem dos tipos de transportes utilizados nas viagens?

def perg5(dados):
    tipos = {}

    for linha in dados:
        transporte = linha['tipo_transporte']

        if transporte in tipos.keys():
            tipos[transporte] += 1
        else:
            tipos[transporte] = 1
    
    return tipos

# Gráfico 5 <pizza>
resp5 = perg5(base)

labels = resp5.keys()
sizes = resp5.values()
explode = (0, 0.05, 0, 0)

plt.figure(figsize=(10, 10))
plt.pie(sizes, labels=labels, explode=explode ,autopct='%.1f%%', colors=['Purple', 'tab:orange', 'violet', 'green'], shadow=True)
plt.title('Transportes utilizados para viagens', fontsize=18)
plt.legend(title='Transportes' ,labels=labels, loc='upper right')

plt.savefig('Pergunta5.png')