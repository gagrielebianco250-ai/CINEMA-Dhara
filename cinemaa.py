totalSeçao1 = 20
totalSeçao2 = 20
totalSeçao3 = 20

print("=🎥=CINEMA=🍿=")

while True:
    print("1 - Vingadores: Doutor Destino | 2h45 | 25,00")
    print("2 - Os Farofeiros 3 | 1h42 | 20,00")
    print("3 - O Gatola Da Cartola | 1h31 | 20,00")
    
    filme = int(input("Escolha um filme: "))
    
    if filme == 1:
        ingresso1 = int(input("Quantidades de ingressos: "))
        if ingresso1 > 0 and ingresso1 <= 20:
            totalSeçao1 -= ingresso1
            print(f"Compra realizada com sucesso! Quantidade disponivel de ingressos para o filme 'Vingadores: Doutor Destino': {totalSeçao1} unidades")
        else:
            print("Ingressos esgotados")
        
    elif filme == 2:
        ingresso2 = int(input("Quantidades de ingressos: "))
        if ingresso2 > 0 and ingresso2 <= 20:
            totalSeçao2 -= ingresso2
            print(f"Compra realizada com sucesso! Quantidade disponivel de ingressos para o filme 'Os Farofeiros 3': {totalSeçao2} unidades")
        else:
            print("Ingressos esgotados")
            
    elif filme == 3:
        ingresso3 = int(input("Quantidades de ingressos: "))
        if ingresso3 > 0 and ingresso3 <= 20:
            totalSeçao3 -= ingresso3
            print(f"Compra realizada com sucesso! Quantidade disponivel de ingressos para o filme 'O Gatola Da Cartola': {totalSeçao3} unidades")
        else:
            print("Ingressos esgotados")
    else:
        ("Não é uma opção!")