
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftEQUALMINUS_EQTIMES_EQPLUS_EQDIVIDE_EQMOD_EQBITWISE_AND_EQBITWISE_OR_EQBITWISE_XOR_EQURSHIFT_EQLSHIFT_EQRSHIFT_EQleftORleftANDleftBITWISE_ORleftBITWISE_XORleftBITWISE_ANDleftEQNEQleftLTGTLEQGEQleftLSHIFTRSHIFTURSHIFTleftPLUSMINUSleftTIMESDIVIDEMODULEleftLINCREMENTLDECREMENTUPLUSUMINUSNOTleftRINCREMENTRDECREMENTABSTRACT AND ASSERT BIN_NUMBER BITWISE_AND BITWISE_AND_EQ BITWISE_NOT BITWISE_OR BITWISE_OR_EQ BITWISE_XOR BITWISE_XOR_EQ BREAK BYTE_NUMBER CASE CATCH CHAR CLASS COMMA CONST CONTINUE DECREMENT DEFAULT DIVIDE DIVIDE_EQ DO DOT DOUBLE_NUMBER ELSE ENUM EQ EQUAL EXTENDS FINAL FINALLY FLOAT_NUMBER FOR GEQ GOTO GT HEXA_NUMBER ID IF IMPLEMENTS IMPORT INCREMENT INSTANCEOF INTERFACE INT_NUMBER LBRACKET LCHAV LEQ LONG_NUMBER LPAREN LSHIFT LSHIFT_EQ LT MINUS MINUS_EQ MODULE MOD_EQ MULTICOMMENT NATIVE NEQ NEW NOT OCTAL_NUMBER OR PACKAGE PLUS PLUS_EQ POT PRIVATE PROTECTED PUBLIC RBRACKET RCHAV RETURN RPAREN RSHIFT RSHIFT_EQ SEMICOLON SHORT STATIC STRICTFP STRING SUPER SWITCH SYNCHRONIZED TERNARY THIS THROW THROWS TIMES TIMES_EQ TRANSIENT TRY TYPE_BOOLEAN TYPE_BYTE TYPE_CHAR TYPE_DOUBLE TYPE_FLOAT TYPE_INT TYPE_LONG TYPE_STRING TYPE_VOID UNICOMMENT URSHIFT URSHIFT_EQ VOLATILE WHILE program : class class : visibility classmodifier CLASS ID EXTENDS ID LCHAV membros RCHAVclass : visibility classmodifier CLASS ID LCHAV membros RCHAV class : visibility classmodifier CLASS ID IMPLEMENTS LCHAV membros RCHAV visibility : PUBLIC visibility : PRIVATE visibility : PROTECTED visibility : classmodifier : classmodifier : ABSTRACTclassmodifier : FINALclassmodifier : PACKAGEmembros : membromembros : membro membrosmembro : atributemembro : functionatribute : visibility atributemodifier type ID SEMICOLONatribute : visibility atributemodifier type ID EQUAL ID SEMICOLONatribute : visibility atributemodifier type ID EQUAL expression SEMICOLONatributemodifier : atributemodifier : STATICatributemodifier : FINALfunction : signature body signature : visibility atributemodifier type ID LPAREN sigparams RPAREN sigparams : ID brackets_expression sigparams : ID brackets_expression COMMA sigparamsbody : LCHAV stms RCHAVstms : stm stms : stm stmsstm : expression SEMICOLONstm : WHILE LPAREN expression RPAREN bodyorstmstm : DO bodyorstm WHILE LPAREN expression RPAREN SEMICOLON stm : FOR LPAREN expression SEMICOLON expression SEMICOLON expression SEMICOLON RPAREN bodyorstmstm : IF LPAREN expression RPAREN bodyorstmstm : IF LPAREN expression RPAREN bodyorstm ELSE bodyorstmstm : IF LPAREN expression RPAREN bodyorstm ELSE IF bodyorstmstm : SEMICOLON bodyorstm : body expression : operator  expression : call  expression : FLOAT_NUMBER  expression : INT_NUMBER  expression : STRING  expression : ID  operator : expression arithmetic expressionoperator : ID assign expressionoperator : expression operatorcomparator expressionoperator : unaryoperatorprefx IDoperator : ID unaryoperatorsufxoperator : expression operatorbittobit brackets_expression : LBRACKET RBRACKET\n                            | LBRACKET INT_NUMBER RBRACKET\n                            | LBRACKET ID RBRACKET\n     type : primitivetypesprimitivetypes : TYPE_INT\n                        | TYPE_FLOAT\n                        | TYPE_DOUBLE\n                        | TYPE_BYTE\n                        | TYPE_BOOLEAN\n                        | TYPE_CHAR\n                        | TYPE_STRING\n                        | TYPE_LONG\n                        | TYPE_VOID\n\n    \n        arithmetic : TIMES \n                    | DIVIDE\n                    | MODULE\n                    | PLUS\n                    | MINUS                     \n    \n    assign : EQUAL\n            | MINUS_EQ\n            | TIMES_EQ\n            | PLUS_EQ\n            | DIVIDE_EQ\n            | MOD_EQ\n            | BITWISE_AND_EQ\n            | BITWISE_OR_EQ\n            | BITWISE_XOR_EQ\n            | URSHIFT_EQ\n            | LSHIFT_EQ\n            | RSHIFT_EQ\n    \n    operatorcomparator : LEQ\n                        | GEQ\n                        | LT\n                        | GT\n                        | NEQ\n                        | EQ\n                        | AND\n                        | OR\n                        | BITWISE_AND\n                        | BITWISE_OR\n                        | BITWISE_XOR\n    \n    unaryoperatorprefx : INCREMENT %prec LINCREMENT\n                        | DECREMENT %prec LDECREMENT\n                        | MINUS %prec UMINUS\n                        | PLUS %prec UPLUS\n                        | NOT\n    \n    unaryoperatorsufx : INCREMENT %prec RINCREMENT\n                        | DECREMENT %prec RDECREMENT\n    \n    operatorbittobit : URSHIFT\n                        | LSHIFT\n                        | RSHIFT\n    \n     call : ID LPAREN params RPAREN call : ID LPAREN RPAREN params : expression COMMA params params : expression'
    
