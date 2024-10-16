lista_notas = []
for nota in range(5):
    nota = int(input("digite a nota do aluno "))
    lista_notas.append(nota)
print(lista_notas)

total_alunos = len(lista_notas)
print(total_alunos)

soma_notas = sum(lista_notas)
print(f"A soma das notas é:{soma_notas:.2f}")

media_notas = soma_notas / total_alunos
print(f"A media das notas é: {media_notas:.2f}")
 
media_acima = 70
for nota in lista_notas:
    if nota >= media_acima:
        print(f"Acima da média:{nota:.2f}")
    else:
        print(f"abaixo da média:{nota:.2f}")
    




#media_notas = lista_notas / total_notas
#print(media_notas)