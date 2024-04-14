from AbstractVisitor import AbstractVisitor
from projeto.Sintatico import *

# global tab
tab = 0

def blank():
    p = ''
    for x in range(tab):
        p = p + ' '
    return p

class Visitor(AbstractVisitor):

    def VisitProgramConcrete(self, programConcrete):
        for cclass in programConcrete.cclass:
            cclass.accept(self)

    def VisitCClassExtends(self, cclassExtends):
        cclassExtends.visibility.accept(self)
        print(cclassExtends.extendClass.name, end='')
        if cclassExtends.classModifiers != None:
            for classModifier in cclassExtends.classModifiers:
                classModifier.accept(self)
        print(blank() + '{')
        cclassExtends.membrosUni.accept(self)
        print(blank() + '}')

    def VisitCClassDefault(self, cclassDefault):
        cclassDefault.visibility.accept(self)
        print('class', end='')
        if cclassDefault.classModifiers != None:
            for classModifier in cclassDefault.classModifiers:
                classModifier.accept(self)
        print(cclassDefault.name, end='')
        if cclassDefault.extendsClass != None:
            print('extends', end='')
            cclassDefault.extendsClass.accept(self)
        if cclassDefault.implementsClasses != None:
            for cclassImplements in cclassDefault.implementsClasses:
                cclassImplements.accept(self)
        print(blank() + '{')
        cclassDefault.membrosUni.accept(self)
        print(blank() + '}')

    def VisitCClassImplements(self, CClassImplements):
        print('implements', end='')
        CClassImplements.className.accept(self)

    def VisitVisibilityConcrete(self, visibility):
        if (visibility.visibilityType == 'public'):
            print('public', end='')
        elif (visibility.visibilityType == 'private'):
            print('private', end='')
        elif (visibility.visibilityType == 'protected'):
            print('protected', end='')

    def VisitClassModifierConcrete(self, classmodifier):
        if (classmodifier.classModifierType == 'final'):
            print('final', end='')
        elif (classmodifier.classModifierType == 'abstract'):
            print('abstract', end='')

    def VisitMembrosUni(self, membrosUni):
        if membrosUni != None:
            for membro in membrosUni:
                membro.accept(self)

    def VisitMembrosMult(self, membrosMult):
        if membrosMult != None:
            for membro in membrosMult:
                membro.accept(self)

    def VisitMembroAtribute(self, membroAtribute):
        atributeDefault = membroAtribute.atributeDefault
        if atributeDefault != None:
            atributeDefault.accept(self)
        print(membroAtribute.type.name, end='')
        print(' ', membroAtribute.id.name, ';', sep='')

    def VisitMembroFunction(self, membroFunction):
        functionDefault = membroFunction.functionDefault
        if functionDefault != None:
            functionDefault.accept(self)
        functionDefault.signature.accept(self)
        functionDefault.body.accept(self)

    def VisitAtributeDefault(self, atributeDefault):
        print('final', end='')

    def VisitAtributeDefaultInicializedType(self, atributeDefaultInicializedType):
        atributeDefaultInicializedType.type.accept(self)
        print(' ', atributeDefaultInicializedType.id.name, '=', end='')
        atributeDefaultInicializedType.expression.accept(self)
        print(';', end='')

    def VisitAtributeModifierConcrete(self, atributeModifierConcrete):
        if (atributeModifierConcrete.atributeModifierType == 'final'):
            print('final', end='')

    def VisitFunctionDefault(self, functionDefault):
        functionDefault.visibility.accept(self)
        functionDefault.returnType.accept(self)
        functionDefault.id.accept(self)
        functionDefault.signature.accept(self)

    def VisitSignatureSimple(self, SignatureSimple):
        print('(', end='')
        SignatureSimple.params.accept(self)
        print(')', end='')

    def VisitSignatureMult(self, signatureMult):
        print('(', end='')
        if (signatureMult.params != []):
            signatureMult.params[0].accept(self)
        for param in signatureMult.params[1:]:
            print(',', end='')
            param.accept(self)
        print(')', end='')

    def VisitSigparamsSigparams(self, sigparamsSigparams):
        sigparamsSigparams.accept(self)
        for sigparam in sigparamsSigparams.sigparams:
            sigparam.accept(self)

    def VisitBodyStms(self, bodyStms):
        bodyStms.accept(self)
        for stm in bodyStms.stms:
            stm.accept(self)

    def VisitStmsUni(self, stmsUni):
        stmsUni.accept(self)
        for stm in stmsUni.stms:
            stm.accept(self)

    def VisitStmsMulti(self, stmsMulti):
        stmsMulti.accept(self)
        for stm in stmsMulti.stms:
            stm.accept(self)

    def VisitStmExpression(self, stmExpression):
        print(blank(), end='')
        stmExpression.expression.accept(self)
        print(';', end='')

    def VisitStmExpressionWhile(self, stmExpressionWhile):
        print(blank(), end='')
        print('while(', end='')
        stmExpressionWhile.expression.accept(self)
        print(') ', end='')
        stmExpressionWhile.stm.accept(self)

    def VisitStmExpressionDoWhile(self, stmExpressionDoWhile):
        print(blank(), end='')
        print('do ', end='')
        stmExpressionDoWhile.stm.accept(self)
        print('while(', end='')
        stmExpressionDoWhile.expression.accept(self)
        print(');', end='')

    def VisitStmExpressionFor(self, stmExpressionFor):
        print(blank(), end='')
        print('for(', end='')
        stmExpressionFor.expressionForAssignForType.accept(self)
        print(';', end='')
        stmExpressionFor.expressionForAssignFor.accept(self)
        print(';', end='')
        stmExpressionFor.expressionOperator.accept(self)
        print(') ', end='')
        stmExpressionFor.stm.accept(self)

    def VisitStmExpressionIf(self, stmExpressionIf):
        print(blank(), end='')
        print('if(', end='')
        stmExpressionIf.expression.accept(self)
        print(') ', end='')
        stmExpressionIf.stm.accept(self)

    def VisitStmExpressionIfElse(self, stmExpressionIfElse):
        print(blank(), end='')
        print('if(', end='')
        stmExpressionIfElse.expression.accept(self)
        print(') ', end='')
        stmExpressionIfElse.stm.accept(self)
        print('else ', end='')
        stmExpressionIfElse.stmElse.accept(self)

    def VisitStmExpressionElseIf(self, stmExpressionElseIf):
        print(blank(), end='')
        print('else ', end='')
        stmExpressionElseIf.expression.accept(self)
        print('if(', end='')
        stmExpressionElseIf.expressionElseIf.accept(self)
        print(') ', end='')
        stmExpressionElseIf.stm.accept(self)

    def VisitStmExpressionSemicolon(self, stmExpressionSemicolon):
        print(blank(), end='')
        print(';', end='')

    def VisitStmExpressionVariable(self, stmExpressionVariable):
        print(blank(), end='')
        stmExpressionVariable.expressionVariableTypeList.accept(self)
        print(stmExpressionVariable.id.name, end='')

    def VisitStmExpressionVariableType(self, stmExpressionVariableType):
        print(blank(), end='')
        stmExpressionVariableType.expressionVariableTypeList.accept(self)
        print(stmExpressionVariableType.id.name, end='')

    def VisitStmExpressionVariableTypeList(self, stmExpressionVariableTypeList):
        stmExpressionVariableTypeList.accept(self)

    def VisitStmExpressionVariableTypeListPre(self, stmExpressionVariableTypeListPre):
        stmExpressionVariableTypeListPre.accept(self)

    def VisitStmExpressionVariableTypeListListPre(self, stmExpressionVariableTypeListListPre):
       stmExpressionVariableTypeListListPre.accept(self)

    def VisitStmExpressionVariableTypeListExpression(self, stmExpressionVariableTypeListExpression):
        stmExpressionVariableTypeListExpression.accept(self)

    def VisitStmExpressionVariableTypeListExpressionInicialized(self, stmExpressionVariableTypeListExpressionInicialized):
        stmExpressionVariableTypeListExpressionInicialized.accept(self)

    def VisitStmExpressionVariableTypeListList(self, stmExpressionVariableTypeListList):
        stmExpressionVariableTypeListList.accept(self)

    def VisitStmExpressionVariableTypeListListInicialized(self, stmExpressionVariableTypeListListInicialized):
        stmExpressionVariableTypeListListInicialized.accept(self)

    def VisitStmExpressionReturn(self, stmExpressionReturn):
        print(blank(), end='')
        print('return ', end='')
        stmExpressionReturn.expression.accept(self)
        print(';', end='')

    def VisitStmExpressionVoidReturn(self, stmExpressionVoidReturn):
        print(blank(), end='')
        print('return;', end='')

    def VisitBodyOrStmBody(self, bodyOrStmBody):
        bodyOrStmBody.accept(self)

    def VisitExpressionForAssignForType(self, expressionForAssignForType):
        expressionForAssignForType.accept(self)

    def VisitExpressionForAssignFor(self, expressionForAssignFor):
        expressionForAssignFor.accept(self)

    def VisitExpressionOperator(self, expressionOperator):
        expressionOperator.accept(self)

    def VisitExpressionCall(self, expressionCall):
        expressionCall.accept(self)

    def VisitExpressionFloatNumber(self, expressionFloatNumber):
        print(expressionFloatNumber.value, end='')

    def VisitExpressionDoubleNumber(self, expressionDoubleNumber):
        print(expressionDoubleNumber.value, end='')

    def VisitExpressionIntNumber(self, expressionIntNumber):
        print(expressionIntNumber.value, end='')

    def VisitExpressionString(self, expressionString):
        print(expressionString.value, end='')

    def VisitExpressionId(self, expressionId):
        print(expressionId.id.name, end='')

    def VisitExpressionNew(self, expressionNew):
        print('new ', end='')
        expressionNew.type.accept(self)

    def VisitExpressionNewList(self, expressionNewList):
        print('new ', end='')
        expressionNewList.type.accept(self)
        print('[]', end='')

    def VisitOperatorArithmeticTimes(self, operatorArithmeticTimes):
        print('*', end='')

    def VisitOperatorArithmeticDivide(self, operatorArithmeticDivide):
        print('/', end='')

    def VisitOperatorArithmeticModule(self, operatorArithmeticModule):
        print('%', end='')

    def VisitOperatorArithmeticPlus(self, operatorArithmeticPlus):
        print('+', end='')

    def VisitOperatorArithmeticMinus(self, operatorArithmeticMinus):
        print('-', end='')

    def VisitOperatorAssignEqual(self, operatorAssignEqual):
        print('=', end='')

    def VisitOperatorAssignMinusEQ(self, operatorAssignMinusEQ):
        print('-=', end='')

    def VisitOperatorAssignTimesEQ(self, operatorAssignTimesEQ):
        print('*=', end='')

    def VisitOperatorAssignPlusEQ(self, operatorAssignPlusEQ):
        print('+=', end='')

    def VisitOperatorAssignDivideEQ(self, operatorAssignDivideEQ):
        print('/=', end='')

    def VisitOperatorAssignModuleEQ(self, operatorAssignModuleEQ):
        print('%=', end='')

    def VisitOperatorAssignBitwiseAndEQ(self, operatorAssignBitwiseAndEQ):
        print('&=', end='')

    def VisitOperatorAssignBitwiseOrEQ(self, operatorAssignBitwiseOrEQ):
        print('|=', end='')

    def VisitOperatorAssignBitwiseXorEQ(self, operatorAssignBitwiseXorEQ):
        print('^=', end='')

    def VisitOperatorAssignUrshiftEQ(self, operatorAssignUrshiftEQ):
        print('>>=', end='')

    def VisitOperatorAssignLshiftEQ(self, operatorAssignLshiftEQ):
        print('<<=', end='')

    def VisitOperatorAssignRshiftEQ(self, operatorAssignRshiftEQ):
        print('>>>=', end='')

    def VisitOperatorComparatorLeq(self, operatorComparatorLeq):
        print('<=', end='')

    def VisitOperatorComparatorGeq(self, operatorComparatorGeq):
        print('>=', end='')

    def VisitOperatorComparatorLt(self, operatorComparatorLt):
        print('<', end='')

    def VisitOperatorComparatorGt(self, operatorComparatorGt):
        print('>', end='')

    def VisitOperatorComparatorNeq(self, operatorComparatorNeq):
        print('!=', end='')

    def VisitOperatorComparatorEq(self, operatorComparatorEq):
        print('==', end='')

    def VisitOperatorComparatorAnd(self, operatorComparatorAnd):
        print('&&', end='')

    def VisitOperatorComparatorOr(self, operatorComparatorOr):
        print('||', end='')

    def VisitOperatorComparatorBitwise_And(self, operatorComparatorBitwise_And):
        print('&', end='')

    def VisitOperatorComparatorBitwise_OR(self, operatorComparatorBitwise_OR):
        print('|', end='')

    def VisitOperatorComparatorBitwise_XOR(self, operatorComparatorBitwise_XOR):
        print('^', end='')

    def VisitUnaryOperatorPrefixConcrete(self, UnaryOperatorPrefixConcrete):
        UnaryOperatorPrefixConcrete.accept(self)

    def VisitUnaryOperatorSufixConcrete(self, UnaryOperatorSufixConcrete):
        UnaryOperatorSufixConcrete.accept(self)

        def VisitUnaryOperatorBitToBitConcrete(self, UnaryOperatorBitToBitConcrete):
            print(UnaryOperatorBitToBitConcrete.operator, end='')

        def VisitBracketsExpressionSimple(self, BracketsExpressionSimple):
            print('(', end='')
            BracketsExpressionSimple.expression.accept(self)
            print(')', end='')

        def VisitBracketsExpressionIntNumber(self, BracketsExpressionIntNumber):
            print('(', end='')
            BracketsExpressionIntNumber.intNumber.accept(self)
            print(')', end='')

        def VisitBracketsExpressionId(self, BracketsExpressionId):
            print('(', end='')
            BracketsExpressionId.id.accept(self)
            print(')', end='')

        def VisitTypePrimitive(self, TypePrimitive):
            print(TypePrimitive.type, end='')

        def VisitPrimitiveTypesConcrete(self, PrimitiveTypesConcrete):
            PrimitiveTypesConcrete.accept(self)

        def VisitCallParams(self, CallParams):
            CallParams.accept(self)

        def VisitCallDefault(self, CallDefault):
            CallDefault.accept(self)

        def VisitParamsCallMulti(self, ParamsCallMulti):
            ParamsCallMulti.accept(self)

        def VisitParamsCallUnique(self, ParamsCallUnique):
            ParamsCallUnique.accept(self)

        def VisitChavExpEmpty(self, ChavExpEmpty):
            pass

        def VisitChavExpExpressionChav(self, ChavExpExpressionChav):
            ChavExpExpressionChav.accept(self)

        def VisitExpressionChavMult(self, ExpressionChavMult):
            ExpressionChavMult.accept(self)

        def VisitExpressionChavUni(self, ExpressionChavUni):
            ExpressionChavUni.accept(self)

        def VisitExpressionChavComma(self, ExpressionChavComma):
            ExpressionChavComma.accept(self)


def main():
    f = open("Teste2.java", "r")
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