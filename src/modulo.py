#!/usr/bin/python
#!encoding: UTF-8

import sys
import math

PI35DT = 3.1415926535897931159979634685441852

#Utilizacion de una funcion calcular_xi para obtener los xi
def calcular_xi (n, i):
  xi = (i - 1.0/2.0) / n
  return xi
  
#Esta funcion es para calcular los 35 decimales, a su vez llama a la funcion arccot
def decimales_pi(digits):
  unity = 10**(digits + 10)
  decimal_pi = 4 *(8*arccot(5, unity) - arccot(239, unity))
  return (float(decimal_pi // 10**10) / 10 **digits)

def calcular_pi (n):
  #  PI35 = 3.1415926535897931159979634685441852
  sumatorio = 0.0
  ini = 0
  intervalos = 1.0 / float (n)
  for i in range(n):
    x_i = ((i+1) - 1.0/2.0) / n
#   x_i = calcular_xi (n, i+1)
    fx_i = 4.0 /(1.0 + x_i * x_i)
    ini += intervalos
    sumatorio += fx_i
  valor_pi = sumatorio / n
  return (valor_pi)
  
  
#Programa principal
#Ojo, para hacer uso de la funcion sys, debemos incluirla al principio deñ programa

if (__name__ == "__main__"):
  argumentos = sys.argv[1:]
  print argumentos
  if (len(argumentos) == 2):
    n = int (argumentos[0])
    aproximaciones = int (argumentos[1])
  else:
    print "Introduzca el nº de intervalos(n>0):"
    n = int (raw_input());
    print "Introduce el nº de aproximaciones:"
    aproximaciones = int (raw_input());
  if(n>0):
    intervalo = n
    lista = []
    for i in range (aproximaciones):
      valor = calcular_pi (intervalo)
      lista.append (valor)
      intervalo += n
    print lista
    diferencia = []
    for i in range (aproximaciones):
      dif = abs (PI35DT - lista[i])
      diferencia.append (dif)
    print "i\tPI35DT\tlista i\tPI35DT - lista i"
    for i in range (aproximaciones):
      print "%d\t%1.10f\t%1.10f\t%1.10f" %(i+1, PI35DT, lista[i], diferencia[i])
  else:
    print "El valor de los intervalos debe ser mayor que 0"