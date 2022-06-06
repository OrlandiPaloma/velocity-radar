'''
velocidade_maxima = 80
Input velocidade_usuario
if velocidade_usuario <= velocidade_maxima
  print("não houve multa")
elif velocidade_usuario > velocidade_maxima e velocidad_usuario <= velocidade_maxima+10
  print("levou multa leve")
elif velocidade_usuário > velocidade_maxima+11 e velocidade_usuario <= velocidade_maxima+20
  print("levou multa grave")
elif velocidade_usuario > velocidade_maxima+20
  print("levou multa gravissima")
'''

velocidade_maxima = 80
velocidade = False
while velocidade == False:
  velocidade_usuario = int(input("Digite a velocidade: "))
  if velocidade_usuario <= velocidade_maxima:
    print("não houve multa")
  elif velocidade_usuario > velocidade_maxima and velocidade_usuario <= velocidade_maxima + 10:
    print("levou multa leve")
  elif velocidade_usuario >= velocidade_maxima + 11 and velocidade_usuario <= velocidade_maxima + 20:
    print("levou multa grave")
  elif velocidade_usuario > velocidade_maxima + 20:
    velocidade = True
    print("levou multa gravissima")