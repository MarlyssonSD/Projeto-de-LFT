
programa → funcao | 
          funcao programa

funcao → assinatura bloco

assinatura → TYPE ID "(" sigparams ")"

sigparams → ID |  
           ID "," sigparams

bloco → "{" instrucoes "}"

instrucoes → instrucao  |  
       instrucoes instrucao ","

instrucao → expressao ";"  |  
      WHILE "(" expressao ")" bloco | return expressao ";"

expressao → expressao "+" expressao |  
            expressao "-" expressao |  
            expressao "*" expressao |    
            expressao "/" expressao |  
            expressao "^" expressao |  
            expressao "//" expressao |   
            expressao "%" expressao |  
            expressao ">" expressao |  
            expressao "<" expressao |  
            expressao "<=" expressao |  
            expressao ">=" expressao |  
            expressao "==" expressao |  
            expressao "+=" expressao |  
            expressao "-=" expressao |  
            expressao "/=" expressao |  
            expressao "*=" expressao |  
            expressao "&&" expressao |  
            expressao "||" expressao |  
            expressao "&" expressao |  
            expressao "|" expressao |  
            chamada |   
            assign |   
            NUM |   
            ID  

chamada → ID "(" parametro ")" | 
       ID "()"

parametro → expressao "," parametro | 
         expressao

assign → ID "=" expressao

NUM → <numero inteiro>

ID → <identificador>
