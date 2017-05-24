import numpy as np
import matplotlib.pyplot as plt

def drawCircle(centro,radio):
	t = np.linspace(0,2*np.pi,360)
	R = radio
	h = centro.real
	k = centro.imag
	x = R*np.cos(t) + h
	y = R*np.sin(t) + k
	plt.plot(x,y)


def circlesGershgorim(A):
	(r,c) = A.shape
	for i in range(r):
		s = 0
		for j in range(c):
			if i!=j:
				s += abs(A[i,j])
		drawCircle(A[i,i],s)


def drawAutoValores(A):
	autovalores = np.linalg.eig(A)
	# print autovalores[0] # autovalores
	# print autovalores[1] # autovectores
	n = len(autovalores[0])
	print("\nAutovalores:");
	for i in range(n):
		print(autovalores[0][i])
		c = autovalores[0][i]
		plt.plot(c.real,c.imag,'o')
		# print c.imag


print("Ingrese tamaño de la matríz: ");
n = int(input())

limitRadio = 30.0
xlimit = 10.0
ylimit = 10.0
A = np.zeros([n,n])
B = np.zeros([n,n])
for i in range(n):	#Generación de números aleatorios
	x = np.random.random()*2*xlimit-xlimit
	y = np.random.random()*2*ylimit-ylimit
	for j in range(n):
		if j == i:
			m = 4
		else:
			m = 1
		A[i,j] = x + np.random.random()*2*m*limitRadio-m*limitRadio
		B[i,j] = y + np.random.random()*2*m*limitRadio-m*limitRadio


B = B*1j #Pasando la matriz B a valores complejos
C = A+B #C = a+bi

print (C)

drawAutoValores(C)
circlesGershgorim(C)
plt.show()








