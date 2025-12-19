for i in range(100):
	if i == 99:
		raise ValueError("Teste do stderr!")
	print(i)
