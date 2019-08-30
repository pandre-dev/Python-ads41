import unittest
from Ex1_maioridade import Pessoa
from Ex2_numextenso import getNumero, getExtensao
from Ex3_calculadora import Calculadora
from Ex4_desconto import calcula_valor
from Ex5_positivonegativo import checar_sinal

class TesteMaioridade(unittest.TestCase):

    def testeMaioridade(self):
        pessoa = Pessoa(15)
        result = pessoa.checarMaioridade()
        self.assertEqual(result, False)

class TesteNumExtenso(unittest.TestCase):

    def testeNumExtenso(self):
        result = getExtensao(1).lower()
        self.assertEqual(result, "um")

class TesteCalculadora(unittest.TestCase):
    calc = Calculadora()
    
    def testeCalculadora(self):
        soma = self.calc.soma(2.33, 3.67)
        self.assertEqual(round(soma), 6.0)

        sub = self.calc.subtracao(8, 3)
        self.assertEqual(round(sub), 5)

        mult = self.calc.multiplicacao(8, 3)
        self.assertEqual(round(mult), 24)

        div = self.calc.divisao(4, 2)
        self.assertEqual(round(div), 2)
    
class TesteTroco(unittest.TestCase):
    def testeTroco(self):
        troco = calcula_valor(10.5, 7.3)
        self.assertEqual(round(troco, 2), 3.2)

class TesteSinal(unittest.TestCase):
    def testeSinal(self):
        result = checar_sinal(0)
        self.assertEqual(result, True)