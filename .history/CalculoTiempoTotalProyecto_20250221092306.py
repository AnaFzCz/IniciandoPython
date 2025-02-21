a=int(input("Informe los días que requiere para la actividad A: "))
b=int(input("Informe los días que requiere para la actividad B: "))
c=int(input("Informe los días que requiere para la actividad C: "))

if a and b and c >0:
    resultado=print("El total de días del proyecto es de", sum(a,b,c))
else:
    print("Los días nos pueden ser negativos, por favor revísalos nuevamente")