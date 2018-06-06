# -*- coding: UTF-8 -*-

class Perfil(object):
	'Classe padrão para perfis de usuários'

	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0

	def imprimir(self):
		print 'Nome: %s, Telefone: %s, Empresa %s' % (self.nome, self.telefone, self.empresa)

	def curtir(self):
		self.__curtidas+=1

	def obter_curtidas(self):
		return self.__curtidas

	#@staticmethod
	@classmethod
	def gerar_perfis(classe, nome_arquivo):
		arquivo = open(nome_arquivo, 'r')
		perfis = []
		for linha in arquivo:
			valores = linha.split(',')
			if(len(valores) is not 3):
				raise ValueError('Uma linha no arquivo %s deve ter 3 valores' % nome_arquivo)
			perfis.append(classe(*valores))
		arquivo.close()
		return perfis

class Perfil_Vip(Perfil):
	'Classe padrão para perfis de usuários vips'

	def __init__(self, nome, telefone, empresa, apelido=''):
		super(Perfil_Vip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def obter_creditos(self):
		return super(Perfil_Vip, self).obter_curtidas() * 10.0


class Data(object):
	'Classe para impressão de Data'

	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def imprime(self):
		print '%s/%s/%s' % (self.dia, self.mes, self.ano)

class Pessoa(object):
	'Classe padrão para pessoa e calculo do IMC'

	def __init__(self, nome, massa, altura):
		self.nome = nome
		self.massa = float(massa)
		self.altura = float(altura)
		
	def imprime(self):
		imc = self.massa / (self.altura **2)
		print 'IMC de %s: %s' % (self.nome, imc)