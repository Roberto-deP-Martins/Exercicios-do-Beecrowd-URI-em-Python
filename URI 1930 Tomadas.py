t1, t2, t3, t4 = map(int, input().split())
# As primeiras três réguas perdem uma tomada para a conexão da régua seguinte, a última não perde
t1 -= 1
t2 -= 1
t3 -= 1
print(t1 + t2 + t3 + t4)