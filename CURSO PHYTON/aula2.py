faturamento = 1152
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento
margem_lucro = round(margem_lucro , 2)

print(f"o faturamento foi de R${faturamento:.2f} o custo foi de R${custo:.2f}  e o lucro foi de R${lucro:.2f} e a margem de lucro foi de {margem_lucro:.0
                                                                                                                                          ,%} ")

email_cliente = "rlemos1997@gmail.com"
email_cliente = email_cliente.lower()
print(email_cliente)

print(email_cliente.find("@"))

if email_cliente.find("@") == -1:
    print("Digite um e-mail valido")
else:
    print("acesso validado")

print(len(email_cliente))
print(email_cliente[:10])

novo_email= email_cliente.replace("rlemos1997" , "ricardolemos1997")
print(novo_email)

nome ="jose ricardo"
print(nome.title())

posicao_servidor = email_cliente.find("@")
servidor = email_cliente[0: posicao_servidor]
print(servidor)

primeiro_espaço = nome.find(" ")
primeiro_nome = nome[0:primeiro_espaço]
print(primeiro_nome.title())

segundo_nome = nome[primeiro_espaço + 1 :]
print(segundo_nome.title())