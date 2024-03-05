# -------------------------
# ExpressionLanguageLex.py
#----------------------
import ply.lex as lex

reservadas = {
  'abstract': 'ABSTRACT',
  'assert': 'ASSERT',
  'boolean': 'BOOLEAN',
  'break': 'BREAK',
  'byte': 'BYTE',
  'case': 'CASE',
  'catch': 'CATCH',
  'char': 'CHAR',
  'class': 'CLASS',
  'const': 'CONST',
  'continue': 'CONTINUE',
  'default': 'DEFAULT',
  'do': 'DO',
  'double': 'DOUBLE_NUMBER',
  'else': 'ELSE',
  'enum': 'ENUM',
  'extends': 'EXTENDS',
  'final': 'FINAL',
  'finally': 'FINALLY',
  'float': 'FLOAT_NUMBER',
  'for': 'FOR',
  'goto': 'GOTO',
  'if': 'IF',
  'implements': 'IMPLEMENTS',
  'import': 'IMPORT',
  'instanceof': 'INSTANCEOF',
  'int': 'INT_NUMBER',
  'interface': 'INTERFACE',
  'long': 'LONG',
  'native': 'NATIVE',
  'new': 'NEW',
  'package': 'PACKAGE',
  'private': 'PRIVATE',
  'protected': 'PROTECTED',
  'public': 'PUBLIC',
  'return': 'RETURN',
  'short': 'SHORT',
  'static': 'STATIC',
  'strictfp': 'STRICTFP',
  'super': 'SUPER',
  'switch': 'SWITCH',
  'synchronized': 'SYNCHRONIZED',
  'this': 'THIS',
  'throw': 'THROW',
  'throws': 'THROWS',
  'transient': 'TRANSIENT',
  'try': 'TRY',
  'void': 'VOID',
  'volatile': 'VOLATILE',
  'while': 'WHILE'
}



tokens = ['IGUAL', 'POT', 'LPAREN', 'RPAREN', 'COMMA', 'LCHAV', 'RCHAV', 'PV', 'PLUS', 'MINUS',
          'TIMES', 'DIVIDE', 'EQ', 'NEQ', 'LT', 'GT', 'LEQ', 'GEQ', 'AND', 'OR', 'NOT', 'BITWISE_AND', 'BITWISE_OR',
          'BITWISE_XOR', 'BITWISE_NOT', 'LSHIFT', 'RSHIFT', 'URSHIFT', 'PLUS_EQ', 'MINUS_EQ', 'TIMES_EQ', 'DIVIDE_EQ',
          'MOD_EQ', 'BITWISE_AND_EQ', 'BITWISE_OR_EQ', 'BITWISE_XOR_EQ', 'LSHIFT_EQ', 'RSHIFT_EQ', 'URSHIFT_EQ', 'ID',
          'STRING', 'RBRACKET', 'LBRACKET', 'DOT', 'HEXA_NUMBER', 'OCTAL_NUMBER', 'BIN_NUMBER', 'INCREMENT', 'DECREMENT'] + list(reservadas.values())


t_URSHIFT_EQ = r'>>>='
t_URSHIFT  = r'>>>'
t_LSHIFT_EQ  = r'<<='
t_RSHIFT_EQ  = r'>>='
t_LSHIFT  = r'<<'
t_RSHIFT = r'>>'
t_LEQ = r'<='
t_GEQ = r'>='
t_AND = r'&&'
t_OR = r'\|\|'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_PLUS_EQ = r'\+='
t_MINUS_EQ = r'-='
t_TIMES_EQ = r'\*='
t_DIVIDE_EQ = r'/='
t_MOD_EQ = r'%='
t_BITWISE_AND_EQ = r'&='
t_BITWISE_OR_EQ = r'\|='
t_BITWISE_XOR_EQ = r'^='
t_EQ = r'=='
t_NEQ = r'!='
t_IGUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_COMMA = r','
t_DOT = r'\.'
t_LCHAV = r'{'
t_RCHAV = r'}'
t_PV = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LT = r'<'
t_GT = r'>'
t_NOT = r'!'
t_BITWISE_AND = r'&'
t_BITWISE_OR = r'\|'
t_BITWISE_XOR = r'\^'
t_BITWISE_NOT = r'~'





def t_BIN_NUMBER(t):
   r'0b[01]+' #ou ... [0|1]
   t.value = int(t.value, base=2) #int() mesmo?
   return t

def t_OCTAL_NUMBER(t):
 r'0[0-7]+'
 t.value = int(t.value, base=8)
 return t

def t_HEXA_NUMBER(t):
   r'0(x|X)[a-fA-F0-9]+'
   t.value = int(t.value, base=16)
   return t

def t_FLOAT_NUMBER(t):
   r'\d+\.\d+(f|F)' #Problema com ex: 40.5f
   t.value = float(t.value)
   return t

def t_DOUBLE_NUMBER(t):
   r'\d+\.\d+'
   t.value = float(t.value) #float/double
   return t

def t_INT_NUMBER(t):
   r'[+-]?\d+'
   t.value = int(t.value)
   return t

def t_CHAR(t):
  r"'(.|\n)?'"
  return t

def t_STRING(t):
  r'"(.|\n)*?"'
  return t

def t_ID(t):
   r'[a-zA-Z_][a-zA-Z_0-9]*'
   t.type = reservadas.get(t.value,'ID')
   return t

def t_comments_1(t):
  r'/\* [^ *\\]'
  t.lexer.lineno += len(t.value)
  

def t_comments_2(t):
   r'// [^ .*]'
   t.lexer.lineno += len(t.value)


def t_newline(t):
   r'\n+'
   t.lexer.lineno += len(t.value)
t_ignore = ' \t'

def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)


def main():
   f = open("Teste1.java", "r")
   lexer = lex.lex(debug=1)
   lexer.input(f.read())
   print('\n\n# lexer output:')
   for tok in lexer:
      print ('type:', tok.type, ', value:',tok.value)


if __name__ == "__main__":
   main()
