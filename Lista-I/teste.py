import unittest
from Ex1_maioridade import Pessoa
from Ex2_numextenso import getNumero, getExtensao
from Ex3_calculadora import Calculadora
from Ex4_desconto import calcula_valor
from Ex5_positivonegativo import checar_sinal
from Ex6_sinaleparidade import checar_sinal, checar_paridade
from Ex7_10numeros import *
from Ex8_10python import *
from Ex9_repetirfrase import *
from Ex10_aprovado import aprovacao
from Ex11_antecessor import antecessor
from Ex12_printmaior import *

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

class TesteSinalParidade(unittest.TestCase):
    def testeSinal(self):
        sinal = checar_sinal(-1);
        self.assertEqual(sinal, False)
        
    def testeParidade(self):
        paridade = checar_paridade(3);
        self.assertEqual(paridade, False)

class TesteListNumeros(unittest.TestCase):
    numeros = [2, 5, 8, 3, 4]

    def testeListNumeros(self):
        maior = achar_maior(self.numeros)
        self.assertEqual(maior, 8)

        menor = achar_menor(self.numeros)
        self.assertEqual(menor, 2)

        sm = soma(self.numeros)
        self.assertEqual(sm, 22)

        md = media(self.numeros)
        self.assertEqual(md, 4.4)

class TestePrintPython(unittest.TestCase):
    def testePrintPython(self):
        result = checar_palavra(lista_python(), "python")
        self.assertEqual(result, True)

class TesteRepetirPalavra(unittest.TestCase):
    def testeRepetirPalavra(self):
        result = repetir_palavra(5, "teste")
        self.assertEqual(result, ["teste" for i in range(5)])

class TesteAprovado(unittest.TestCase):
    def testeAprovado(self):
        result = aprovacao(5, 6, 7)
        self.assertEqual(result, False)

class TesteAntecessor(unittest.TestCase):
    def testeAntecessor(self):
        result = antecessor(10)
        self.assertEqual(result, 9)


class TesteMostrarMaio(unittest.TestCase):
    def testeMostrarMaior(self):
        result = maior_valor(10, 9)
        self.assertEqual(result, 10)