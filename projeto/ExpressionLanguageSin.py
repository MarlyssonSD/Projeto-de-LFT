from ExpressionLanguageLex import *
import ply.yacc as yacc

#https://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html

precedence = (
    ('left', 'EQUAL','MINUS_EQ','TIMES_EQ','PLUS_EQ','DIVIDE_EQ','MOD_EQ','BITWISE_AND_EQ','BITWISE_OR_EQ','BITWISE_XOR_EQ','URSHIFT_EQ','LSHIFT_EQ','RSHIFT_EQ'),
    ('left','OR'),
    ('left','AND'),
    ('left','BITWISE_OR'),
    ('left','BITWISE_XOR'),
    ('left','BITWISE_AND'),
    ('left','EQ','NEQ'),
    ('left','LT','GT','LEQ','GEQ'),
    ('left','LSHIFT','RSHIFT','URSHIFT'),
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE','MODULE'),
    ('left','LINCREMENT','LDECREMENT','UPLUS','UMINUS','NOT'),
    ('left','RINCREMENT','RDECREMENT'),
)

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

def p_classmodifier_package(p):
    '''classmodifier : PACKAGE'''
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
    '''atribute : visibility atributemodifier type ID SEMICOLON'''
    pass

def p_atribute_inicialized_type(p):
    '''atribute : visibility atributemodifier type ID EQUAL expression SEMICOLON'''
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
    ''' signature : visibility atributemodifier type ID LPAREN sigparams RPAREN '''
    pass

def p_signature_list(p):
    ''' signature : visibility atributemodifier type brackets_expression ID LPAREN sigparams RPAREN '''
    pass

def p_sigparams_id(p):
    '''sigparams : type ID  '''
    pass

def p_sigparams_sigparams(p):
    '''sigparams : type ID COMMA sigparams'''
    pass


def p_body(p):
    '''body : LCHAV stms RCHAV'''
    pass

def p_stms(p):
    '''stms : stm '''
    pass

def p_multistms(p):
    '''stms : stm stms '''
    pass

def p_stm_exp(p):
    '''stm : expression SEMICOLON'''
    pass

def p_stm_while(p):
    '''stm : WHILE LPAREN expression RPAREN bodyorstm'''
    pass

def p_stm_dowhile(p):
    '''stm : DO bodyorstm WHILE LPAREN expression RPAREN SEMICOLON '''
    pass

def p_stm_for(p):
    '''stm : FOR LPAREN expression SEMICOLON expression SEMICOLON expression SEMICOLON RPAREN bodyorstm'''
    pass

def p_stm_if(p):
    '''stm : IF LPAREN expression RPAREN bodyorstm'''
    pass

def p_stm_ifelse(p):
    '''stm : IF LPAREN expression RPAREN bodyorstm ELSE bodyorstm'''
    pass

def p_stm_elseif(p):
    '''stm : IF LPAREN expression RPAREN bodyorstm ELSE IF bodyorstm'''
    pass

def p_stm_semicollon(p):
    '''stm : SEMICOLON '''
    pass

def p_stm_variable(p):
    '''stm : '''
    
    
def p_stm_variable(p):
    '''stm : atributemodifier type ID SEMICOLON'''
    pass


def p_stm_variable_type(p):
    '''stm : atributemodifier type ID EQUAL expression SEMICOLON'''
    pass

def p_stm_return(p):
    '''stm : RETURN expression SEMICOLON'''
    pass


    
    
    
    #---------------FALTANDO COMANDOS (switch)-------------------------

def p_bodyorstm_body(p):
    '''bodyorstm : body'''
    pass


#EXPRESSÕES
def p_expression(p):
    ''' expression : operator '''
    pass

def p_expression_call(p):
    ''' expression : call '''
    pass

def p_expression_FLOAT_NUMBER(p):
    ''' expression : FLOAT_NUMBER '''
    pass

def p_expression_INT_NUMBER(p):
    ''' expression : INT_NUMBER '''
    pass

def p_expression_STRING(p):
    ''' expression : STRING '''
    pass

def p_expression_ID (p):
    ''' expression : ID  '''
    pass

def p_expression_new(p):
    '''expression : NEW type LPAREN params_call RPAREN '''
    pass

def p_expression_new_list(p):
    '''expression : NEW type LBRACKET expression RBRACKET '''
    


#OPERADORES
def p_operator_arithmetic_times(p):
    '''operator : expression TIMES expression'''
    pass

def p_operator_arithmetic_divide(p):
    '''operator : expression DIVIDE expression'''
    pass

def p_operator_arithmetic_module(p):
    '''operator : expression MODULE expression'''
    pass

def p_operator_arithmetic_plus(p):
    '''operator : expression PLUS expression'''
    pass

def p_operator_arithmetic_minus(p):
    '''operator : expression MINUS expression'''
    pass


