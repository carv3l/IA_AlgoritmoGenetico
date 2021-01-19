# Exercicio Prático Obrigatório 2 (Algoritmo Genético) em código Python

Isto permite agilizar a criação do Algoritmo Genético

## Requisitos

Python 3.9 ou 3.7

``` $ pip install xlsxwriter ```

## Usage

Apenas correr o programa

### Inputs no script


#### Tamanho da População:

 ``` $ Tamanho da População (Número Inteiro par ) : ```

 Aqui introduzir no número inteiro o tamanho da população a gerar
 Ter em atenção que só pode ser introduzido números pares
 

#### Numero do ponto de Corte:

 ``` $ INTRODUZA NUMERO DO PONTO DE CORTE: ```

 Aqui introduzir no número inteiro onde cortar no numero Binário
 Ter em atenção que só pode ir até 17


#### Se quer guardar a geração numa SpreadSheet:

 ``` $ PARSAR PARA EXCEL?  (1  = sim , 0 = não) :  ```

 Aqui na própria linha de comandos aparece as opções

 Se o utilizador escolher o valor 1:
 É gerado um ficheiro ``` GA.xlsx ```


### Examples

Se o valor aleatorio for inferior à probabilidade de recombinação, faz-se a recombinação com o ponto de corte
Se o valor aleatorio for superior à probabilidade de recombinação, os filhos ficam iguais aos progenitores, ou seja não se faz a recombinação

A probabilidade de mutação tem que ter em conta 3 coisas:
-Tamanho da População
-Probabilidade de Mutação 
-Numero de Bits

probabilidadeMutação * tamanhoPopulação * NumeroBits = Numero de Individuos a serem mutados aleatóriamente

EXEMPLO
0,005 * 20 * 18 = 1,8 = 2




## Notas

O código ainda não está perfeito, mas o rough está presente
Após aprovação do Professor Responsável,irá se proceder à iteração por uma versão melhor

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.