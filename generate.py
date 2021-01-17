import random
import decimal
#from openpyxl import Workbook
import xlsxwriter
import itertools


rand_decimal = 0
converted_to_bin = 0
valor_real = 0
merito = 0
lista = []
lista_invertida = []
lista_binary = []
lista_realvalue = []
lista_merito = []
lista_roleta= []
lista_aleatorio= []
media_merito = 0



def conv_to_bin(decimal):
    valor_bin = bin(rand_decimal)[2:].zfill(8)
    for k in range(len(valor_bin)):
            if len(valor_bin)< 18:
                valor_bin = ''.join(('0',valor_bin))
    return valor_bin


def calc_valor_real(decimal):
    return 1 + decimal *(24/(pow(2,18)-1))
    

def func_avaliacao(value_real):
    return pow((value_real-15),2)

def generate_random(switch):#GERAR ALEATORIO
    if switch == 1:
        return random.randint(1,pow(2,18))
    elif switch == 2:
        j = 2
        while j <= 20:
            try:
                #print(j)
                lista[j].extend([round(random.uniform(0, 1),3)])#GERAR ALEATORIO ENTRE 0 e 1 E ARREDONDAR PARA 3 CASAS DECIMAIS
            except IndexError:
                break 
            j+=1

        
        
def calc_average():
    soma_atual = 0
    for j in range(len(lista)+1):
        try:
            soma_atual +=lista[j][3] 
        except IndexError:
            break
    print(soma_atual)
    for l in range(len(lista)+1):
        prob = 0
        try:
            prob = lista[l][3]/soma_atual
            lista[l].extend([prob])
        except IndexError:
            break 


def segmento_Roleta():
    roleta_value = 0
    for k in range(len(lista)+1):
        try:
            roleta_value += lista[k][4]
            lista[k].extend([round(roleta_value,3)])
        except IndexError:
            break 

def savetoexcel():
    workbook = xlsxwriter.Workbook('GA.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0

    lista_invertida = transpose(lista)
    print(lista_invertida)

    for col, data in enumerate(lista_invertida):
        worksheet.write_column(row, col, data)
    workbook.close()


def transpose(array):
    transposed_array = itertools.izip_longest(*array)

    return array




i = 1
while i<=20:
   rand_decimal = generate_random(1)
   converted_to_bin = conv_to_bin(rand_decimal)
   valor_real = calc_valor_real(rand_decimal)
   merito = func_avaliacao(valor_real)
  # print(rand_decimal," - ",converted_to_bin," - ",valor_real," - ",merito)
   lista.append([rand_decimal,converted_to_bin,valor_real,merito])
   i+=1


calc_average()
segmento_Roleta()
generate_random(2)


#print ('\n'.join([ str(myelement) for myelement in lista])) ##IMprimir elemento por linha


savetoexcel()



#print(lista)

k = input("Press key to exit")
