program → funcdecl | 
          funcdecl program

funcdecl → signature block

signature → TYPE ID "(" sigparams ")"

sigparams → ID | 
            ID "," sigparams

block → "{" stms "}"

stms → stm  | 
       stms stm

stm → exp ";"  | 
      WHILE "(" exp ")" block | return exp ";"

call → ID "(" params ")"

exp → exp "+" exp | 
      exp "*" exp | 
      exp "^" exp | 
      call | 
      assign | 
      NUM | 
      ID

call → ID "(" params ")" | 
       ID "()"

params → exp "," params | 
         exp

assign → ID "=" exp
