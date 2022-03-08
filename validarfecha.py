#Ejemplo 5
mestipo1=['Abril', 'Julio', 'Septiembre', 'Noviembre']
mestipo2=['Enero', 'Marzo', 'Mayo', 'Junio', 'Agosto', 'Octubre', 'Diciembre']
mestipo3=['Febrero']

def DiasDelMes(mes):
  if mes in mestipo1:
    diasmes=30
  elif mes in mestipo2:
    diasmes=31
  elif mes in mestipo3:
    diasmes=28
  else:
    print('Mes incorrecto')
    diasmes=0
  return diasmes

def ValidarFecha(dia,mes,año):
  diasmes=DiasDelMes(mes)
  if dia>1 and dia<diasmes:
    print('La fecha: '+ str(dia) + ' de ' + mes + ' de ' + año + ' es válida')
  else:
    print('La fecha: '+ str(dia) + ' de ' + mes  + ' de ' + año + ' no es válida')

print('Ingrese una fecha.')
dia=int(input('Dia: '))
mes=input('Mes: ')
año=input('Año: ')
Validar=ValidarFecha(dia,mes,año)