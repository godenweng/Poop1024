a1 = 5
a2 = 5.0
a3 = 1 + 5j
print(type(a1), type(a2), type(a3))
print(a3.real)
print(a3.imag)
print(a3 + a3, a3 - a3, a3 * a3)
print(abs(a3))
print((a3.real ** 2 + a3.imag ** 2) ** 0.5)
print(a3.conjugate())
# round
print(round(1.1),round(2.1),round(3.1),round(4.1))
print(round(1.4),round(2.4),round(3.4),round(4.4))
print(round(1.5),round(2.5),round(3.5),round(4.5))
print(round(5.5),round(6.5),round(7.5),round(8.5))
print(round(1.6),round(2.6),round(3.6),round(4.6))
print(round(1.7),round(2.7),round(3.7),round(4.7))