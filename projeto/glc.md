# GLC para o sintatico

```
programa → class

class → visibility modifier "class" ID extends ID {membros} |
          visibility modifier "class" ID {membros} |
          visibility modifier "class" ID implements ID {membros}
          

visibility → "PUBLIC"   |
             "PRIVATE"  |
             "PROTECTED"|
             ""               // "DEFAULT"= VAZIO

modifier →  "static"|
            "final" |
            ""                // "DEFAULT"= VAZIO

membros → membro |
          membro membros

membro → atribute |
          funcao

atribute → visibility atributemodifier ID |

atributemodifier →   "abstract" |
                        "final" |
                        ""          

funcao → signature  body 

body  → "{" stms "}"

stms → stm  |  
       stm stms

bodyorstm → body  |
            stm

signature  → visibility ID ID "(" sigparams ")"

sigparams → ID    |  
            ID "," sigparams


stm → exp ";"                       |  //Restos dos comandos switch etc
      WHILE "(" exp ")" bodyorstm        |
      DO bodyorstm WHILE "("exp")"       | // talvez faça
      FOR "(" exp ; exp ; exp ")" bodyorstm  |
      IF "(" exp ")" bodyorstm                 |
      IF "(" exp ")" bodyorstm ELSE bodyorstm |
      return exp ";"

exp → exp ">>>=" exp |
      exp ">>>" exp |
      exp "<<=" exp |
      exp ">>=" exp |
      exp "<<" exp |
      exp ">>" exp |
      exp "<=" exp |
      exp ">=" exp |
      exp "&&" exp |
      exp "\|\|" exp |
      exp "\+\+" exp |
      exp "--" exp | 
      exp "\+=" exp | 
      exp "-=" exp | 
      exp "\*=" exp | 
      exp "%=" exp | 
      exp "&=" exp | 
      exp "\|=" exp | 
      exp "^=" exp | 
      exp "==" exp | 
      exp "!=" exp | 
      exp "=" exp | 
      exp "\(" exp | 
      exp "\)" exp | 
      exp "\[" exp | 
      exp "\]" exp | 
      exp "," exp | 
      exp "\." exp | 
      exp "{" exp | 
      exp "}" exp | 
      exp ";" exp | 
      exp "\+" exp | 
      exp "-" exp | 
      exp "\*" exp | 
      exp "/" exp | 
      exp "<" exp | 
      exp ">" exp | 
      exp "!" exp | 
      exp "&" exp | 
      exp "\|" exp | 
      exp "\^" exp | 
      exp "~" exp |  
      call |   
      assign |   
      FLOAT_NUMBER | 
      INT_NUMBER |  
      STRING |
      ID  

call → ID "(" parametro ")" |
          ID "()"

parametro → exp "," parametro |
          exp

assign → ID "=" exp

```