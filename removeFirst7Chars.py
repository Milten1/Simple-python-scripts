import sys

lista1 = open(sys.argv[1]).read() 
lista = lista1.splitlines()

f = open("new_cookies.txt", "a")

for line in lista:
    f.write(line[-32:] + "\n")

f.close()
