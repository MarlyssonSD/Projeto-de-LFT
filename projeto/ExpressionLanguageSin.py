
def p_programa(p):
    ''' programa : CLASS '''
    
def p_class1(p):
    ''' class : visibility CLASS ID extends ID LCHAV membros RCHAV '''
    
def p_class2(p):
    ''' class : visibility CLASS ID LCHAV membros RCHAV '''

def p_class3(p):
    ''' class : visibility CLASS ID IMPLEMENTS LCHAV membros RCHAV '''
    