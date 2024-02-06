# -------------------------
# ExpressionLanguageLex.py
#----------------------
import ply.lex as lex
reservadas = {
  'public' : 'PUBLIC',
  'private' : 'PRIVATE',
  'protected' : 'PROTECTED',
  'static' : 'STATIC',
  'final' : 'FINAL',
  'abstract' : 'ABSTRACT',
  'for' : 'FOR',
  'while' : 'WHILE',
  'if' : 'IF',
  'else' : 'ELSE',
  'switch' : 'SWITCH',
  'try' : 'TRY',
  'catch' : 'CATCH',
  'finally' : 'FINALLY',
  'this' : 'THIS',
  'super' : 'SUPER',
  'throws' : 'THROWS',
  'return' : 'RETURN',
  'new' : 'NEW',
  'void' : 'VOID',
  'instanceof' : 'INSTANCEOF',
  'throw' : 'THROW',
  'break' : 'BREAK',
  'continue' : 'CONTINUE',
  'default' : 'DEFAULT',
  'final' : 'FINAL',
  'strictfp' : 'STRICTFP',
  'abstract' : 'ABSTRACT',
  'synchronized' : 'SYNCHRONIZED',
  'volatile' : 'VOLATILE',
  'assert' : 'ASSERT',
  'interface' : 'INTERFACE',
  'implements' : 'IMPLEMENTS',
  'package' : 'PACKAGE?',
  'import' : 'IMPORT',
  'transient' : 'TRANSIENT'
}
tokens = ['IGUAL', 'SOMA', 'VEZES', 'POT', 'LPAREN', 'RPAREN', 'COMMA', 'LCHAV', 'RCHAV', 'PV', 'PLUS', 'MINUS',
          'TIMES', 'DIVIDE', 'EQ', 'NEQ', 'LT', 'GT', 'LEQ', 'GEQ', 'AND', 'OR', 'NOT', 'BITWISE_AND', 'BITWISE_OR',
          'BITWISE_XOR', 'BITWISE_NOT', 'LSHIFT', 'RSHIFT', 'URSHIFT', 'PLUS_EQ', 'MINUS_EQ', 'TIMES_EQ', 'DIVIDE_EQ',+
          'MOD_EQ', 'BITWISE_AND_EQ', 'BITWISE_OR_EQ', 'BITWISE_XOR_EQ', 'LSHIFT_EQ', 'RSHIFT_EQ', 'URSHIFT_EQ'] + list(reservadas.values())

"T_IGUAL": r'=',
"T_SOMA": r'\+',
"T_VEZES": r'\*',
"T_POT": r'\^',
"T_LPAREN": r'\(',
"T_RPAREN": r'\)',
"T_COMMA": r',',
"T_LCHAV": r'{',
"T_RCHAV": r'}',
"T_PV": r';'
"T_PLUS": r'\+',
"T_MINUS": r'-',
"T_TIMES": r'\*',
"T_DIVIDE": r'/',
"T_EQ": r'==',
"T_NEQ": r'!=',
"T_LT": r'<',
"T_GT": r'>',
"T_LEQ": r'<=',
"T_GEQ": r'>=',
"T_AND": r'&&',
"T_OR": r'\|\|',
"T_NOT": r'!',
"T_BITWISE_AND": r'&',
"T_BITWISE_OR": r'\|',
"T_BITWISE_XOR": r'^',
"T_BITWISE_NOT": r'~',
"T_LSHIFT": r'<<',
"T_RSHIFT": r'>>',
"T_URSHIFT": r'>>>',
"T_PLUS_EQ": r'\+=',
"T_MINUS_EQ": r'-=',
"T_TIMES_EQ": r'\*=',
"T_DIVIDE_EQ": r'/=',
"T_MOD_EQ": r'%=',
"T_BITWISE_AND_EQ": r'&=',
"T_BITWISE_OR_EQ": r'\|=',
"T_BITWISE_XOR_EQ": r'^=',
"T_LSHIFT_EQ": r'<<=',
"T_RSHIFT_EQ": r'>>=',
"T_URSHIFT_EQ": r'>>>='

def t_ID(t):
   r'[a-zA-Z_][a-zA-Z_0-9]*'
   t.type = reservadas.get(t.value,'ID')
   return t


def t_NUMBER_BIN(t):
   r'0b[01]+' #ou ... [0|1]
   t.value = int(t.value) #int() mesmo?
   return t

def t_NUMBER_OCTAL(t):
 r'0[0-7]+'
 t.value = int(t.value)
 return t
    
def t_NUMBER_HEXA(t):
   r'0(x|X)[a-fA-F0-9]+' #para que o underline?
   t.value = int(t.value)
   return t
  
def t_NUMBER_DOUBLE(t):
   r'\d+\.\d+d'
   t.value = double(t.value)
   return t

def t_NUMBER_FLOAT(t):
   r'\d+\.\d+'
   t.value = float(t.value)
   return t
  
def t_NUMBER_INT(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_CHAR(t): #trabalhar melhor, sem considerar \n \t etc
  r"'.'"
  return t
  
def t_String(t):
  return t

def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)
t_ignore = ' \t'

def t_comments_1(t):
   r'/\* [^ *\\'
   t.lexer.lineno += len(t.value)
t_ignore = ' \t'

def t_comments_2(t):
   r'//// [^ \n' #ignorar tudo até encontrar quebra de linha
   t.lexer.lineno += len(t.value)
t_ignore = ' \t'

def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)


def main():
   f = open("teste.java", "r")
   lexer = lex.lex(debug=1)
   lexer.input(f.read())
   print('\n\n# lexer output:')
   for tok in lexer:
      print ('type:', tok.type, ', value:',tok.value)


if __name__ == "__main__":
   main()
