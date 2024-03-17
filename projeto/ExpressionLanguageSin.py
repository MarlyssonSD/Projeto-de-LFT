from ExpressionLanguageLex import *
import ply.yacc as yacc


def p_program(p):
    ''' program : class '''
    pass


def p_class_extends(p):
    '''class : visibility classmodifier CLASS ID EXTENDS ID LCHAV membros RCHAV'''
    pass

def p_class_default(p):
    '''class : visibility classmodifier CLASS ID LCHAV membros RCHAV'''
    pass

def p_class_implements(p):
    ''' class : visibility classmodifier CLASS ID IMPLEMENTS LCHAV membros RCHAV '''
    pass

    #VISIBILIDADE
def p_visibility_public(p):
    '''visibility : PUBLIC '''
    pass

def p_visibility_private(p):
    '''visibility : PRIVATE '''
    pass

def p_visibility_protected(p):
    '''visibility : PROTECTED '''
    pass

def p_visibility_default(p):
    '''visibility : '''
    pass

    #MODIFICADORES
def p_classmodifier_default(p):
    '''classmodifier : '''
    pass

def p_classmodifier_abstract(p):
    '''classmodifier : ABSTRACT'''
    pass

def p_classmodifier_final(p):
    '''classmodifier : FINAL'''
    pass

#MEMBROS
def p_membros(p):
    '''membros : membro'''
    pass

def p_multimembros(p): #multimembros
    '''membros : membro membros'''
    pass

def p_membro_atribute(p):
    '''membro : atribute'''    
    pass

def p_membrofunction(p):
    '''membro : function'''    
    pass

#ATRIBUTOS
def p_atribute(p):
    '''atribute :  visibility atributemodifier ID'''
    pass

def p_atributemodifier_default(p):
    '''atributemodifier : '''
    pass

def p_atributemodifier_static(p):
    '''atributemodifier : STATIC'''
    pass

def p_atributemodifier_final(p):
    '''atributemodifier : FINAL'''
    pass

#FUNÇÕES
def p_function(p):
    '''function : signature body'''
    pass

def p_signature(p):
    ''' signature : visibility ID ID LPAREN sigparams RPAREN'''
    pass

def p_sigparams_id(p):
    '''sigparams : ID'''
    pass

def p_sigparams_sigparams(p):
    '''sigparams : ID COMMA sigparams'''
    pass

def p_body(p):
    '''body : LCHAV stms RCHAV'''
    pass

def p_stms(p):
    '''stms : stm'''
    pass

def p_multistms(p):
    '''stms : stm stms'''
    pass

#COMANDOS SWITCH
def p_stm_exp(p):
    '''stm : expression PV'''
    pass

def p_stm_while(p):
    '''stm : WHILE LPAREN expression RPAREN bodyorstm'''
    pass

def p_stm_dowhile(p):
    '''stm : DO bodyorstm WHILE LPAREN expression RPAREN PV '''
    pass

def p_stm_for(p):
    '''stm : FOR LPAREN expression PV expression PV expression PV RPAREN bodyorstm'''
    pass

def p_stm_if(p):
    '''stm : IF LPAREN expression RPAREN bodyorstm'''
    pass

def p_stm_ifelse(p):
    '''stm : IF LPAREN expression RPAREN bodyorstm ELSE bodyorstm'''
    pass

def p_stmd_elseif(p):
    '''stm : IF LPAREN expression RPAREN bodyorstm ELSE IF bodyorstm'''
    pass


    
    #---------------FALTANDO COMANDOS (switch)-------------------------

def p_bodyorstm_body(p):
    '''bodyorstm : body'''
    pass

def p_bodyorstm_stm(p):
    '''bodyorstm : stm '''
    pass

#EXPRESSÕES
def p_expression(p):
    ''' expression : operator '''
    pass
    
#OPERADORES
def p_operator_arithmetic(p):
    '''operator : expression arithmetic expression'''
    pass

def p_operator_assign(p):
    '''operator : ID assign expression'''
    pass

def p_operator_operatorcomparator(p):
    '''operator : expression operatorcomparator expression'''
    pass

def p_operator_unaryoperatorprefx(p):
    '''operator : unaryoperatorprefx ID'''
    pass

def p_operator_unaryoperatorsufx(p):
    '''operator : ID unaryoperatorsufx'''
    pass

def p_operator_operatorbittobit(p):
    '''operator : expression operatorbittobit'''
    pass

def p_arithmetic(p):
    '''
        arithmetic : TIMES 
                    | DIVIDE
                    | MODULE
                    | PLUS
                    | MINUS                     
    '''
    pass

def p_assign(p):
    '''
    assign : EQUAL
            | PLUS_EQ
            | MINUS_EQ
            | TIMES_EQ
            | DIVIDE_EQ
            | MOD_EQ
            | BITWISE_AND_EQ
            | BITWISE_OR_EQ
            | BITWISE_XOR_EQ
            | URSHIFT_EQ
            | LSHIFT_EQ
            | RSHIFT_EQ
    '''
    pass

def p_operatorcomparator(p):
    '''
    operatorcomparator : LEQ
                        | GEQ
                        | LT
                        | GT
                        | NEQ
                        | EQ
                        | AND
                        | OR
                        | BITWISE_AND
                        | BITWISE_OR
                        | BITWISE_XOR
    '''
    pass

def p_unaryoperatorprefx(p):
    '''
    unaryoperatorprefx : INCREMENT
                        | DECREMENT
                        | MINUS_EQ
                        | PLUS
                        | NOT
    '''
    pass
def p_unaryoperatorsufx(p):
    '''
    unaryoperatorsufx : INCREMENT
                        | DECREMENT
    '''
    pass

def P_operatorbittobit(p):
    '''
    operatorbittobit : URSHIFT
                        | LSHIFT
                        | RSHIFT
    
    '''
    pass


def main():
    f = open("projeto/Teste2.java", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=True)


if __name__ == "__main__":
    main()
    