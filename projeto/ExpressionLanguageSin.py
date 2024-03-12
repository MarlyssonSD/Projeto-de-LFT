import ply.lex as lex
import ply.yacc as yacc


def p_program(p):
    ''' program : class '''
    pass


def p_class_extends(p):
    '''class : modifier visibility CLASS ID EXTENDS ID LCHAV membros RCHAV'''
    pass

def p_class_default(p):
    '''classe : modifier visibility CLASS ID LCHAV membros RCHAV'''
    pass

def p_class_implements(p):
    ''' class : modifier visibility CLASS ID IMPLEMENTS LCHAV membros RCHAV '''
    pass


def p_visibility_public(p):
    '''visibility : PUBLIC '''
    pass

def p_visibility_private(p):
    '''visibility : PRIVATE '''
    pass

def p_visibility_protected(p):
    '''visibility : PROTECTED '''
    pass

def p_visibility_default(p): #??vazio? default
    '''visibility :  '''
    pass


def p_modifier_static(p):
    '''modifier : static'''
    pass

def p_modifier_final(p):
    '''modifier : final'''
    pass




def main():
    f = open("projeto/Teste2.java", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=True)


if __name__ == "__main__":
    main()