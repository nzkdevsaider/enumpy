from pathlib import Path

di = input("Introduce la ruta en la que quieres trabajar: ")

d = Path(di)

c = 0

mode = int(input("¿Qué quieres realizar en esta carpeta?\n[1] - Renombrar y enumerar archivos según extensión.\n[2] - Ver conteo del directorio\n"))

if(mode == 1):
	suff = input("¿Cuál es el sufijo del archivo que deseas enumerar?")
	for x in d.iterdir():
		if x.is_file():
			if x.suffix == suff:
				x.rename(str(c)+suff)
				c = c + 1

if(mode == 2):
	for x in d.iterdir():
		if x.is_file():
			print(x)
