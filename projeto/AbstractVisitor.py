from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def VisitProgramConcrete(self, program):
        pass
    
    @abstractmethod
    def VisitCClassExtends(self, cclass):
        pass
    
    @abstractmethod
    def VisitCClassDefault(self, cclass):
        pass
    
    @abstractmethod
    def VisitCClassImplements(self, cclass):
        pass  
      
    @abstractmethod
    def VisitVisibilityConcrete(self, visibility):
        pass
          
    @abstractmethod
    def VisitClassModifierConcrete(self, classmodifier):
        pass
          
    @abstractmethod
    def VisitMembrosUni(self, membros):
        pass
          
    @abstractmethod
    def VisitMembrosMult(self, membros):
        pass
          
    @abstractmethod
    def VisitMembroAtribute(self, membro):
        pass
          
    @abstractmethod
    def VisitMembroFunction(self, membro):
        pass
          
    @abstractmethod
    def VisitAtributeDefault(self, atribute):
        pass
          
    @abstractmethod
    def VisitAtributeDefaultInicializedType(self, atribute):
        pass
          
    @abstractmethod
    def VisitAtributeModifierConcrete(self, atribute):
        pass
          
    @abstractmethod
    def VisitFunctionDefault(self, function):
        pass
          
    @abstractmethod
    def VisitSignatureSimple(self, signature):
        pass
          
    @abstractmethod
    def VisitSignatureMult(self, signature):
        pass
          
    @abstractmethod
    def VisitSigparamsSigparams(self, sigparams):
        pass
              
    @abstractmethod
    def VisitBodyStms(self, body):
        pass
              
    @abstractmethod
    def VisitStmsUni(self, stms):
        pass
              
    @abstractmethod
    def VisitStmsMulti(self, stms):
        pass
              
    @abstractmethod
    def VisitStmExpression(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionWhile(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionDoWhile(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionFor(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionIf(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionIfElse(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionElseIf(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionSemicolon(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionVariable(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionVariableType(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionVariableTypeList(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionVariableTypeListPre(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionVariableTypeListListPre(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionVariableTypeListExpression(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionVariableTypeListExpressionInicialized(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionVariableTypeListList(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionVariableTypeListListInicialized(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionReturn(self, stm):
        pass
              
    @abstractmethod
    def VisitStmExpressionVoidReturn(self, stm):
        pass
              
    @abstractmethod
    def VisitBodyOrStmBody(self, bodyOrStm):
        pass
              
    @abstractmethod
    def VisitExpressionForAssignForType(self, expressionFor):
        pass
              
    @abstractmethod
    def VisitExpressionForAssignFor(self, expressionFor):
        pass
              
    @abstractmethod
    def VisitExpressionOperator(self, expression):
        pass
              
    @abstractmethod
    def VisitExpressionCall(self, expression):
        pass
              
    @abstractmethod
    def VisitExpressionFloatNumber(self, expression):
        pass
              
    @abstractmethod
    def VisitExpressionDoubleNumber(self, expression):
        pass
              
    @abstractmethod
    def VisitExpressionIntNumber(self, expression):
        pass
              
    @abstractmethod
    def VisitExpressionString(self, expression):
        pass
              
    @abstractmethod
    def VisitExpressionId(self, expression):
        pass
              
    @abstractmethod
    def VisitExpressionNew(self, expression):
        pass
              
    @abstractmethod
    def VisitExpressionNewList(self, expression):
        pass
              
    @abstractmethod
    def VisitOperatorArithmeticTimes(self, operator):
        pass
              
    @abstractmethod
    def VisitOperatorArithmeticDivide(self, operator):
        pass
              
    @abstractmethod
    def VisitOperatorArithmeticModule(self, operator):
        pass
              
    @abstractmethod
    def VisitOperatorArithmeticPlus(self, operator):
        pass
              
    @abstractmethod
    def VisitOperatorArithmeticMinus(self, operator):
        pass
              
    @abstractmethod
    def VisitOperatorAssignEqual(self, operator):
        pass
              
    @abstractmethod
    def VisitOperatorAssignMinusEQ(self, operator):
        pass
              
    @abstractmethod
    def VisitOperatorAssignTimesEQ(self, operator):
        pass
              
    @abstractmethod
    def VisitOperatorAssignPlusEQ(self, operator):
        pass
              
    @abstractmethod
    def VisitOperatorAssignDivideEQ(self, operator):
        pass
              
    @abstractmethod
    def VisitOperatorAssignModuleEQ(self, operator):
        pass
              
    @abstractmethod
    def VisitOperatorAssignBitwiseAndEQ(self, operator):
        pass
              
    @abstractmethod
    def VisitOperatorAssignBitwiseOrEQ(self, operator):
        pass
              
    @abstractmethod
    def VisitOperatorAssignBitwiseXorEQ(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorAssignUrshiftEQ(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorAssignLshiftEQ(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorAssignRshiftEQ(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorComparatorLeq(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorComparatorGeq(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorComparatorLt(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorComparatorGt(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorComparatorNeq(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorComparatorEq(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorComparatorAnd(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorComparatorOr(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorComparatorBitwise_And(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorComparatorBitwise_OR(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorComparatorBitwise_XOR(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorUnaryPrefix(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorUnarySufix(self, operator):
        pass
                  
    @abstractmethod
    def VisitOperatorBitToBit(self, operator):
        pass
                  
    @abstractmethod
    def VisitUnaryOperatorPrefixConcrete(self, unaryOperatorPrefix):
        pass
                  
    @abstractmethod
    def VisitUnaryOperatorSufixConcrete(self, unaryOperatorSufix):
        pass
                  
    @abstractmethod
    def VisitUnaryOperatorBitToBitConcrete(self, unaryOperatorBitToBit):
        pass
                  
    @abstractmethod
    def VisitBracketsExpressionSimple(self, bracketsExpression):
        pass
                  
    @abstractmethod
    def VisitBracketsExpressionIntNumber(self, bracketsExpression):
        pass
                  
    @abstractmethod
    def VisitBracketsExpressionId(self, bracketsExpression):
        pass
                  
    @abstractmethod
    def VisitTypePrimitive(self, type):
        pass
                  
    @abstractmethod
    def VisitPrimitiveTypesConcrete(self, primitiveTypes):
        pass
                  
    @abstractmethod
    def VisitCallParams(self, call):
        pass
                      
    @abstractmethod
    def VisitCallDefault(self, call):
        pass
                      
    @abstractmethod
    def VisitParamsCallMulti(self, paramsCall):
        pass
                      
    @abstractmethod
    def VisitParamsCallUnique(self, paramsCall):
        pass
                      
    @abstractmethod
    def VisitChavExpEmpty(self, chavExp):
        pass
                      
    @abstractmethod
    def VisitChavExpExpressionChav(self, chavExp):
        pass
                      
    @abstractmethod
    def VisitExpressionChavMult(self, expressionChav):
        pass
                          
    @abstractmethod
    def VisitExpressionChavUni(self, expressionChav):
        pass
                          
    @abstractmethod
    def VisitExpressionChavComma(self, expressionChav):
        pass
    