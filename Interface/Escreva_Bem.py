import pygame

pygame.init()
pygame.mixer.init()
print("=====ESCREVA BEM=====")

cont = 0
resposta_correta = 0
resposta_errada = 0

print()

print('Estou com fome, irei ...\n[1] Almoçar\n[2] Aumoçar\n[3] Almossar\n[4] Aumossar')
r1 = int(input('Sua resposta: '))

if r1 == 1:
    pygame.mixer.music.load('sons/correto.wav')
    pygame.mixer.music.play()
    print('Resposta correta! +10 pontos!')
    cont += 10
    resposta_correta += 1

elif r1 == 2 or r1 == 3 or r1 == 4:
    pygame.mixer.music.load('sons/errado.wav')
    pygame.mixer.music.play()
    cont += 0
    resposta_errada += 1
    print('Resposta incorreta!')

else:
    print('Digite apenas números entre 1 e 4!')


print()

print('Irei contatar meu...\n[1] Adevogado\n[2] Advogado\n[3] Adivogado\n[4] Adivogadu')
r2 = int(input('Sua resposta: '))

if r2 == 2:
    pygame.mixer.music.load('sons/correto.wav')
    pygame.mixer.music.play()
    cont += 10
    resposta_correta += 1
    print('Resposta correta! +10 pontos!')

elif r2 == 1 or r2 == 3 or r2 == 4:
    pygame.mixer.music.load('sons/errado.wav')
    pygame.mixer.music.play()
    cont += 0
    resposta_errada += 1
    print('Resposta incorreta!')

else:
    print('Digite apenas números entre 1 e 4!')
    print(r2)

print()

print('Comprei 200 gramas de...\n[1] Mortandela\n[2] Mortadela\n[3] Mortadella\n[4] Motadella')
r3 = int(input('Sua resposta: '))

if r3 == 2:
    pygame.mixer.music.load('sons/correto.wav')
    pygame.mixer.music.play()
    cont += 10
    resposta_correta += 1
    print('Resposta correta! +10 pontos!')


elif r3 == 1 or r3 == 3:
    pygame.mixer.music.load('sons/errado.wav')
    pygame.mixer.music.play()
    cont += 0
    resposta_errada += 1
    print('Resposta incorreta!')

else:
    print('Digite apenas números entre 1 e 4!')

print('É sempre um ... recebê-lo(a) em minha casa!\n[1] Prasê\n[2] Praser\n[3] Prazê\n[4] Prazer')
r4 = int(input('Sua resposta: '))

print()

if r4 == 4:
    pygame.mixer.music.load('sons/correto.wav')
    pygame.mixer.music.play()
    cont += 10
    resposta_correta += 1
    print('Resposta correta! +10 pontos!')

elif r4 == 1 or r4 == 2 or r4 == 3:
    pygame.mixer.music.load('sons/errado.wav')
    pygame.mixer.music.play()
    cont += 0
    resposta_errada += 1
    print('Resposta incorreta!')

else:
    print('Digite apenas números entre 1 e 4!')

print()

print('Você obteve no total {} pontos!'.format(cont))
print('Acertou {} perguntas e errou {}.'.format(resposta_correta, resposta_errada))
pygame.event.wait()



