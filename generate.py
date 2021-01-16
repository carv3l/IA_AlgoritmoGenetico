import random



rand_decimal = 0
converted_to_bin = 0
valor_real = 0



def valor_real(decimal):
    valor_real = 1 + decimal *(24/(pow(2,18)-1))
    print(valor_real)





for i in range(21): #Itera ate 20
    rand_decimal = random.randint(1,pow(2,18))
    print(rand_decimal)
    converted_to_bin = bin(rand_decimal)[2:].zfill(8)
    for k in range(len(converted_to_bin)):
        if len(converted_to_bin)< 18:
            converted_to_bin = ''.join(('0',converted_to_bin))
    print(converted_to_bin)
    valor_real(rand_decimal)

k = input("Press key to exit")
