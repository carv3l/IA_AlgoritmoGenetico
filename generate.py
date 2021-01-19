import random
import decimal
#from openpyxl import Workbook
import xlsxwriter
import itertools
import numpy as np


rand_decimal = 0
converted_to_bin = 0
valor_real = 0
merito = 0
lista = []
lista_invertida = []
lista_avaliacao =  []
lista_roleta = []
lista_aleatorio = []
posicao_roleta= []
media_merito = 0
sT_maxvalue =0
nD_maxvalue = 0



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
        lista[0].extend([0])
        lista[1].extend([0])
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

def savetoexcel():## PARSAR PARA EXCEL
    workbook = xlsxwriter.Workbook('GA.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0

    lista_invertida = transpose(lista)
   # print(lista_invertida)
    for col, data in enumerate(lista_invertida):
        worksheet.write_column(row, col, data)
    workbook.close()


def transpose(array):
    return list(itertools.zip_longest(*array))

def get_2_highest():
     for k in range(len(lista)+1):
        try:
            lista_avaliacao.append(lista[k][3])
        except IndexError:
            break

     lista_avaliacao.sort()
     
     for j in range(len(lista)+1):
            try:
                if(lista_avaliacao[-1] == lista[j][3]):
                    posicao_roleta.append(j)
            except IndexError:
                break

     for j in range(len(lista)+1):
            try:
                if(lista_avaliacao[-2] == lista[j][3] ):
                    posicao_roleta.append(j)
            except IndexError:
                break     


     print(lista_avaliacao[-1])
     print(lista_avaliacao[-2])

def position_bin_to_list(array):

     for j in range(len(lista)+1):
            try:
                bin_value = lista[array[j]][1]
                lista[j].extend([bin_value])
            except IndexError:
                break     

def locate_in_interval(): #LOCALIZAR O ELEMENTO ALEATORIO DENTRO DO SEGMENTO DA ROLETA
    print("POSI",posicao_roleta)
    k = 2
    while k <= 20:
        try:
            lista_aleatorio.append(lista[k][6])
        except IndexError:
            break 
        k+=1

    for j in range(len(lista)+1):
            try:
                lista_roleta.append(lista[j][5])
            except IndexError:
                break

    for aleatorio in enumerate(lista_aleatorio):
        for i in range(len(lista_roleta)+1):
            try:
                if(aleatorio[1]<=lista_roleta[i]):
                    print("ALEATORIO:",aleatorio[1],">=",lista_roleta[i])
                    print(" ---")
                    posicao_roleta.append(i)
                    break          
            except IndexError:
                break
    print("Pos",posicao_roleta)
    print("R",lista_roleta)
    print("ALE",lista_aleatorio)

    position_bin_to_list(posicao_roleta)





def replace_str_index(text,index=0,size=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+size:])


def recombinacao(ptcorte):
    firstbin = 0
    secondbin = 0

    firsthalf = 0
    secondhalf = 0


    j = 2
    lista[0].extend([lista[0][7]])
    lista[1].extend([lista[1][7]])
    while j <= (len(lista)):
        try:
            firstbin = lista[j][7]
            secondbin = lista[j+1][7]

            firsthalf = firstbin[0:int(ptcorte)]
            secondhalf = secondbin[0:int(ptcorte)]

            print("firsthalf", firsthalf,"secondhalf",secondhalf)

            lista[j].extend([replace_str_index(secondbin,0,int(ptcorte),firsthalf)])
            lista[j+1].extend([replace_str_index(firstbin,0,int(ptcorte),secondhalf)])
            j+=2
        except IndexError:
                break     
          






    
#If you have a range xmin < x < xmax then this should work (taking x=filename[:,0] and y=filename[:,1]) :

  #   idx = np.where(y==np.max(y[(x>xmin)&(x<xmax)]))[0][0]
  

i = 1
while i<=20:
   rand_decimal = generate_random(1)
   converted_to_bin = conv_to_bin(rand_decimal)
   valor_real = calc_valor_real(rand_decimal)
   merito = func_avaliacao(valor_real)
#   print(rand_decimal," - ",converted_to_bin," - ",valor_real," - ",merito)
   lista.append([rand_decimal,converted_to_bin,valor_real,merito])
   i+=1


calc_average()
segmento_Roleta()
generate_random(2)
get_2_highest()
locate_in_interval()




pontosCorte = input("INTRODUZA PONTOS DE CORTE:")



recombinacao(pontosCorte)



print ('\n'.join([ str(myelement) for myelement in lista])) ##IMprimir elemento por linha
#savetoexcel()




k = input("Press key to exit")
