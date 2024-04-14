from AbstractVisitor import AbstractVisitor
from Sintatico import *

# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p


class Visitor(AbstractVisitor):

    def VisitProgramConcrete(self, programConcrete):
        pass
    
    
    def VisitCClassExtends(self, cclassExtends):
        pass
    
    
    def VisitCClassDefault(self, cclassDefault):
        pass
    
    
    def VisitCClassImplements(self, CClassImplements):
        pass  

    
    def VisitVisibilityConcrete(self, visibility):
        pass
          
    
    def VisitClassModifierConcrete(self, classmodifier):
        pass
          
    
    def VisitMembrosUni(self, membrosUni):
        pass
          
    
    def VisitMembrosMult(self, membrosMult):
        pass
          
    
    def VisitMembroAtribute(self, membroAtribute):
        pass
          
    
    def VisitMembroFunction(self, membroFunction):
        pass
          
    
    def VisitAtributeDefault(self, atributeDefault):
        pass
          
    
    def VisitAtributeDefaultInicializedType(self, atributeDefaultInicializedType):
        pass
          
    
    def VisitAtributeModifierConcrete(self, atributeModifierConcrete):
        pass
          
    
    def VisitFunctionDefault(self, functionDefault):
        pass
          
    
    def VisitSignatureSimple(self, SignatureSimple):
        pass
          
    
    def VisitSignatureMult(self, signatureMult):
        pass
          
    
    def VisitSigparamsSigparams(self, sigparamsSigparams):
        pass
              
    
    def VisitBodyStms(self, bodyStms):
        pass
              
    
    def VisitStmsUni(self, stmsUni):
        pass
              
    
    def VisitStmsMulti(self, stmsMulti):
        pass
              
    
    def VisitStmExpression(self, stmExpression):
        pass
              
    
    def VisitStmExpressionWhile(self, stmExpressionWhile):
        pass
              
    
    def VisitStmExpressionDoWhile(self, stmExpressionDoWhile):
        pass
              
    
    def VisitStmExpressionFor(self, stmExpressionFor):
        pass
              
    
    def VisitStmExpressionIf(self, stmExpressionIf):
        pass
              
    
    def VisitStmExpressionIfElse(self, stmExpressionIfElse):
        pass
              
    
    def VisitStmExpressionElseIf(self, stmExpressionElseIf):
        pass
              
    
    def VisitStmExpressionSemicolon(self, stmExpressionSemicolon):
        pass
              
    
    def VisitStmExpressionVariable(self, stmExpressionVariable):
        pass
              
    
    def VisitStmExpressionVariableType(self, stmExpressionVariableType):
        pass
              
    
    def VisitStmExpressionVariableTypeList(self, stmExpressionVariableTypeList):
        pass
              
    
    def VisitStmExpressionVariableTypeListPre(self, stmExpressionVariableTypeListPre):
        pass
              
    
    def VisitStmExpressionVariableTypeListListPre(self, stmExpressionVariableTypeListListPre):
        pass
              
    
    def VisitStmExpressionVariableTypeListExpression(self, stmExpressionVariableTypeListExpression):
        pass
              
    
    def VisitStmExpressionVariableTypeListExpressionInicialized(self, stmExpressionVariableTypeListExpressionInicialized):
        pass
              
    
    def VisitStmExpressionVariableTypeListList(self, stmExpressionVariableTypeListList):
        pass
              
    
    def VisitStmExpressionVariableTypeListListInicialized(self, stmExpressionVariableTypeListListInicialized):
        pass
              
    
    def VisitStmExpressionReturn(self, stmExpressionReturn):
        pass
              
    
    def VisitStmExpressionVoidReturn(self, stmExpressionVoidReturn):
        pass
              
    
    def VisitBodyOrStmBody(self, bodyOrStmBody):
        pass
              
    
    def VisitExpressionForAssignForType(self, expressionForAssignForType):
        pass
              
    
    def VisitExpressionForAssignFor(self, expressionForAssignFor):
        pass
              
    
    def VisitExpressionOperator(self, expressionOperator):
        pass
              
    
    def VisitExpressionCall(self, expressionCall):
        pass
              
    
    def VisitExpressionFloatNumber(self, expressionFloatNumber):
        pass
              
    
    def VisitExpressionDoubleNumber(self, expressionDoubleNumber):
        pass
              
    
    def VisitExpressionIntNumber(self, expressionIntNumber):
        pass
              
    
    def VisitExpressionString(self, expressionString):
        pass
              
    def VisitExpressionId(self, expressionId):
        pass
              
    
    def VisitExpressionNew(self, expressionNew):
        pass
              
    
    def VisitExpressionNewList(self, expressionNewList):
        pass
              
    
    def VisitOperatorArithmeticTimes(self, operatorArithmeticTimes):
        pass
              
    
    def VisitOperatorArithmeticDivide(self, operatorArithmeticDivide):
        pass
              
    
    def VisitOperatorArithmeticModule(self, operatorArithmeticModule):
        pass
              
    
    def VisitOperatorArithmeticPlus(self, operatorArithmeticPlus):
        pass
              
    
    def VisitOperatorArithmeticMinus(self, operatorArithmeticMinus):
        pass
              
    
    def VisitOperatorAssignEqual(self, operatorAssignEqual):
        pass
              
    
    def VisitOperatorAssignMinusEQ(self, operatorAssignMinusEQ):
        pass
              
    
    def VisitOperatorAssignTimesEQ(self, operatorAssignTimesEQ):
        pass
              
    
    def VisitOperatorAssignPlusEQ(self, operatorAssignPlusEQ):
        pass
              
    
    def VisitOperatorAssignDivideEQ(self, operatorAssignDivideEQ):
        pass
              
    
    def VisitOperatorAssignModuleEQ(self, operatorAssignModuleEQ):
        pass
              
    
    def VisitOperatorAssignBitwiseAndEQ(self, operatorAssignBitwiseAndEQ):
        pass
              
    
    def VisitOperatorAssignBitwiseOrEQ(self, operatorAssignBitwiseOrEQ):
        pass
              
    
    def VisitOperatorAssignBitwiseXorEQ(self, operatorAssignBitwiseXorEQ):
        pass
                  
    
    def VisitOperatorAssignUrshiftEQ(self, operatorAssignUrshiftEQ):
        pass
                  
    
    def VisitOperatorAssignLshiftEQ(self, operatorAssignLshiftEQ):
        pass
                  
    
    def VisitOperatorAssignRshiftEQ(self, operatorAssignRshiftEQ):
        pass
                  
    
    def VisitOperatorComparatorLeq(self, operatorComparatorLeq):
        pass
                  
    
    def VisitOperatorComparatorGeq(self, operatorComparatorGeq):
        pass
                  
    
    def VisitOperatorComparatorLt(self, operatorComparatorLt):
        pass
                  
    
    def VisitOperatorComparatorGt(self, operatorComparatorGt):
        pass
                  
    
    def VisitOperatorComparatorNeq(self, operatorComparatorNeq):
        pass
                  
    
    def VisitOperatorComparatorEq(self, operatorComparatorEq):
        pass
                  
    
    def VisitOperatorComparatorAnd(self, operatorComparatorAnd):
        pass
                  
    
    def VisitOperatorComparatorOr(self, operatorComparatorOr):
        pass
                  
    
    def VisitOperatorComparatorBitwise_And(self, operatorComparatorBitwise_And):
        pass
                  
    
    def VisitOperatorComparatorBitwise_OR(self, operatorComparatorBitwise_OR):
        pass
                  
    
    def VisitOperatorComparatorBitwise_XOR(self, operatorComparatorBitwise_XOR):
        pass
                  
    
    def VisitOperatorUnaryPrefix(self, operatorUnaryPrefix):
        pass
                  
    
    def VisitOperatorUnarySufix(self, operatorUnarySufix):
        pass
                  
    
    def VisitOperatorBitToBit(self, operatorBitToBit):
        pass
                  
    
    def VisitUnaryOperatorPrefixConcrete(self, UnaryOperatorPrefixConcrete):
        pass
                  
    
    def VisitUnaryOperatorSufixConcrete(self, UnaryOperatorSufixConcrete):
        pass
                  
    
    def VisitUnaryOperatorBitToBitConcrete(self, UnaryOperatorBitToBitConcrete):
        pass
                  
    
    def VisitBracketsExpressionSimple(self, BracketsExpressionSimple):
        pass
                  
    
    def VisitBracketsExpressionIntNumber(self, BracketsExpressionIntNumber):
        pass
                  
    
    def VisitBracketsExpressionId(self, BracketsExpressionId):
        pass
                  
    
    def VisitTypePrimitive(self, TypePrimitive):
        pass
                  
    
    def VisitPrimitiveTypesConcrete(self, PrimitiveTypesConcrete):
        pass
                  
    
    def VisitCallParams(self, CallParams):
        pass
                      
    
    def VisitCallDefault(self, CallDefault):
        pass
                      
    
    def VisitParamsCallMulti(self, ParamsCallMulti):
        pass
                      
    
    def VisitParamsCallUnique(self, ParamsCallUnique):
        pass
                      
    
    def VisitChavExpEmpty(self, ChavExpEmpty):
        pass
                      
    
    def VisitChavExpExpressionChav(self, ChavExpExpressionChav):
        pass
                      
    
    def VisitExpressionChavMult(self, ExpressionChavMult):
        pass
                          
    
    def VisitExpressionChavUni(self, ExpressionChavUni):
        pass
                          
    
    def VisitExpressionChavComma(self, ExpressionChavComma):
        pass
    
    
def main():
    f = open("projeto/Teste2.java", "r")
    lexer = lex.lex()
    lexer.input(f.read())
    parser = yacc.yacc()
    result = parser.parse(debug=False)
    print("#imprime o programa que foi passado como entrada")
    visitor = Visitor()
    for r in result:
        r.accept(visitor)

if __name__ == "__main__":
    main()