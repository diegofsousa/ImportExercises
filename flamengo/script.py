def call_flamengo():
	print("Flamengo foi importado")

try:
	from basquete import situacao
	situacao.resultados()
except ImportError as e:
	print("Importação 'from basquete import situacao' é inválida para este caso.")
