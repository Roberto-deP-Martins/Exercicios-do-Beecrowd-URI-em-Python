segundos = int(input())
# Segundos para minutos
minutos = segundos // 60
resto = segundos % 60
#Se resto é zero, há um número exato de minutos, logo, não há segundos sobrando
if resto == 0:
    segundos = 0
# Remove os minutos (em segundo) do total de segundos
elif minutos > 0:
    segundos -= minutos * 60

# Minutos para segundos
horas = minutos // 60
resto = minutos % 60
#Se resto é zero, há um número exato de horas, logo, não há minutos sobrando
if resto == 0:
    minutos = 0
# Remove as horas (em segundo) do total de minutos
elif horas > 0:
    minutos -= horas * 60

print('{}:{}:{}'.format(horas, minutos, segundos))