_lr_action_items = {'PUBLIC':([0,14,19,20,21,23,24,30,68,116,139,140,],[4,4,4,-15,-16,4,4,-23,-27,-17,-18,-19,]),'PRIVATE':([0,14,19,20,21,23,24,30,68,116,139,140,],[5,5,5,-15,-16,5,5,-23,-27,-17,-18,-19,]),'PROTECTED':([0,14,19,20,21,23,24,30,68,116,139,140,],[6,6,6,-15,-16,6,6,-23,-27,-17,-18,-19,]),'ABSTRACT':([0,3,4,5,6,],[-8,8,-5,-6,-7,]),'FINAL':([0,3,4,5,6,14,17,19,20,21,23,24,30,68,116,139,140,],[-8,9,-5,-6,-7,-8,27,-8,-15,-16,-8,-8,-23,-27,-17,-18,-19,]),'PACKAGE':([0,3,4,5,6,],[-8,10,-5,-6,-7,]),'CLASS':([0,3,4,5,6,7,8,9,10,],[-8,-9,-5,-6,-7,11,-10,-11,-12,]),'$end':([1,2,28,65,66,],[0,-1,-3,-4,-2,]),'STATIC':([4,5,6,14,17,19,20,21,23,24,30,68,116,139,140,],[-5,-6,-7,-8,26,-8,-15,-16,-8,-8,-23,-27,-17,-18,-19,]),'TYPE_INT':([4,5,6,14,17,19,20,21,23,24,25,26,27,30,68,116,139,140,],[-5,-6,-7,-8,-20,-8,-15,-16,-8,-8,36,-21,-22,-23,-27,-17,-18,-19,]),'TYPE_FLOAT':([4,5,6,14,17,19,20,21,23,24,25,26,27,30,68,116,139,140,],[-5,-6,-7,-8,-20,-8,-15,-16,-8,-8,37,-21,-22,-23,-27,-17,-18,-19,]),'TYPE_DOUBLE':([4,5,6,14,17,19,20,21,23,24,25,26,27,30,68,116,139,140,],[-5,-6,-7,-8,-20,-8,-15,-16,-8,-8,38,-21,-22,-23,-27,-17,-18,-19,]),'TYPE_BYTE':([4,5,6,14,17,19,20,21,23,24,25,26,27,30,68,116,139,140,],[-5,-6,-7,-8,-20,-8,-15,-16,-8,-8,39,-21,-22,-23,-27,-17,-18,-19,]),'TYPE_BOOLEAN':([4,5,6,14,17,19,20,21,23,24,25,26,27,30,68,116,139,140,],[-5,-6,-7,-8,-20,-8,-15,-16,-8,-8,40,-21,-22,-23,-27,-17,-18,-19,]),'TYPE_CHAR':([4,5,6,14,17,19,20,21,23,24,25,26,27,30,68,116,139,140,],[-5,-6,-7,-8,-20,-8,-15,-16,-8,-8,41,-21,-22,-23,-27,-17,-18,-19,]),'TYPE_STRING':([4,5,6,14,17,19,20,21,23,24,25,26,27,30,68,116,139,140,],[-5,-6,-7,-8,-20,-8,-15,-16,-8,-8,42,-21,-22,-23,-27,-17,-18,-19,]),'TYPE_LONG':([4,5,6,14,17,19,20,21,23,24,25,26,27,30,68,116,139,140,],[-5,-6,-7,-8,-20,-8,-15,-16,-8,-8,43,-21,-22,-23,-27,-17,-18,-19,]),'TYPE_VOID':([4,5,6,14,17,19,20,21,23,24,25,26,27,30,68,116,139,140,],[-5,-6,-7,-8,-20,-8,-15,-16,-8,-8,44,-21,-22,-23,-27,-17,-18,-19,]),'ID':([11,13,31,34,35,36,37,38,39,40,41,42,43,44,46,48,59,60,61,62,63,64,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,96,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,117,118,134,135,138,142,144,147,149,154,159,162,164,166,],[12,16,58,67,-54,-55,-56,-57,-58,-59,-60,-61,-62,-63,58,-37,115,-92,-93,-94,-95,-96,-27,-30,58,58,-64,-65,-66,-67,-68,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,58,-38,58,58,58,58,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,129,131,58,58,58,152,-31,-34,131,58,-32,-35,-36,-33,]),'EXTENDS':([12,],[13,]),'LCHAV':([12,15,16,22,50,133,136,143,155,161,165,],[14,23,24,31,31,31,31,-24,31,31,31,]),'IMPLEMENTS':([12,],[15,]),'RCHAV':([18,19,20,21,29,30,32,33,45,46,48,68,69,70,95,116,139,140,144,147,159,162,164,166,],[28,-13,-15,-16,-14,-23,65,66,68,-28,-37,-27,-29,-30,-38,-17,-18,-19,-31,-34,-32,-35,-36,-33,]),'WHILE':([31,46,48,68,70,94,95,144,147,159,162,164,166,],[49,49,-37,-27,-30,122,-38,-31,-34,-32,-35,-36,-33,]),'DO':([31,46,48,68,70,95,144,147,159,162,164,166,],[50,50,-37,-27,-30,-38,-31,-34,-32,-35,-36,-33,]),'FOR':([31,46,48,68,70,95,144,147,159,162,164,166,],[51,51,-37,-27,-30,-38,-31,-34,-32,-35,-36,-33,]),'IF':([31,46,48,68,70,95,144,147,155,159,162,164,166,],[52,52,-37,-27,-30,-38,-31,-34,161,-32,-35,-36,-33,]),'SEMICOLON':([31,46,47,48,53,54,55,56,57,58,67,68,70,73,90,91,92,95,99,113,114,115,119,120,123,125,127,129,130,137,144,146,147,153,159,160,162,164,166,],[48,48,70,-37,-39,-40,-41,-42,-43,-44,116,-27,-30,-50,-99,-100,-101,-38,-49,-97,-98,-48,-45,-47,135,-46,-103,139,140,-102,-31,154,-34,159,-32,163,-35,-36,-33,]),'FLOAT_NUMBER':([31,46,48,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,96,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,117,134,135,138,144,147,154,159,162,164,166,],[55,55,-37,-27,-30,55,55,-64,-65,-66,-67,-68,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,55,-38,55,55,55,55,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,55,55,55,55,-31,-34,55,-32,-35,-36,-33,]),'INT_NUMBER':([31,46,48,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,96,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,117,134,135,138,142,144,147,154,159,162,164,166,],[56,56,-37,-27,-30,56,56,-64,-65,-66,-67,-68,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,56,-38,56,56,56,56,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,56,56,56,56,151,-31,-34,56,-32,-35,-36,-33,]),'STRING':([31,46,48,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,96,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,117,134,135,138,144,147,154,159,162,164,166,],[57,57,-37,-27,-30,57,57,-64,-65,-66,-67,-68,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,57,-38,57,57,57,57,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,57,57,57,57,-31,-34,57,-32,-35,-36,-33,]),'INCREMENT':([31,46,48,58,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,96,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,117,129,134,135,138,144,147,154,159,162,164,166,],[60,60,-37,113,-27,-30,60,60,-64,-65,-66,-67,-68,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,60,-38,60,60,60,60,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,60,113,60,60,60,-31,-34,60,-32,-35,-36,-33,]),'DECREMENT':([31,46,48,58,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,96,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,117,129,134,135,138,144,147,154,159,162,164,166,],[61,61,-37,114,-27,-30,61,61,-64,-65,-66,-67,-68,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,61,-38,61,61,61,61,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,61,114,61,61,61,-31,-34,61,-32,-35,-36,-33,]),'MINUS':([31,46,47,48,53,54,55,56,57,58,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,117,119,120,121,123,124,125,127,128,129,130,134,135,137,138,144,145,146,147,154,159,160,162,164,166,],[62,62,78,-37,-39,-40,-41,-42,-43,-44,-27,-30,62,62,-50,-64,-65,-66,-67,-68,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,-99,-100,-101,62,-38,62,62,62,-49,62,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-97,-98,-48,62,78,78,78,78,78,78,-103,78,-44,78,62,62,-102,62,-31,78,78,-34,62,-32,78,-35,-36,-33,]),'PLUS':([31,46,47,48,53,54,55,56,57,58,68,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,117,119,120,121,123,124,125,127,128,129,130,134,135,137,138,144,145,146,147,154,159,160,162,164,166,],[63,63,77,-37,-39,-40,-41,-42,-43,-44,-27,-30,63,63,-50,-64,-65,-66,-67,-68,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,-99,-100,-101,63,-38,63,63,63,-49,63,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,-97,-98,-48,63,77,77,77,77,77,77,-103,77,-44,77,63,63,-102,63,-31,77,77,-34,63,-32,77,-35,-36,-33,]),'NOT':([31,46,48,68,70,71,72,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,93,95,96,97,98,100,101,102,103,104,105,106,107,108,109,110,111,112,117,134,135,138,144,147,154,159,162,164,166,],[64,64,-37,-27,-30,64,64,-64,-65,-66,-67,-68,-81,-82,-83,-84,-85,-86,-87,-88,-89,-90,-91,64,-38,64,64,64,64,-69,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-80,64,64,64,64,-31,-34,64,-32,-35,-36,-33,]),'TIMES':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[74,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,74,74,74,74,74,74,-103,74,-44,74,-102,74,74,74,]),'DIVIDE':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[75,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,75,75,75,75,75,75,-103,75,-44,75,-102,75,75,75,]),'MODULE':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[76,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,76,76,76,76,76,76,-103,76,-44,76,-102,76,76,76,]),'LEQ':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[79,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,79,79,79,79,79,79,-103,79,-44,79,-102,79,79,79,]),'GEQ':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[80,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,80,80,80,80,80,80,-103,80,-44,80,-102,80,80,80,]),'LT':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[81,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,81,81,81,81,81,81,-103,81,-44,81,-102,81,81,81,]),'GT':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[82,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,82,82,82,82,82,82,-103,82,-44,82,-102,82,82,82,]),'NEQ':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[83,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,83,83,83,83,83,83,-103,83,-44,83,-102,83,83,83,]),'EQ':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[84,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,84,84,84,84,84,84,-103,84,-44,84,-102,84,84,84,]),'AND':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[85,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,85,85,85,85,85,85,-103,85,-44,85,-102,85,85,85,]),'OR':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[86,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,86,86,86,86,86,86,-103,86,-44,86,-102,86,86,86,]),'BITWISE_AND':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[87,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,87,87,87,87,87,87,-103,87,-44,87,-102,87,87,87,]),'BITWISE_OR':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[88,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,88,88,88,88,88,88,-103,88,-44,88,-102,88,88,88,]),'BITWISE_XOR':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[89,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,89,89,89,89,89,89,-103,89,-44,89,-102,89,89,89,]),'URSHIFT':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[90,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,90,90,90,90,90,90,-103,90,-44,90,-102,90,90,90,]),'LSHIFT':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[91,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,91,91,91,91,91,91,-103,91,-44,91,-102,91,91,91,]),'RSHIFT':([47,53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,121,123,124,125,127,128,129,130,137,145,146,160,],[92,-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,92,92,92,92,92,92,-103,92,-44,92,-102,92,92,92,]),'LPAREN':([49,51,52,58,67,122,129,],[93,96,97,100,118,134,100,]),'RPAREN':([53,54,55,56,57,58,73,90,91,92,99,100,113,114,115,119,120,121,124,125,126,127,128,132,137,141,145,148,150,156,157,158,163,],[-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,127,-97,-98,-48,-45,-47,133,136,-46,137,-103,-105,143,-102,-25,153,-104,-51,-26,-52,-53,165,]),'COMMA':([53,54,55,56,57,58,73,90,91,92,99,113,114,115,119,120,125,127,128,137,141,150,157,158,],[-39,-40,-41,-42,-43,-44,-50,-99,-100,-101,-49,-97,-98,-48,-45,-47,-46,-103,138,-102,149,-51,-52,-53,]),'EQUAL':([58,67,129,],[101,117,101,]),'MINUS_EQ':([58,129,],[102,102,]),'TIMES_EQ':([58,129,],[103,103,]),'PLUS_EQ':([58,129,],[104,104,]),'DIVIDE_EQ':([58,129,],[105,105,]),'MOD_EQ':([58,129,],[106,106,]),'BITWISE_AND_EQ':([58,129,],[107,107,]),'BITWISE_OR_EQ':([58,129,],[108,108,]),'BITWISE_XOR_EQ':([58,129,],[109,109,]),'URSHIFT_EQ':([58,129,],[110,110,]),'LSHIFT_EQ':([58,129,],[111,111,]),'RSHIFT_EQ':([58,129,],[112,112,]),'ELSE':([68,95,147,],[-27,-38,155,]),'LBRACKET':([131,],[142,]),'RBRACKET':([142,151,152,],[150,157,158,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'class':([0,],[2,]),'visibility':([0,14,19,23,24,],[3,17,17,17,17,]),'classmodifier':([3,],[7,]),'membros':([14,19,23,24,],[18,29,32,33,]),'membro':([14,19,23,24,],[19,19,19,19,]),'atribute':([14,19,23,24,],[20,20,20,20,]),'function':([14,19,23,24,],[21,21,21,21,]),'signature':([14,19,23,24,],[22,22,22,22,]),'atributemodifier':([17,],[25,]),'body':([22,50,133,136,155,161,165,],[30,95,95,95,95,95,95,]),'type':([25,],[34,]),'primitivetypes':([25,],[35,]),'stms':([31,46,],[45,69,]),'stm':([31,46,],[46,46,]),'expression':([31,46,71,72,93,96,97,98,100,117,134,135,138,154,],[47,47,119,120,121,123,124,125,128,130,145,146,128,160,]),'operator':([31,46,71,72,93,96,97,98,100,117,134,135,138,154,],[53,53,53,53,53,53,53,53,53,53,53,53,53,53,]),'call':([31,46,71,72,93,96,97,98,100,117,134,135,138,154,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'unaryoperatorprefx':([31,46,71,72,93,96,97,98,100,117,134,135,138,154,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'arithmetic':([47,119,120,121,123,124,125,128,130,145,146,160,],[71,71,71,71,71,71,71,71,71,71,71,71,]),'operatorcomparator':([47,119,120,121,123,124,125,128,130,145,146,160,],[72,72,72,72,72,72,72,72,72,72,72,72,]),'operatorbittobit':([47,119,120,121,123,124,125,128,130,145,146,160,],[73,73,73,73,73,73,73,73,73,73,73,73,]),'bodyorstm':([50,133,136,155,161,165,],[94,144,147,162,164,166,]),'assign':([58,129,],[98,98,]),'unaryoperatorsufx':([58,129,],[99,99,]),'params':([100,138,],[126,148,]),'sigparams':([118,149,],[132,156,]),'brackets_expression':([131,],[141,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> class','program',1,'p_program','ExpressionLanguageSin.py',23),
  ('class -> visibility classmodifier CLASS ID EXTENDS ID LCHAV membros RCHAV','class',9,'p_class_extends','ExpressionLanguageSin.py',28),
  ('class -> visibility classmodifier CLASS ID LCHAV membros RCHAV','class',7,'p_class_default','ExpressionLanguageSin.py',32),
  ('class -> visibility classmodifier CLASS ID IMPLEMENTS LCHAV membros RCHAV','class',8,'p_class_implements','ExpressionLanguageSin.py',36),
  ('visibility -> PUBLIC','visibility',1,'p_visibility_public','ExpressionLanguageSin.py',41),
  ('visibility -> PRIVATE','visibility',1,'p_visibility_private','ExpressionLanguageSin.py',45),
  ('visibility -> PROTECTED','visibility',1,'p_visibility_protected','ExpressionLanguageSin.py',49),
  ('visibility -> <empty>','visibility',0,'p_visibility_default','ExpressionLanguageSin.py',53),
  ('classmodifier -> <empty>','classmodifier',0,'p_classmodifier_default','ExpressionLanguageSin.py',58),
  ('classmodifier -> ABSTRACT','classmodifier',1,'p_classmodifier_abstract','ExpressionLanguageSin.py',62),
  ('classmodifier -> FINAL','classmodifier',1,'p_classmodifier_final','ExpressionLanguageSin.py',66),
  ('classmodifier -> PACKAGE','classmodifier',1,'p_classmodifier_package','ExpressionLanguageSin.py',70),
  ('membros -> membro','membros',1,'p_membros','ExpressionLanguageSin.py',75),
  ('membros -> membro membros','membros',2,'p_multimembros','ExpressionLanguageSin.py',79),
  ('membro -> atribute','membro',1,'p_membro_atribute','ExpressionLanguageSin.py',83),
  ('membro -> function','membro',1,'p_membrofunction','ExpressionLanguageSin.py',87),
  ('atribute -> visibility atributemodifier type ID SEMICOLON','atribute',5,'p_atribute','ExpressionLanguageSin.py',92),
  ('atribute -> visibility atributemodifier type ID EQUAL ID SEMICOLON','atribute',7,'p_atribute_inicialized_ID','ExpressionLanguageSin.py',96),
  ('atribute -> visibility atributemodifier type ID EQUAL expression SEMICOLON','atribute',7,'p_atribute_inicialized_type','ExpressionLanguageSin.py',100),
  ('atributemodifier -> <empty>','atributemodifier',0,'p_atributemodifier_default','ExpressionLanguageSin.py',104),
  ('atributemodifier -> STATIC','atributemodifier',1,'p_atributemodifier_static','ExpressionLanguageSin.py',108),
  ('atributemodifier -> FINAL','atributemodifier',1,'p_atributemodifier_final','ExpressionLanguageSin.py',112),
  ('function -> signature body','function',2,'p_function','ExpressionLanguageSin.py',117),
  ('signature -> visibility atributemodifier type ID LPAREN sigparams RPAREN','signature',7,'p_signature','ExpressionLanguageSin.py',121),
  ('sigparams -> ID brackets_expression','sigparams',2,'p_sigparams_id','ExpressionLanguageSin.py',125),
  ('sigparams -> ID brackets_expression COMMA sigparams','sigparams',4,'p_sigparams_sigparams','ExpressionLanguageSin.py',129),
  ('body -> LCHAV stms RCHAV','body',3,'p_body','ExpressionLanguageSin.py',133),
  ('stms -> stm','stms',1,'p_stms','ExpressionLanguageSin.py',137),
  ('stms -> stm stms','stms',2,'p_multistms','ExpressionLanguageSin.py',141),
  ('stm -> expression SEMICOLON','stm',2,'p_stm_exp','ExpressionLanguageSin.py',146),
  ('stm -> WHILE LPAREN expression RPAREN bodyorstm','stm',5,'p_stm_while','ExpressionLanguageSin.py',150),
  ('stm -> DO bodyorstm WHILE LPAREN expression RPAREN SEMICOLON','stm',7,'p_stm_dowhile','ExpressionLanguageSin.py',154),
  ('stm -> FOR LPAREN expression SEMICOLON expression SEMICOLON expression SEMICOLON RPAREN bodyorstm','stm',10,'p_stm_for','ExpressionLanguageSin.py',158),
  ('stm -> IF LPAREN expression RPAREN bodyorstm','stm',5,'p_stm_if','ExpressionLanguageSin.py',162),
  ('stm -> IF LPAREN expression RPAREN bodyorstm ELSE bodyorstm','stm',7,'p_stm_ifelse','ExpressionLanguageSin.py',166),
  ('stm -> IF LPAREN expression RPAREN bodyorstm ELSE IF bodyorstm','stm',8,'p_stm_elseif','ExpressionLanguageSin.py',170),
  ('stm -> SEMICOLON','stm',1,'p_stm_semicollon','ExpressionLanguageSin.py',175),
  ('bodyorstm -> body','bodyorstm',1,'p_bodyorstm_body','ExpressionLanguageSin.py',181),
  ('expression -> operator','expression',1,'p_expression','ExpressionLanguageSin.py',187),
  ('expression -> call','expression',1,'p_expression_call','ExpressionLanguageSin.py',191),
  ('expression -> FLOAT_NUMBER','expression',1,'p_expression_FLOAT_NUMBER','ExpressionLanguageSin.py',195),
  ('expression -> INT_NUMBER','expression',1,'p_expression_INT_NUMBER','ExpressionLanguageSin.py',199),
  ('expression -> STRING','expression',1,'p_expression_STRING','ExpressionLanguageSin.py',203),
  ('expression -> ID','expression',1,'p_expression_ID','ExpressionLanguageSin.py',207),
  ('operator -> expression arithmetic expression','operator',3,'p_operator_arithmetic','ExpressionLanguageSin.py',212),
  ('operator -> ID assign expression','operator',3,'p_operator_assign','ExpressionLanguageSin.py',216),
  ('operator -> expression operatorcomparator expression','operator',3,'p_operator_operatorcomparator','ExpressionLanguageSin.py',220),
  ('operator -> unaryoperatorprefx ID','operator',2,'p_operator_unaryoperatorprefx','ExpressionLanguageSin.py',224),
  ('operator -> ID unaryoperatorsufx','operator',2,'p_operator_unaryoperatorsufx','ExpressionLanguageSin.py',228),
  ('operator -> expression operatorbittobit','operator',2,'p_operator_operatorbittobit','ExpressionLanguageSin.py',232),
  ('brackets_expression -> LBRACKET RBRACKET','brackets_expression',2,'p_brackets_expression','ExpressionLanguageSin.py',236),
  ('brackets_expression -> LBRACKET INT_NUMBER RBRACKET','brackets_expression',3,'p_brackets_expression','ExpressionLanguageSin.py',237),
  ('brackets_expression -> LBRACKET ID RBRACKET','brackets_expression',3,'p_brackets_expression','ExpressionLanguageSin.py',238),
  ('type -> primitivetypes','type',1,'p_type','ExpressionLanguageSin.py',243),
  ('primitivetypes -> TYPE_INT','primitivetypes',1,'p_primitivetypes','ExpressionLanguageSin.py',247),
  ('primitivetypes -> TYPE_FLOAT','primitivetypes',1,'p_primitivetypes','ExpressionLanguageSin.py',248),
  ('primitivetypes -> TYPE_DOUBLE','primitivetypes',1,'p_primitivetypes','ExpressionLanguageSin.py',249),
  ('primitivetypes -> TYPE_BYTE','primitivetypes',1,'p_primitivetypes','ExpressionLanguageSin.py',250),
  ('primitivetypes -> TYPE_BOOLEAN','primitivetypes',1,'p_primitivetypes','ExpressionLanguageSin.py',251),
  ('primitivetypes -> TYPE_CHAR','primitivetypes',1,'p_primitivetypes','ExpressionLanguageSin.py',252),
  ('primitivetypes -> TYPE_STRING','primitivetypes',1,'p_primitivetypes','ExpressionLanguageSin.py',253),
  ('primitivetypes -> TYPE_LONG','primitivetypes',1,'p_primitivetypes','ExpressionLanguageSin.py',254),
  ('primitivetypes -> TYPE_VOID','primitivetypes',1,'p_primitivetypes','ExpressionLanguageSin.py',255),
  ('arithmetic -> TIMES','arithmetic',1,'p_arithmetic','ExpressionLanguageSin.py',262),
  ('arithmetic -> DIVIDE','arithmetic',1,'p_arithmetic','ExpressionLanguageSin.py',263),
  ('arithmetic -> MODULE','arithmetic',1,'p_arithmetic','ExpressionLanguageSin.py',264),
  ('arithmetic -> PLUS','arithmetic',1,'p_arithmetic','ExpressionLanguageSin.py',265),
  ('arithmetic -> MINUS','arithmetic',1,'p_arithmetic','ExpressionLanguageSin.py',266),
  ('assign -> EQUAL','assign',1,'p_assign','ExpressionLanguageSin.py',272),
  ('assign -> MINUS_EQ','assign',1,'p_assign','ExpressionLanguageSin.py',273),
  ('assign -> TIMES_EQ','assign',1,'p_assign','ExpressionLanguageSin.py',274),
  ('assign -> PLUS_EQ','assign',1,'p_assign','ExpressionLanguageSin.py',275),
  ('assign -> DIVIDE_EQ','assign',1,'p_assign','ExpressionLanguageSin.py',276),
  ('assign -> MOD_EQ','assign',1,'p_assign','ExpressionLanguageSin.py',277),
  ('assign -> BITWISE_AND_EQ','assign',1,'p_assign','ExpressionLanguageSin.py',278),
  ('assign -> BITWISE_OR_EQ','assign',1,'p_assign','ExpressionLanguageSin.py',279),
  ('assign -> BITWISE_XOR_EQ','assign',1,'p_assign','ExpressionLanguageSin.py',280),
  ('assign -> URSHIFT_EQ','assign',1,'p_assign','ExpressionLanguageSin.py',281),
  ('assign -> LSHIFT_EQ','assign',1,'p_assign','ExpressionLanguageSin.py',282),
  ('assign -> RSHIFT_EQ','assign',1,'p_assign','ExpressionLanguageSin.py',283),
  ('operatorcomparator -> LEQ','operatorcomparator',1,'p_operatorcomparator','ExpressionLanguageSin.py',289),
  ('operatorcomparator -> GEQ','operatorcomparator',1,'p_operatorcomparator','ExpressionLanguageSin.py',290),
  ('operatorcomparator -> LT','operatorcomparator',1,'p_operatorcomparator','ExpressionLanguageSin.py',291),
  ('operatorcomparator -> GT','operatorcomparator',1,'p_operatorcomparator','ExpressionLanguageSin.py',292),
  ('operatorcomparator -> NEQ','operatorcomparator',1,'p_operatorcomparator','ExpressionLanguageSin.py',293),
  ('operatorcomparator -> EQ','operatorcomparator',1,'p_operatorcomparator','ExpressionLanguageSin.py',294),
  ('operatorcomparator -> AND','operatorcomparator',1,'p_operatorcomparator','ExpressionLanguageSin.py',295),
  ('operatorcomparator -> OR','operatorcomparator',1,'p_operatorcomparator','ExpressionLanguageSin.py',296),
  ('operatorcomparator -> BITWISE_AND','operatorcomparator',1,'p_operatorcomparator','ExpressionLanguageSin.py',297),
  ('operatorcomparator -> BITWISE_OR','operatorcomparator',1,'p_operatorcomparator','ExpressionLanguageSin.py',298),
  ('operatorcomparator -> BITWISE_XOR','operatorcomparator',1,'p_operatorcomparator','ExpressionLanguageSin.py',299),
  ('unaryoperatorprefx -> INCREMENT','unaryoperatorprefx',1,'p_unaryoperatorprefx','ExpressionLanguageSin.py',305),
  ('unaryoperatorprefx -> DECREMENT','unaryoperatorprefx',1,'p_unaryoperatorprefx','ExpressionLanguageSin.py',306),
  ('unaryoperatorprefx -> MINUS','unaryoperatorprefx',1,'p_unaryoperatorprefx','ExpressionLanguageSin.py',307),
  ('unaryoperatorprefx -> PLUS','unaryoperatorprefx',1,'p_unaryoperatorprefx','ExpressionLanguageSin.py',308),
  ('unaryoperatorprefx -> NOT','unaryoperatorprefx',1,'p_unaryoperatorprefx','ExpressionLanguageSin.py',309),
  ('unaryoperatorsufx -> INCREMENT','unaryoperatorsufx',1,'p_unaryoperatorsufx','ExpressionLanguageSin.py',314),
  ('unaryoperatorsufx -> DECREMENT','unaryoperatorsufx',1,'p_unaryoperatorsufx','ExpressionLanguageSin.py',315),
  ('operatorbittobit -> URSHIFT','operatorbittobit',1,'p_operatorbittobit','ExpressionLanguageSin.py',321),
  ('operatorbittobit -> LSHIFT','operatorbittobit',1,'p_operatorbittobit','ExpressionLanguageSin.py',322),
  ('operatorbittobit -> RSHIFT','operatorbittobit',1,'p_operatorbittobit','ExpressionLanguageSin.py',323),
  ('call -> ID LPAREN params RPAREN','call',4,'p_call','ExpressionLanguageSin.py',329),
  ('call -> ID LPAREN RPAREN','call',3,'p_call_default','ExpressionLanguageSin.py',333),
  ('params -> expression COMMA params','params',3,'p_params_multi','ExpressionLanguageSin.py',337),
  ('params -> expression','params',1,'p_params_unique','ExpressionLanguageSin.py',341),
]
