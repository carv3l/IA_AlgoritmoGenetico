import random
import decimal
#from openpyxl import Workbook
import xlsxwriter
import itertools
import numpy as np
import os


numero_geracoes = 0
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
tamanho_população = 0
val_prob_recombinacao = 0
tamanho_individuo_mutacao = 0

col_decimal = 0
col_binario = 1
col_valoreal = 2
col_avaliacao = 3
col_prob_select = 4
col_seg_roleta = 5
col_aleatorio_roleta = 6
col_cromossoma_selected = 8
col_recomb_prob = 9
col_pontoCorte = 10
col_recombinacao = 11
col_mutacao = 12
#col_




saveiter = 0
workbook = xlsxwriter.Workbook('GA.xlsx')

def closeExcelIfOpen():
    fo = open(r'GA.xlsx')
    print("Name of the file: ", fo.name)
    os.close(fo.fileno())



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
        while j <= tamanho_população:
            try:
                #print(j)
                lista[j].extend([round(random.uniform(0, 1),3)])#GERAR ALEATORIO ENTRE 0 e 1 E ARREDONDAR PARA 3 CASAS DECIMAIS
            except IndexError:
                break 
            j+=1
    elif switch == 3:
        lista[0].extend([0])
        lista[1].extend([0])
        j = 2
        while j <= tamanho_população:
            try:
                randval = round(random.uniform(0, 1),2)
                lista[j].extend([randval])#GERAR ALEATORIO ENTRE 0 e 1 E ARREDONDAR PARA 3 CASAS DECIMAIS
                lista[j+1].extend([randval])#GERAR ALEATORIO ENTRE 0 e 1 E ARREDONDAR PARA 3 CASAS DECIMAIS
            except IndexError:
                break 
            j+=2
    elif switch == 4:
        return random.randint(0,tamanho_população-1)
    elif switch == 5:
        return random.randint(0,17)
        
def calc_average():
    soma_atual = 0
    for j in range(len(lista)+1):
        try:
            soma_atual +=lista[j][col_avaliacao] 
        except IndexError:
            break
    
   # print(round(soma_atual,4))
    print("Média: ",round(soma_atual/(len(lista)),4))

    for l in range(len(lista)+1):
        prob = 0
        try:
            prob = lista[l][col_avaliacao]/soma_atual
            lista[l].extend([prob])
        except IndexError:
            break 


def segmento_Roleta():
    roleta_value = 0
    for k in range(len(lista)+1):
        try:
            roleta_value += lista[k][col_prob_select]
            lista[k].extend([round(roleta_value,3)])
        except IndexError:
            break 

def savetoexcel(iteration):## PARSAR PARA EXCEL    
    worksheet = workbook.add_worksheet('GER '+str(iteration))
    worksheet.write(0, 0, 'Decimal')          # Write em excel na primeira linha primeira coluna
    worksheet.write(0, 1, 'Binário')          
    worksheet.write(0, 2, 'Valor Real')         
    worksheet.write(0, 3, 'Função Avaliação')         
    worksheet.write(0, 4, 'Probabilidade de ser Selecionada')         
    worksheet.write(0, 5, 'Segmento da Roleta')         
    worksheet.write(0, 6, 'Aleatório Roleta')   
    worksheet.write(0, 7, 'Pai Selecionado')       
    worksheet.write(0, 8, 'Cromossoma em BIN') 
    worksheet.write(0, 9, 'Probabilidade de Recombinação')
    worksheet.write(0, 10, 'Ponto de Corte Aleatório') 
    worksheet.write(0, 11, 'Recombinação')
    worksheet.write(0, 12, 'Mutação')       

    lista_invertida = transpose(lista)
    row = 1 
    # print(lista_invertida)
    for col, data in enumerate(lista_invertida):
        worksheet.set_column(col,col,len(data))
        worksheet.write_column(row, col, data)
    print("Salvo em excel como GER",str(iteration))


def transpose(array):
    return list(itertools.zip_longest(*array))