def p_operator_assign_EQUAL(p):
    '''operator : ID EQUAL expression'''
    pass

def p_operator_assign_MINUS_EQ(p):
    '''operator : ID MINUS_EQ expression'''
    pass

def p_operator_assign_TIMES_EQ(p):
    '''operator : ID TIMES_EQ expression'''
    pass

def p_operator_assign_PLUS_EQ(p):
    '''operator : ID PLUS_EQ expression'''
    pass

def p_operator_assign_DIVIDE_EQ(p):
    '''operator : ID DIVIDE_EQ expression'''
    pass

def p_operator_assign_MOD_EQ(p):
    '''operator : ID MOD_EQ expression'''
    pass

def p_operator_assign_BITWISE_AND_EQ(p):
    '''operator : ID BITWISE_AND_EQ expression'''
    pass

def p_operator_assign_BITWISE_OR_EQ(p):
    '''operator : ID BITWISE_OR_EQ expression'''
    pass

def p_operator_assign_BITWISE_XOR_EQ(p):
    '''operator : ID BITWISE_XOR_EQ expression'''
    pass

def p_operator_assign_URSHIFT_EQ(p):
    '''operator : ID URSHIFT_EQ expression'''
    pass

def p_operator_assign_LSHIFT_EQ(p):
    '''operator : ID LSHIFT_EQ expression'''
    pass

def p_operator_assign_RSHIFT_EQ(p):
    '''operator : ID RSHIFT_EQ expression'''
    pass


def p_operator_operatorcomparator_LEQ(p):
    '''operator : expression LEQ expression'''
    pass

def p_operator_operatorcomparator_GEQ(p):
    '''operator : expression GEQ expression'''
    pass

def p_operator_operatorcomparator_LT(p):
    '''operator : expression LT expression'''
    pass

def p_operator_operatorcomparator_GT(p):
    '''operator : expression GT expression'''
    pass

def p_operator_operatorcomparator_NEQ(p):
    '''operator : expression NEQ expression'''
    pass

def p_operator_operatorcomparator_EQ(p):
    '''operator : expression EQ expression'''
    pass

def p_operator_operatorcomparator_AND(p):
    '''operator : expression AND expression'''
    pass

def p_operator_operatorcomparator_OR(p):
    '''operator : expression OR expression'''
    pass

def p_operator_operatorcomparator_BITWISE_AND(p):
    '''operator : expression BITWISE_AND expression'''
    pass

def p_operator_operatorcomparator_BITWISE_OR(p):
    '''operator : expression BITWISE_OR expression'''
    pass

def p_operator_operatorcomparator_BITWISE_XOR(p):
    '''operator : expression BITWISE_XOR expression'''
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




# def p_operatorcomparator(p):
#     '''
#     operatorcomparator : LEQ
#                         | GEQ
#                         | LT
#                         | GT
#                         | NEQ
#                         | EQ
#                         | AND
#                         | OR
#                         | BITWISE_AND
#                         | BITWISE_OR
#                         | BITWISE_XOR
#     '''
#     pass

def p_unaryoperatorprefx(p):
    '''
    unaryoperatorprefx : INCREMENT %prec LINCREMENT
                        | DECREMENT %prec LDECREMENT
                        | MINUS %prec UMINUS
                        | PLUS %prec UPLUS
                        | NOT
    '''
    pass
def p_unaryoperatorsufx(p):
    '''
    unaryoperatorsufx : INCREMENT %prec RINCREMENT
                        | DECREMENT %prec RDECREMENT
    '''
    pass

def p_operatorbittobit(p):
    '''
    operatorbittobit : URSHIFT
                        | LSHIFT
                        | RSHIFT
    
    '''
    pass


def p_brackets_expression(p):
    ''' brackets_expression : LBRACKET RBRACKET
                            | LBRACKET INT_NUMBER RBRACKET
                            | LBRACKET ID RBRACKET
    '''

#TIPOS PRIMITIVOS
def p_type(p):
    ''' type : primitivetypes'''
    pass

def p_primitivetypes(p):
    '''primitivetypes : TYPE_INT
                        | TYPE_FLOAT
                        | TYPE_DOUBLE
                        | TYPE_BYTE
                        | TYPE_BOOLEAN
                        | TYPE_CHAR
                        | TYPE_STRING
                        | TYPE_LONG
                        | TYPE_VOID

    '''
    pass



def p_call(p):
    ''' call : ID LPAREN params_call RPAREN'''
    pass

def p_call_default(p):
    ''' call : ID LPAREN RPAREN'''
    pass

def p_params_multi(p):
    ''' params_call : expression COMMA params_call'''
    pass

def p_params_unique(p):
    ''' params_call : expression'''
    pass




def main():
    f = open("projeto\\Teste2.java", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=False) #True


if __name__ == "__main__":
    main()
    