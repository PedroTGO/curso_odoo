class Coche:

	def __init__(self,gasolina):
		self.gasolina=gasolina
		print "Tenemos "+str(self.gasolina)+" litros"
	def arrancar(self):
		if self.gasolina>0:
			print "Arranca"
		else:
			print "No Arranca"
	def conducir(self):
		if self.gasolina > 0:
			self.gasolina-=1
			print "Quedan "+str(self.gasolina)+" litros"
		else:
			print "No se mueve"



