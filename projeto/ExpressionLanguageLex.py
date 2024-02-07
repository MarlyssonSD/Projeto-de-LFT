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
  'package' : 'PACKAGE',
  'import' : 'IMPORT',
  'transient' : 'TRANSIENT'
}
tokens = ['IGUAL', 'SOMA', 'VEZES', 'POT', 'LPAREN', 'RPAREN', 'COMMA', 'LCHAV', 'RCHAV', 'PV', 'PLUS', 'MINUS',
          'TIMES', 'DIVIDE', 'EQ', 'NEQ', 'LT', 'GT', 'LEQ', 'GEQ', 'AND', 'OR', 'NOT', 'BITWISE_AND', 'BITWISE_OR',
          'BITWISE_XOR', 'BITWISE_NOT', 'LSHIFT', 'RSHIFT', 'URSHIFT', 'PLUS_EQ', 'MINUS_EQ', 'TIMES_EQ', 'DIVIDE_EQ',
          'MOD_EQ', 'BITWISE_AND_EQ', 'BITWISE_OR_EQ', 'BITWISE_XOR_EQ', 'LSHIFT_EQ', 'RSHIFT_EQ', 'URSHIFT_EQ', 'ID', 'STRING'] + list(reservadas.values())

t_IGUAL= r'='
t_SOMA= r'\+'
t_VEZES= r'\*'
t_POT= r'\^'
t_LPAREN= r'\('
t_RPAREN= r'\)'
t_COMMA= r','
t_LCHAV= r'{'
t_RCHAV= r'}'
t_PV= r';'
t_PLUS= r'\+'
t_MINUS= r'-'
t_TIMES= r'\*'
t_DIVIDE= r'/'
t_EQ= r'=='
t_NEQ= r'!='
t_LT= r'<'
t_GT= r'>'
t_LEQ= r'<='
t_GEQ= r'>='
t_AND= r'&&'
t_OR= r'\|\|'
t_NOT= r'!'
# t_BITWISE_AND= r'&'
# t_BITWISE_OR= r'\|'
# t_BITWISE_XOR= r'^'
# t_BITWISE_NOT= r'~'
t_LSHIFT= r'<<'
t_RSHIFT= r'>>'
t_URSHIFT= r'>>>'
t_PLUS_EQ= r'\+='
t_MINUS_EQ= r'-='
t_TIMES_EQ= r'\*='
t_DIVIDE_EQ= r'/='
t_MOD_EQ= r'%='
t_BITWISE_AND_EQ= r'&='
t_BITWISE_OR_EQ= r'\|='
t_BITWISE_XOR_EQ= r'^='
t_LSHIFT_EQ= r'<<='
t_RSHIFT_EQ= r'>>='
t_URSHIFT_EQ= r'>>>='

def t_ID(t):
   r'[a-zA-Z_][a-zA-Z_0-9]*'
   t.type = reservadas.get(t.value,'ID')
   return t

#TRANSFORMAÇÃO ERRADA não é int(t.value)
def t_NUMBER_BIN(t):
   r'0b[01]+' #ou ... [0|1]
   t.value = int(t.value, base=2) #int() mesmo?
   return t

def t_NUMBER_OCTAL(t):
 r'0[0-7]+'
 t.value = int(t.value, base=8)
 return t

def t_NUMBER_HEXA(t):
   r'0(x|X)[a-fA-F0-9]+' #para que o underline?
   t.value = int(t.value, base=16)
   return t

def t_NUMBER_DOUBLE(t):
   r'\d+\.\d+d'
   t.value = double(t.value)
   return t

def t_NUMBER_FLOAT(t):
   r'\d+\.\d+f?'
   t.value = float(t.value)
   return t

def t_NUMBER_INT(t):
   r'\d+'
   t.value = int(t.value)
   return t

def t_CHAR(t):
  r"'(.|\n)?'"
  return t

def t_STRING(t):
  r'"(.|\n)*?"'
  return t

def t_comments_1(t):
  r'/\* [^ *\\]'
  t.lexer.lineno += len(t.value)
  

def t_comments_2(t):
   r'// [^ .*]' #ignorar tudo até encontrar quebra de linha
   t.lexer.lineno += len(t.value)


def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)
# /\* [^ *\\] comentário (add comentário de linha //)
t_ignore = ' \t'

def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)


def main():
   f = open("teste.j", "r")
   lexer = lex.lex(debug=1)
   lexer.input(f.read())
   print('\n\n# lexer output:')
   for tok in lexer:
      print ('type:', tok.type, ', value:',tok.value)


if __name__ == "__main__":
   main()
