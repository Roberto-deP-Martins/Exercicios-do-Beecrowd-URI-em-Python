numCaso = 1  # Número de casos já produzidos
for i in range(int(input())):
    sheldon, raj = input().split()  # Pega a escolha de cada um
    if sheldon == raj:  # Empate
        print(f'Caso #{numCaso}: De novo!')
    elif sheldon == 'tesoura':
        if raj == 'papel' or raj == 'lagarto':  # Vitória de Sheldon
            print(f'Caso #{numCaso}: Bazinga!')
        else:
            print(f'Caso #{numCaso}: Raj trapaceou!')
    elif sheldon == 'papel':
        if raj == 'pedra' or raj == 'Spock':  # Vitória de Sheldon
            print(f'Caso #{numCaso}: Bazinga!')
        else:
            print(f'Caso #{numCaso}: Raj trapaceou!')
    elif sheldon == 'pedra':
        if raj == 'lagarto' or raj == 'tesoura':  # Vitória de Sheldon
            print(f'Caso #{numCaso}: Bazinga!')
        else:
            print(f'Caso #{numCaso}: Raj trapaceou!')
    elif sheldon == 'lagarto':
        if raj == 'Spock' or raj == 'papel':  # Vitória de Sheldon
            print(f'Caso #{numCaso}: Bazinga!')
        else:
            print(f'Caso #{numCaso}: Raj trapaceou!')
    elif sheldon == 'Spock':
        if raj == 'tesoura' or raj == 'pedra':  # Vitória de Sheldon
            print(f'Caso #{numCaso}: Bazinga!')
        else:
            print(f'Caso #{numCaso}: Raj trapaceou!')
    numCaso += 1
