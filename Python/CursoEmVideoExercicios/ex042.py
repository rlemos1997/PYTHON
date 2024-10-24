l1 = float(input("primeiro segmento: "))
l2 = float(input("Segundo segmento: "))
l3 = float(input("Terceiro segmento: "))

if l1 + l2 < l3:
    print("Esses segmentos nao formam um triangulo")
elif l1 == l2:
    print("Esse segmentos formam um triangulo RETANGULO")
elif l1 != l2 != l3:
    print("Esses segmentos formam um triangulo ISOSCELES")
elif l1 == l2 == l3:
    print("Esses segmentos formam um triangulo EQUILATERO")

    