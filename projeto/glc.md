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

atribute → visibility  ID |

atributemodifier →   "abstract" |
                        "final" |
                        "default"          

funcao → signature  body 

body  → "{" stms "}"

signature  → visibility ID ID "(" sigparams ")"

sigparams → ID    |  
            ID "," sigparams


stms → stm  |  
       stm stms

stm → exp ";"                       |  
      WHILE "(" exp ")" body        |
      DO body WHILE "("exp")"       |
      FOR "(" exp ; exp ; exp ")"   |
      IF "(" exp ")"
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