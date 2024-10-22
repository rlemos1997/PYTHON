palavra = input("Digite uma palavra")

print(f"o tipo primitivo desse valor é:",type(palavra)) #QUAL TIPO 
print(f"Tem somente espaços?", palavra.isspace()) #SOMENTE ESPAÇO?
print(f"É um numero?", palavra.isnumeric()) 
print(f"é alfabetico?", palavra.isalpha())
print(f"é alfanumerico?", palavra.isalnum())



