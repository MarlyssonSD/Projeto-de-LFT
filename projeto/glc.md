# GLC para o sintatico

```
programa → class

class → visibility "class" ID extends ID {membros} |
          visibility "class" ID {membros} |
          visibility "class" ID implements ID {membros}

membros → membro |
          membro membros

membro → atribute |
          funcao

atribute → visibility ID

visibility → "PUBLIC" |
             "PRIVATE"|
             "PROTECTED"|
             "DEFAULT" |      //VAZIO


funcao → assinatura bloco

bloco → "{" instrucoes "}"

assinatura → visibility ID ID "(" sigparams ")" //rever modificadores java

sigparams → ID |  
           ID "," sigparams


instrucoes → instrucao  |  
       instrucoes instrucao ","

instrucao → exp ";"  |  
      WHILE "(" exp ")" bloco | return exp ";"
      FOR "(" exp ; exp ; exp ")"

exp → exp "+" exp |  
            exp "-" exp |  
            exp "*" exp |    
            exp "/" exp |  
            exp "^" exp |  
            exp "//" exp |   
            exp "%" exp |  
            exp ">" exp |  
            exp "<" exp |  
            exp "<=" exp |  
            exp ">=" exp |  
            exp "==" exp |  
            exp "+=" exp |  
            exp "-=" exp |  
            exp "/=" exp |  
            exp "*=" exp |  
            exp "&&" exp |  
            exp "||" exp |  
            exp "&" exp |  
            exp "|" exp |  
            chamada |   
            assign |   
            NUM |   
            ID  

chamada → ID "(" parametro ")" |
          ID "()"

parametro → exp "," parametro |
          exp

assign → ID "=" exp

NUM → <numero inteiro>

ID → <identificador>
```
