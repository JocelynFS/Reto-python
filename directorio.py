from typing import Sized
# All your code goes here!!!print("Directorio de estudiantes de SKILLS FOR WOMEN IN TECH")
Directorio=[]
while True:
  print("1) Ingresar un nuevo registro.")
  print("2) Salir.")
  opcion=int(input("Digite una opción: "))
  if opcion==1:
    nombre=input("Escriba el nombre: ")
    edad=int(input("Digite la edad: "))
    temas=input("Escriba los temas en los que está interesad(o/a): ")
    if edad>=18:
      menordeedad="No"
    else:
      menordeedad="Si"
  
    Directorio.append({
      "Nombre": nombre,
      "Edad": edad,
      "Temas": temas,
      "Menor de edad": menordeedad
      })
  else:
    break

print("Estudiantes SKILLS FOR WOMEN IN TECH")
for i in range(len(Directorio)):
  print([i+1], end="")
  print(Directorio[i])