def get_2_highest():
     for k in range(len(lista)+1):
        try:
            lista_avaliacao.append(lista[k][col_avaliacao])
        except IndexError:
            break
        
     lista_avaliacao.sort()
     
     print("Melhor Individuo: ",round(lista_avaliacao[-1],4))
     
     for j in range(len(lista)+1):
            try:
                if(lista_avaliacao[-1] == lista[j][col_avaliacao]):
                    posicao_roleta.append(j)
            except IndexError:
                break

     for j in range(len(lista)+1):
            try:
                if(lista_avaliacao[-2] == lista[j][col_avaliacao] ):
                    posicao_roleta.append(j)
            except IndexError:
                break     
     print("LISTA AVALIACAO",lista_avaliacao) 
     lista_avaliacao.clear()
   ##  print(lista_avaliacao[-1]) VALOR MAIS ALTO
   ##  print(lista_avaliacao[-2]) 2 VALOR MAIS ALTO
     

def position_bin_to_list(array):


    for i in range(len(lista)+1):
            try:
                lista[i].extend(["i"+str(array[i]+2)]) #PERMITE VER A POSICAO DO PAI NO EXCEL COMO NO EXCEL COMECA EM 0 SOMA 1 PARA ALINHAR,
                                                       # E COMO COMECA A ESCREVER NA LINHA 1, SOMA MAIS OUTRO 1 ficando 2
            except IndexError:
                break
    #view_output()

    for j in range(len(lista)+1):
        try:
            bin_value = lista[array[j]][col_binario]
            lista[j].extend([bin_value])
        except IndexError:
                break
    
    posicao_roleta.clear()
    lista_roleta.clear()
    lista_aleatorio.clear()
     

def locate_in_interval(): #LOCALIZAR O ELEMENTO ALEATORIO DENTRO DO SEGMENTO DA ROLETA
    
    k = 2
    while k <= tamanho_população:
        try:
            lista_aleatorio.append(lista[k][col_aleatorio_roleta])
        except IndexError:
            break 
        k+=1

    for j in range(len(lista)+1):
            try:
                lista_roleta.append(lista[j][col_seg_roleta])
            except IndexError:
                break

    for aleatorio in enumerate(lista_aleatorio):
        for i in range(len(lista_roleta)+1):
            try:
                if(aleatorio[1]<=lista_roleta[i]):
                ##    print("ALEATORIO:",aleatorio[1],">=",lista_roleta[i])
                ##    print(" ---")
                    posicao_roleta.append(i)
                    break          
            except IndexError:
                break
   # print("Pos",posicao_roleta)
   # print("R",lista_roleta)
   # print("ALE",lista_aleatorio)

    position_bin_to_list(posicao_roleta)
    


def replace_str_index(text,index=0,size=0,replacement=''):
    return '%s%s%s'%(text[:index],replacement,text[index+size:])


def recombinacao(ptcorte,firstbin,secondbin):
    firsthalf = 0
    secondhalf = 0

    firsthalf = firstbin[0:int(ptcorte)]
    secondhalf = secondbin[0:int(ptcorte)]

    child_1 = replace_str_index(secondbin,0,int(ptcorte),firsthalf)
    child_2 = replace_str_index(firstbin,0,int(ptcorte),secondhalf)

    return child_1, child_2

def probabilidade_recombinacao(prob):
   # view_output()
    firstbin = 0
    secondbin = 0
    lista[0].extend([lista[0][col_cromossoma_selected]])
    lista[1].extend([lista[1][col_cromossoma_selected]])
    j = 2
    while j <= (len(lista)):
        try:
            
            if(lista[j][col_recomb_prob] <= float(prob) and lista[j+1][col_recomb_prob] <= float(prob)):
                firstbin = lista[j][col_cromossoma_selected]
                secondbin = lista[j+1][col_cromossoma_selected]
                print("PONTO:",lista[j][col_pontoCorte])
                child1 , child2 =  recombinacao(lista[j][col_pontoCorte],firstbin,secondbin)
                
                lista[j].extend([child1])
                lista[j+1].extend([child2])
            elif(lista[j][col_recomb_prob] > float(prob) and lista[j+1][col_recomb_prob] > float(prob)):
                lista[j].extend([lista[j][col_cromossoma_selected]])
                lista[j+1].extend([lista[j+1][col_cromossoma_selected]])
        except IndexError:
            break
        j+=2



