# Valor requisitado e sua impressão
n = float(input()) + 0.001
print("NOTAS:")
# Notas de 100
notasDe100 = n // 100
print(int(notasDe100), "nota(s) de R$ 100.00")
restoN100 = n % 100

# Notas de 50
notasDe50 = float(restoN100) // 50
print(int(notasDe50), "nota(s) de R$ 50.00")
restoN50 = restoN100 % 50

# Notas de 20
notasDe20 = float(restoN50) // 20
print(int(notasDe20), "nota(s) de R$ 20.00")
restoN20 = restoN50 % 20

# Notas de 10
notasDe10 = float(restoN20) // 10
print(int(notasDe10), "nota(s) de R$ 10.00")
restoN10 = restoN20 % 10

# Notas de 5
notasDe5 = float(restoN10) // 5
print(int(notasDe5), "nota(s) de R$ 5.00")
restoN5 = restoN10 % 5

# Notas de 2
notasDe2 = float(restoN5) // 2
print(int(notasDe2), "nota(s) de R$ 2.00")
restoN2 = restoN5 % 2

print("MOEDAS:")

# Moedas de 1
moedasDe1 = float(restoN2) // 1
print(int(moedasDe1), "moeda(s) de R$ 1.00")
restoN1 = restoN2 % 1

# Moedas de 0.50
moedas50Centavos = float(restoN1) // 0.5
print(int(moedas50Centavos), "moeda(s) de R$ 0.50")
restoN50Centavos = restoN1 % 0.5

# Moedas de 0.25
moedas25Centavos = float(restoN50Centavos) // 0.25
print(int(moedas25Centavos), "moeda(s) de R$ 0.25")
restoN25Centavos = restoN50Centavos % 0.25

# Moedas de 0.10
moedas10Centavos = float(restoN25Centavos) // 0.1
print(int(moedas10Centavos), "moeda(s) de R$ 0.10")
restoN10Centavos = restoN25Centavos % 0.1

# Moedas de 0.05
moedas05Centavos = float(restoN10Centavos) // 0.05
print(int(moedas05Centavos), "moeda(s) de R$ 0.05")
restoN05Centavos = restoN10Centavos % 0.05

# Moedas de 0.01
moedas01Centavos = float(restoN05Centavos) // 0.01
print(int(moedas01Centavos), "moeda(s) de R$ 0.01")