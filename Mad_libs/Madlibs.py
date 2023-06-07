print("A continuación se presenta una Madlibs, por favor digita las palabras solicitadas para generar la historia")

Nombre=str(input("Nombre: "))
SustantivoUno=str(input("Sustantivo masculino: "))
VerboUno=str(input("Verbo 1: "))
NumeroUno=int(input("Número entero mayor a uno:"))
Profesion=str(input("Profesión:"))
Vocal=str(input("Vocal: "))

MadLib=f"Crear historias interesantes es realmente complejo, sin embargo, a {Nombre} le era muy sencillo \
puesto que tenía aquel {SustantivoUno} que le gustaba tanto, decía que eso hacia que fuera excelente haciendo \
historias,sin embargo, el {VerboUno} lo ha llevado {NumeroUno} o más a veces distraerse de su objetivo.\
Pero bueno a pesar de este hecho ha logrado conversirse en {Profesion} con su risa característica \
j{Vocal}j{Vocal}j{Vocal}j{Vocal}."

print(MadLib)