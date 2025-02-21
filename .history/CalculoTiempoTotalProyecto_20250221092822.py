a=int(input("Informe los días que requiere para la actividad A: "))
b=int(input("Informe los días que requiere para la actividad B: "))
c=int(input("Informe los días que requiere para la actividad C: "))

if a>0 and b>0 and c >0:
    suma=a+b+c
    resultado=print("El total de días del proyecto es de", suma)
else:
    print("Los días nos pueden ser negativos, por favor revísalos nuevamente")