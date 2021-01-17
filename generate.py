import random



rand_decimal = 0
converted_to_bin = 0
valor_real = 0
merito = 0

def conv_to_bin(decimal):
    valor_bin = bin(rand_decimal)[2:].zfill(8)
    for k in range(len(valor_bin)):
            if len(valor_bin)< 18:
                valor_bin = ''.join(('0',valor_bin))
    return valor_bin


def calc_valor_real(decimal):
    return 1 + decimal *(24/(pow(2,18)-1))
    

def func_avaliacao(value_real):
    merito = pow((value_real-15),2)

def generate_random():
    return random.randint(1,pow(2,18))






        
        
        

i = 0

while i<=20:
   rand_decimal = generate_random()
   converted_to_bin = conv_to_bin(rand_decimal)

   i+=1

k = input("Press key to exit")
