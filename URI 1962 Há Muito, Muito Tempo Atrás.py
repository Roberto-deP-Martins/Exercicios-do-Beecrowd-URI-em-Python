for i in range(int(input())):
    anos_transcorridos = int(input())
    if anos_transcorridos >= 2015:
        print(f"{anos_transcorridos - 2015 + 1} A.C.")
    else:
        print(f"{2015 - anos_transcorridos} D.C.")