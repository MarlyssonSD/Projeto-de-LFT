# GLC para o sintatico

```
programa → class

class → visibility classmodifier "class" ID extends ID {membros} |
          visibility classmodifier "class" ID {membros} |
          visibility classmodifier "class" ID implements ID {membros}
          

visibility → "PUBLIC"   |
             "PRIVATE"  |
             "PROTECTED"|
             ""               // "DEFAULT"= VAZIO

classmodifier →  "abstract"|
                   "final" |
                  ""          // "DEFAULT"= VAZIO

membros → membro |
          membro membros

membro → atribute |
          function

atribute → visibility atributemodifier ID |

atributemodifier →      "static"|
                        "final" |
                        ""          

function → signature  body 

signature  → visibility ID ID "(" sigparams ")"

sigparams → ID    |  
            ID "," sigparams

body  → "{" stms "}"

stms → stm  |  
       stm stms

stm → exp ";"                       |  //Restos dos comandos switch etc
      WHILE "(" exp ")" bodyorstm        |
      DO bodyorstm WHILE "("exp")" ";"       | // talvez faça
      FOR "(" exp ; exp ; exp ")" bodyorstm  |
      IF "(" exp ")" bodyorstm                 |
      IF "(" exp ")" bodyorstm ELSE bodyorstm |
      return exp ";"

bodyorstm → body  |
            stm

exp → operator|
      call |      
      FLOAT_NUMBER | 
      INT_NUMBER |  
      STRING |
      ID  

operator →  exp arithmetic exp|
            ID assign exp|
            exp operatorcomparator exp|
            unaryoperatorprefx ID|
            ID unaryoperatorsufx|
            exp operatorbittobit

arithmetic → "*"  |
             "/"  |
             "%"  |
             "+"  |
             "-"  

assign →    "=" exp|
            "+=" exp|
            "-=" exp|
            "*=" exp|
            "/=" exp|
            "%=" exp|
            "&=" exp|
            "|=" exp|
            "^=" exp|
            ">>>=" exp|
            ">>=" exp|
            "<<=" exp   

operatorcomparator →    ">="|
                        "<="|
                        ">"|
                        "<"|
                        "!="|
                        "=="|
                        "&&"|
                        "||"|
                        "&"|
                        "|"|
                        "^"  

unaryoperatorprefx →    "++"|
                        "--"|
                        "-"|
                        "+"|
                        "!"

unaryoperatorsufx →     "++"|
                        "--"


operatorbittobit →      ">>>"|
                        ">>"|
                        "<<"



call → ID "(" params ")" |
          ID "()"

params → exp "," params |
          exp


```