from abc import abstractmethod
from abc import ABC

# Gramática
# programa : listadecomandos
# listadecomandos : comando
#                | listadecomandos comando
# comando : VAR ID ATRIBUICAO expressao PONTOEVIRGULA
#         | ID ATRIBUICAO expressao PONTOEVIRGULA
#         | IF expressao THEN listadecomandos ELSE listadecomandos ENDIF
#         | WHILE expressao DO listadecomandos ENDWHILE
# expressao : expressao MAIS expressao
#                  | expressao MENOS expressao
#                  | expressao VEZES expressao
#                  | expressao DIVIDE expressao
#                  | ID
#                  | NUMERO


#Programa
class Programa():
    def __init__(self, listadecomandos):
        self.listadecomandos = listadecomandos
        
    @abstractmethod
    def print(self):
        self.listadecomandos.print()


#Listadecomandos
class Listadecomandos(ABC):
    @abstractmethod
    def print(self):
        pass


class UmComando(Listadecomandos):
    def __init__(self, comando):
        self.comando = comando
        
    def print(self):
        print('[UmComando]', end='')
        self.comando.print()


class MaisdeUmComando(Listadecomandos):
    def __init__(self, listadecomandos, comando):
        self.comando = comando
        self.listadecomandos = listadecomandos
        
    def print(self):
        print('[MaisdeUmComando', end='')
        self.comando.print()
        self.listadecomandos.print()


#Comando
class Comando(ABC):
    @abstractmethod
    def print(self):
        pass

class DeclaracaoVariavel(Comando):
    def __init__(self, ID, exp):
        self.ID = ID
        self.exp = exp
        
    def print(self):
        print('[DeclaracaoVariavel]', end='')
        self.exp.print()

class AtribuicaoVariavel(Comando):
    def __init__(self, ID, exp):
        self.ID = ID
        self.exp = exp
        
    def print(self):
        print('[AtribuicaoVariavel]')
        self.exp.print()


# Expressão
class Exp(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def print(self):
        print('[Expressao]', end='')


class ExpSoma(Exp):
    def __init__(self, exp1, exp2):
        super().__init__()
        self.exp1 = exp1
        self.exp2 = exp2

    def print(self):
        print('[ExpressaoSoma]', end='')
        self.exp1.print()
        self.exp2.print()


class ExpSubt(Exp):
    def __init__(self, exp1, exp2):
        super().__init__()
        self.exp1 = exp1
        self.exp2 = exp2

    def print(self):
        print('[ExpressãoSubtração]', end='')
        self.exp1.print()
        self.exp2.print()


class ExpMulti(Exp):
    def __init__(self, exp1, exp2):
        super().__init__()
        self.exp1 = exp1
        self.exp2 = exp2

    def print(self):
        print('[ExpressãoMultiplicação]', end='')
        self.exp1.print()
        self.exp2.print()


class ExpDivisao(Exp):
    def __init__(self, exp1, exp2):
        super().__init__()
        self.exp1 = exp1
        self.exp2 = exp2

    def print(self):
        print('[ExpressãoDivisao]', end='')
        self.exp1.print()
        self.exp2.print()


class ExpId(Exp):
    def __init__(self, ID):
        super().__init__()
        self.ID = ID

    def print(self):
        print('[ExpressãoId]', end='')

class ExpNumero(Exp):
    def __init__(self, numero):
        self.numero = numero

    def print(self):
        print('[ExpressãoNumero]', end='')
        
        
class ComandoIfElse(Comando):
    def __init__(self, exp, lista_de_comandos_if, lista_de_comandos_else):
        self.exp = exp
        self.lista_de_comandos_if = lista_de_comandos_if
        self.lista_de_comandos_else = lista_de_comandos_else

    def print(self):
        print('[ComandoIfElse]', end='')
        self.exp.print()
        self.lista_de_comandos_if.print()
        self.lista_de_comandos_else.print()


class ComandoWhile(Comando):
    def __init__(self, exp, lista_de_comandos):
        self.exp = exp
        self.lista_de_comandos = lista_de_comandos

    def print(self):
        print('[ComandoWhile]', end='')
        self.exp.print()
        self.lista_de_comandos.print()
