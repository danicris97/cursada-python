import clsFigurasGeometricas
import random

rectangulo=clsFigurasGeometricas.clsRectangulo(random.randint(1,10),random.randint(1,10))
print("rectangulo: lado a= " + str(rectangulo.getLadoA()) + " lado b= " + str(rectangulo.getLadoB()))
cuadrado=clsFigurasGeometricas.clsCuadrado(random.randint(1,10))
print("cuadrado: lado= " + str(cuadrado.getLadoA()))
triangulo=clsFigurasGeometricas.clsTriagulo(random.randint(1,10),random.randint(1,10),random.randint(1,10))
print("triangulo: lado a= " + str(triangulo.getLadoA()) + " lado b= " + str(triangulo.getLadoB()) + " lado c= " + str(triangulo.getLadoC()))
circulo=clsFigurasGeometricas.clsCirculo(random.randint(1,10))
print("circulo: radio= " + str(circulo.getRadio()))
print("")

lista=[rectangulo,cuadrado,triangulo,circulo]

for i in range(len(lista)):
    print("PERIMETRO DEL " + str(type(lista[i]).__name__) + " ES: " + str(lista[i].calculaPerimetro()))
    print("AREA DEL " + str(type(lista[i]).__name__) + " ES: " + str(lista[i].calculaArea()))
    print("")