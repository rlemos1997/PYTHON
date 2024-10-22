import math

ang = int(input("Digite um angulo "))

seno = math.sin(math.radians(ang))

cos = math.cos(math.radians(ang))

tan = math.tan(math.radians(ang))

print(f"O seno de {ang} e {seno:.2f}, o coseno é de {cos:.2f} e a tangente é de {tan:.2f}")