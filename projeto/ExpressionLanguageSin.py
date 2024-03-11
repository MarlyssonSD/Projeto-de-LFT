import ply.lex as lex
import ply.yacc as yacc


def p_program(p):
    ''' programa : classe '''
    pass

def p_class1(p):
    '''classe : visibility CLASS ID EXTENDS ID LCHAV membros RCHAV'''
    pass

def p_class2(p):
    '''classe : visibility CLASS ID LCHAV membros RCHAV'''
    pass

def p_class3(p):
    ''' class : visibility CLASS ID IMPLEMENTS LCHAV membros RCHAV '''
    pass




def main():
    f = open("projeto/Teste2.java", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=True)


if __name__ == "__main__":
    main()