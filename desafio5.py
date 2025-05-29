nomes = []
print("Digite 10 nomes, um por vez:")

for i in range(10):
    while True:
        nome = input(f"Digite o {i+1}º nome: ").strip()
        
       
        if not all(c.isalpha() or c.isspace() for c in nome):
            print("Erro: Nome contém caracteres inválidos. Use apenas letras e espaços.")
            exit()  
        elif not nome:  
            print("Erro: Nome não pode estar vazio.")
        else:
            nomes.append(nome.title())  
            break


nomes_ordenados = sorted(nomes)


print("\nNomes ordenados alfabeticamente com suas quantidades de letras:")
for nome in nomes_ordenados:
    qtd_letras = len([c for c in nome if c.isalpha()])  
    print(f"{nome} - {qtd_letras} letras")
