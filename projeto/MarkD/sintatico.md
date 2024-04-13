# **Linguagem Java - Sintático**

## 1. Elementos Sintáticos

Um programa em Java possui uma ou mais funções, podendo conter uma ou mais classes. É semelhante a c++. Abaixo está uma das regras que define funções:

programa → class

class → visibility classmodifier "class" ID extends ID {membros} |
          visibility classmodifier "class" ID {membros} |
          visibility classmodifier "class" ID implements ID {membros}
          
No Java nós podemos definir uma visibilidade e modificadores para as classes por exemplo.

## 1.1 Comandos do Java

Assim como todas as linguagens, Java possui diversos comandos de expressões, condicionais, repetições, tratamento de exceções e etc. Abaixo está uma das regras:

stm → exp ";"                       |  //Restos dos comandos switch etc
      WHILE "(" exp ")" bodyorstm        |
      DO bodyorstm WHILE "("exp")" ";"       | // talvez faça
      FOR "(" exp ; exp ; exp ")" bodyorstm  |
      IF "(" exp ")" bodyorstm                 |
      IF "(" exp ")" bodyorstm ELSE bodyorstm |
      return exp ";"

No java podemos usar os mais diversos tipos de comandos, incluindo entre eles, repetições, condicionais e os retornos.

## 1.2 Expressões em Java

Em Java temos suporte para as mais diversas expressões aritméticas, soma, subtração, divisão, multiplicação etc. É possível também ter chamadas de funções com atribuições ou não e de forma geral, as expressões podem ser números ou variáveis. As regras de expressões é:

exp → exp "+" exp | 
      exp "*" exp | 
      exp "^" exp | 
      call | 
      assign | 
      NUM | 
      ID
```

As expressões são diversas e vão muito além dessas, mas um exemplo é a soma que pode ter uma expressão + expressão * expressão .... etc
É necessário aceitar todos os tipos de cálculos, desde que seja possível no java.


## 1.2.1 Funções e atribuições

Na linguagem Java também é possível ter chamadas de funções com e sem parâmetros e os parâmetros podem ser qualquer expressão Java. A regra se resume em:

function → signature body 

atribute → visibility atributemodifier ID |

atributemodifier →      "static"|
                        "final" |
                        ""          


A função se resume as suas assinaturas e após isso, o corpo, quer seria o {}
Além disso podemos adicionar modificadores nas atribuições.


# 2. Exemplos de códigos

public class Teste2 {
    public static void main(String args) {
        // Definindo os valores individuais
        final int valor1 = 1;
        int valor2 = 2;
        int valor3 = 3;
        int valor4 = 4;
        int valor5 = 5;
        String minhaFrase;
        boolean meudouble = false;
        float MeuFLOAT;
        // int[] teste = new int[20];

        if (false) {
            return;
        }
        valor2++;
        while (valor3 < 10) {
            valor2++;
        }
        int novo;
        for (novo = 2; novo < 4; novo++){
            novo++;
        }



        // Calculando a soma dos valores
        int soma = valor1 + valor2 + valor3 + valor4 + valor5;
        System.out.println(soma);
        // Exibindo o resultado da soma
        //System.out.println("A soma dos valores é: " + soma);
    }
}

