from abc import abstractmethod
from abc import ABCMeta

#PROGRAM
class Program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass
        
class ProgramConcrete(Program):
    def __init__(self, _class):
        self._class = _class
    def accept(self, visitor):
        pass
        
        
#CLASS
class _Class(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass
    
class CClassExtends(_Class):
    def __init__(self,visibility, classmodifier,  ID_NOMECLASS, ID_NOMEEXTENDS, membros):
        self.visibility = visibility
        self.classmodifier = classmodifier
        self.ID_NOMECLASS = ID_NOMECLASS
        self.ID_NOMEEXTENDS = ID_NOMEEXTENDS
        self.membros = membros
    def accept(self, visitor):
        pass
        
class CClassDefault(_Class):
    def __init__(self, visibility, classmodifier, ID_NOMECLASS,  membros):
        self.visibility = visibility     
        self.classmodifier = classmodifier
        self.ID_NOMECLASS = ID_NOMECLASS
        self.membros = membros
    def accept(self, visitor):
        pass
    
class CClassImplements(_Class):
    def __init__(self, visibility, classmodifier, ID_NOMECLASS, membros):
        self.visibility = visibility
        self.classmodifier = classmodifier
        self.ID_NOMECLASS = ID_NOMECLASS
        self.membros = membros
    def accept(self, visitor):
        pass


#VISIBILIDADE
class Visibility(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass
    
    
class VisibilityConcrete(Visibility):
    def __init__(self,visibilidade):
        self.visibilidade = visibilidade
    def accept(self, visitor):
        pass

    
#CLASSMODIFIER
class ClassModifier(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass
  
class ClassModifierConcrete(ClassModifier):
    def __init__(self, classmodifier):
        self.classmodifier = classmodifier
    def accept(self, visitor):
        pass
    
# class ClassModifierDefault(ClassModifier):
#     def __init__(self):
#         pass
#     def accept(self, visitor):
#         pass
    
# class ClassModifierAbstract(ClassModifier):
#     def __init__(self):
#         pass
#     def accept(self, visitor):
#         pass
    
# class ClassModifierFinal(ClassModifier):
#     def __init__(self):
#         pass
#     def accept(self, visitor):
#         pass    

# class ClassModifierPackage(ClassModifier):
#     def __init__(self):
#         pass
#     def accept(self, visitor):
        # pass
    
    
#MEMBROS
class Membros(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass
    
class MembrosUni(Membros):
    def __init__(self, membro):
        self.membro = membro
    def accept(self, visitor):
        pass
    
class MembrosMult(Membros):
    def __init__(self, membro, membros):
        self.membro = membro
        self.membros = membros
    def accept(self, visitor):
        pass
    
    
#MEMBRO
class Membro(metaclass=ABCMeta):
    @abstractmethod
    def accept(self,visitor):
        pass
    
class MembroAtribute(Membro):
    def __init__(self,atribute):
        self.atribute = atribute
    def accept(self, visitor):
        pass

class MembroFunction(Membro):
    def __init__(self, function):
        self.function = function
    def accept(self, visitor):
        pass


#ATRIBUTOS
class Atribute(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class AtributeDefault(Atribute):
    def __init__(self, visibility, atributemodifier, type, ID):
        self.visibility = visibility
        self.atributemodifier = atributemodifier
        self.type = type
        self.ID = ID
    def accept(self, visitor):
        pass
    
class AtributeDefaultInicializedType(Atribute):
    def __init__(self, visibility, atributemodifier, type, ID, expression):
        self.visibility = visibility
        self.atributemodifier = atributemodifier
        self.type = type
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass
    
    
#ATRIBUTEMODIFIER
class AtributeModifier(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class AtributeModifierConcrete(AtributeModifier):
    def __init__(self,atributemodifier):
        self.atributemodifier = atributemodifier
    def accept(self, visitor):
        pass


#FUNÇÕES
class Function(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class FunctionDefault(Function):
    def __init__(self, signature, body):
        self.signature = signature
        self.body = body
    def accept(self, visitor):
        pass
    

#SIGNATURE
class Signature(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class SignatureSimple(Signature):
    def __init__(self, visibility, atributemodifier, type, ID, sigparams):
        self.visibility = visibility
        self.atributemodifier = atributemodifier
        self.type = type
        self.ID = ID
        self.sigparams = sigparams
    def accept(self, visitor):
        pass
        
class SignatureMult(Signature):
    def __init__(self, visibility, atributemodifier, type, brackets_expression, ID, sigparams):
        self.visibility = visibility
        self.atributemodifier = atributemodifier
        self.type = type
        self.brackets_expression = brackets_expression
        self.ID = ID
        self.sigparams = sigparams
    def accept(self, visitor):
        pass
    

#SIGPARAMS
class Sigparams(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class SigparamsId(Sigparams):
    def __init__(self, type, ID):
        self.type = type
        self.ID = ID
    def accept(self, visitor):
        pass
    
class SigparamsSigparams(Sigparams):
    def __init__(self, type, ID, sigparams):
        self.type = type
        self.ID = ID
        self.sigparams = sigparams
               
               
#BODY
class Body(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class BodyStms(Body):
    def __init__(self, stms):
        self.stms = stms
    def accept(self, visitor):
        pass
    
#STMS
class Stms(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class StmsUni(Stms):
    def __init__(self, stm):
        self.stm = stm
    def accept(self, visitor):
        pass
    
class StmsMulti(Stms):
    def __init__(self, stm, stms):
        self.stm = stm
        self.stms = stms
    def accept(self, visitor):
        pass


#STM
class Stm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class StmExpression(Stm):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        pass
    
class StmExpressionWhile(Stm):
    def __init__(self, expression, bodyorstm):
        self.expression = expression
        self.bodyorstm = bodyorstm
    def accept(self, visitor):
        pass
    
class StmExpressionDoWhile(Stm):
    def __init__(self, bodyorstm, expression):
        self.bodyorstm = bodyorstm
        self.expression = expression
    def accept(self, visitor):
        pass
    
class StmExpressionFor(Stm):
    def __init__(self, expression_for, expression_mid, expression_final, bodyorstm):
        self.expression_for = expression_for
        self.expression_mid = expression_mid
        self.expression_final = expression_final
        self.bodyorstm = bodyorstm
    def accept(self, visitor):
        pass
        
class StmExpressionIf(Stm):
    def __init__(self, expression, bodyorstm):
        self.expression = expression
        self.bodyorstm = bodyorstm
    def accept(self, visitor):
        pass
        
class StmExpressionIfElse(Stm):
    def __init__(self, expression, bodyorstm_1,bodyorstm_2):
        self.expression = expression
        self.bodyorstm_1 = bodyorstm_1
        self.bodyorstm_2 = bodyorstm_2
    def accept(self, visitor):
        pass
        
class StmExpressionElseIf(Stm):
    def __init__(self, expression, bodyorstm_1,bodyorstm_2):
        self.expression = expression
        self.bodyorstm_1 = bodyorstm_1
        self.bodyorstm_2 = bodyorstm_2
    def accept(self, visitor):
        pass
    
class StmExpressionSemicolon(Stm):
    def __init__(self):
        pass
    def accept(self, visitor):
        pass     
        
class StmExpressionVariable(Stm):
    def __init__(self, atributemodifier, type, ID):
        self.atributemodifier = atributemodifier
        self.type = type
        self.ID = ID
    def accept(self, visitor):
        pass        
                
class StmExpressionVariableType(Stm):
    def __init__(self, atributemodifier, type, ID, expression):
        self.atributemodifier = atributemodifier
        self.type = type
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass
    
class StmExpressionReturn(Stm):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        pass
    
class StmExpressionVoidReturn(Stm):
    def __init__(self, void_return):
        self.void_return = void_return
    def accept(self, visitor):
        pass

#BODYORSTM
class BodyOrStm(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class BodyOrStmBody(BodyOrStm):
    def __init__(self, body):
        self.body = body
    def accept(self, visitor):
        pass
        
#EXPRESSIONFOR
class ExpressionFor(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ExpressionForAssignForType(ExpressionFor):
    def __init__(self, type, ID, expression):
        self.type = type 
        self.ID = ID 
        self.expression = expression 
    def accept(self, visitor):
        pass
    
class ExpressionForAssignFor(ExpressionFor):
    def __init__(self, ID, expression):
        self.ID = ID 
        self.expression = expression 
    def accept(self, visitor):
        pass
    
    
    
#EXPRESSION
class Expression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpressionOperator(Expression):
    def __init__(self, operator):
        self.operator = operator
    def accept(self, visitor):
        pass

class ExpressionCall(Expression):
    def __init__(self, call):
        self.call = call
    def accept(self, visitor):
        pass
    
class ExpressionFloatNumber(Expression):
    def __init__(self, float_number):
        self.float_number = float_number
    def accept(self, visitor):
        pass
        
class ExpressionDoubleNumber(Expression):
    def __init__(self, double_number):
        self.double_number = double_number
    def accept(self, visitor):
        pass
        
class ExpressionIntNumber(Expression):
    def __init__(self, int_number):
        self.int_number = int_number
    def accept(self, visitor):
        pass
    
class ExpressionString(Expression):
    def __init__(self, string):
        self.string = string
    def accept(self, visitor):
        pass
        
class ExpressionId(Expression):
    def __init__(self, ID):
        self.ID = ID
    def accept(self, visitor):
        pass
        
class ExpressionNew(Expression):
    def __init__(self, type, params_call):
        self.type = type
        self.params_call = params_call
    def accept(self, visitor):
        pass
        
class ExpressionNewList(Expression):
    def __init__(self, type, expression):
        self.type = type
        self.expression = expression
    def accept(self, visitor):
        pass       
        

#OPERATOR
class Operator(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class OperatorArithmeticTimes(Operator):
    def __init__(self,expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass
    
class OperatorArithmeticDivide(Operator):
    def __init__(self,expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass
    
class OperatorArithmeticModule(Operator):
    def __init__(self,expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass
    
class OperatorArithmeticPlus(Operator):
    def __init__(self,expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass
    
class OperatorArithmeticMinus(Operator):
    def __init__(self,expression_1, expression_2):
            self.expression_1 = expression_1
            self.expression_2 = expression_2
    def accept(self, visitor):
        pass

class OperatorAssignEqual(Operator):
    def __init__(self, ID, expression):
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass
    
class OperatorAssignMinusEQ(Operator):
    def __init__(self, ID, expression):
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass
    
class OperatorAssignTimesEQ(Operator):
    def __init__(self, ID, expression):
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass

class OperatorAssignPlusEQ(Operator):
    def __init__(self, ID, expression):
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass

class OperatorAssignDivideEQ(Operator):
    def __init__(self, ID, expression):
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass
    
class OperatorAssignModuleEQ(Operator):
    def __init__(self, ID, expression):
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass
    
class OperatorAssignBitwiseAndEQ(Operator):
    def __init__(self, ID, expression):
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass
    
class OperatorAssignBitwiseOrEQ(Operator):
    def __init__(self, ID, expression):
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass
    
class OperatorAssignBitwiseXorEQ(Operator):
    def __init__(self, ID, expression):
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass
    
class OperatorAssignUrshiftEQ(Operator):
    def __init__(self, ID, expression):
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass
    
class OperatorAssignLshiftEQ(Operator):
    def __init__(self, ID, expression):
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass

class OperatorAssignRshiftEQ(Operator):
    def __init__(self, ID, expression):
        self.ID = ID
        self.expression = expression
    def accept(self, visitor):
        pass
    
class OperatorComparatorLeq(Operator):
    def __init__(self, expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass

class OperatorComparatorGeq(Operator):
    def __init__(self, expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass
    
class OperatorComparatorLt(Operator):
    def __init__(self, expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass

class OperatorComparatorGt(Operator):
    def __init__(self, expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass
    
class OperatorComparatorNeq(Operator):
    def __init__(self, expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass
    
class OperatorComparatorEq(Operator):
    def __init__(self, expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass
    
class OperatorComparatorAnd(Operator):
    def __init__(self, expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass
    
class OperatorComparatorOr(Operator):
    def __init__(self, expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass
    
class OperatorComparatorBitwise_And(Operator):
    def __init__(self, expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass

class OperatorComparatorBitwise_OR(Operator):
    def __init__(self, expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass
    
class OperatorComparatorBitwise_XOR(Operator):
    def __init__(self, expression_1, expression_2):
        self.expression_1 = expression_1
        self.expression_2 = expression_2
    def accept(self, visitor):
        pass
    
class OperatorUnaryPrefix(Operator):
    def __init__(self, unaryoperatorprefx, ID):
        self.unaryoperatorprefx = unaryoperatorprefx
        self.ID = ID
    def accept(self, visitor):
        pass
    
class OperatorUnarySufix(Operator):
    def __init__(self, ID, unaryoperatorsufix):
        self.unaryoperatorsufix = unaryoperatorsufix
        self.ID = ID
    def accept(self, visitor):
        pass
        
class OperatorBitToBit(Operator):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        pass


#UNARYOPERATORPREFIX
class UnaryOperatorPrefix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class UnaryOperatorPrefixConcrete(UnaryOperatorPrefix):
    def __init__(self, unaryoperatorprefx):
        self.unaryoperatorprefx = unaryoperatorprefx
    def accept(self, visitor):
        pass
    

#UNARYOPERATORSUFIX
class UnaryOperatorSufix(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class UnaryOperatorSufixConcrete(UnaryOperatorSufix):
    def __init__(self, unaryoperatorsufix):
        self.unaryoperatorsufix = unaryoperatorsufix
    def accept(self, visitor):
        pass
    
#UNARYOPERATORBITTOBIT
class UnaryOperatorBitToBit(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class UnaryOperatorBitToBitConcrete(UnaryOperatorBitToBit):
    def __init__(self, unaryoperatorbit):
        self.unaryoperatorbit = unaryoperatorbit
    def accept(self, visitor):
        pass        
        
#BRACKETSEXPRESSION       
class BracketsExpression(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
          
class BracketsExpressionSimple(BracketsExpression):
    def __init__(self, brackets_default):
        self.brackets_default = brackets_default
    def accept(self, visitor):
        pass     
          
class BracketsExpressionIntNumber(BracketsExpression):
    def __init__(self, int_number):
        self.int_number = int_number
    def accept(self, visitor):
        pass 
    
class BracketsExpressionId(BracketsExpression):
    def __init__(self, ID):
        self.ID = ID
    def accept(self, visitor):
        pass 
    

    
#TYPE
class Type(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class Type(Type):
    def __init__(self, primitivetypes):
        self.primitivetypes = primitivetypes
    def accept(self, visitor):
        pass
        
        
#PRIMITIVETYPES
class PrimitiveTypes(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class PrimitiveTypesConcrete(PrimitiveTypes):
    def __init__(self, primitivetypes):
        self.primitivetypes = primitivetypes
    def accept(self, visitor):
        pass

# class PrimitiveTypesInt(PrimitiveTypes):
#     def __init__(self, _int):
#         self._int = _int
#     def accept(self, visitor):
#         pass
    
# class PrimitiveTypes(PrimitiveTypes):
#     def __init__(self, _float):
#         self._float = _float
#     def accept(self, visitor):
#         pass

# class PrimitiveTypesDouble(PrimitiveTypes):
#     def __init__(self, _double):
#         self._double = _double
#     def accept(self, visitor):
#         pass
    
# class PrimitiveTypesByte(PrimitiveTypes):
#     def __init__(self, _byte):
#         self._byte = _byte
#     def accept(self, visitor):
#         pass

# class PrimitiveTypesBoolean(PrimitiveTypes):
#     def __init__(self, _boolean):
#         self._boolean = _boolean
#     def accept(self, visitor):
#         pass
    
# class PrimitiveTypesChar(PrimitiveTypes):
#     def __init__(self, _char):
#         self._char = _char
#     def accept(self, visitor):
#         pass
    
# class PrimitiveTypesString(PrimitiveTypes):
#     def __init__(self, _string):
#         self._string = _string
#     def accept(self, visitor):
#         pass
        
# class PrimitiveTypesLong(PrimitiveTypes):
#     def __init__(self, _long):
#         self._long = _long
#     def accept(self, visitor):
#         pass

# class PrimitiveTypesVoid(PrimitiveTypes):
#     def __init__(self, _void):
#         self._void = _void
#     def accept(self, visitor):
#         pass
  
    
#CALL    
class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CallParams(Call):
    def __init__(self,ID , callparams):
        self.ID = ID
        self.callparams = callparams
    def accept(self, visitor):
        pass

class CallDefault(Call):
    def __init__(self, ID):
        self.ID = ID
    def accept(self, visitor):
        pass
    
#PARAMSCALL
class ParamsCall(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass
    
class ParamsCallMulti(ParamsCall):
    def __init__(self, expression, params_call):
        self.expression = expression
        self.params_call = params_call
    def accept(self, visitor):
        pass
    
class ParamsCallUnique(ParamsCall):
    def __init__(self, expression):
        self.expression = expression
    def accept(self, visitor):
        pass


    