def generate_pontosCorte():
    i = 0
    while i <= len(lista):
        try:
            corte = generate_random(5)
            lista[i].extend([corte])
            lista[i+1].extend([corte])
        except IndexError:
            break
        i +=2
   



def mutacao():
    j = 0
    while j <= (len(lista)-1):
        try:
           lista[j].extend([lista[j][col_recombinacao]])
        except IndexError:
            break
        j+=1

    to_mutate = 0
    gene_pos = 0
    after_mutate = 0
    val = 0
    selector_number = round(0.005 * tamanho_população * 18)
   ## print(selector_number)
    i = 1
    while i <= selector_number:
        
        val = generate_random(4)

      ##  print("VAl",val)
        to_mutate = lista[val][col_mutacao]

        #tamanho_individuo_mutacao = len(to_mutate)-1

        gene_pos = generate_random(5)

        if(to_mutate[gene_pos] == '0'):
            after_mutate = replace_str_index(to_mutate,gene_pos,1,'1')
        else:
            after_mutate = replace_str_index(to_mutate,gene_pos,1,'0')

      ##  print(to_mutate)  
      ##  print(gene_pos)
      ##  print(to_mutate[gene_pos])
      ##  print(after_mutate)
        lista[val][col_recombinacao] = after_mutate

        i+=1


def reset_and_set():
    lista_mutacao = []
    lista_decimais = []
    for j in range(len(lista)+1):
            try:
                lista_mutacao.append(lista[j][col_mutacao])
            except IndexError:
                break

    lista.clear()
    for i in range(len(lista_mutacao)+1):
            try:
                lista_decimais.append(int(lista_mutacao[i],2))
               # lista.insert(1,lista_mutacao[i])
            except IndexError:
                break
                
   # print(lista_mutacao)
   # print(lista_decimais)

    i = 0
    while i <= len(lista_mutacao)-1:
        valor_real = calc_valor_real(lista_decimais[i])
        merito = func_avaliacao(valor_real)
        lista.append([lista_decimais[i],lista_mutacao[i],valor_real,merito])
        i+=1


def view_output():
    print ('\n'.join([ str(myelement) for myelement in lista])) ##Imprimir elemento por linha

def clear():    #Function to clear console after exit input
    os.system('cls' if os.name=='nt' else 'clear')


 ################### INICIO DO CÓDIGO #####################################         

##closeExcelIfOpen()

while True:
    state = input("PARSAR PARA EXCEL?  (1  = sim , 0 = não) : ")
    if(int(state) == 0 or int(state) == 1):
        break

numero_geracoes = input("INTRODUZA O NUMERO DE GERACOES:")

while True:
    tamanho_população = int(input("Tamanho da População (Número Inteiro par ) :"))
    if( (tamanho_população % 2) == 0):
        break

val_prob_recombinacao = input("INTRODUZA A PROBABILIDADE DE RECOMBINAÇÃO:")

state_view = input("PRETENDE VER A LISTA ? (1  = sim , 0 = não):")

i = 1
while i<=tamanho_população:
   rand_decimal = generate_random(1)
   converted_to_bin = conv_to_bin(rand_decimal)
   valor_real = calc_valor_real(rand_decimal)
   merito = func_avaliacao(valor_real)
#   print(rand_decimal," - ",converted_to_bin," - ",valor_real," - ",merito)
   lista.append([rand_decimal,converted_to_bin,valor_real,merito])
   i+=1

j = 1
while j <= int(numero_geracoes):
    calc_average()
    segmento_Roleta()
    generate_random(2)
    get_2_highest()
    locate_in_interval()
    generate_random(3) ##Aleatorio Roleta
    generate_pontosCorte()
    probabilidade_recombinacao(val_prob_recombinacao)
    mutacao()
    if int(state) == 1:
        savetoexcel(j)
    if int(state_view) == 1:
        view_output()
    reset_and_set()
    j+=1
workbook.close()


k = input("Press key to exit") 
clear()