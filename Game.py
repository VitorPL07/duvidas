from random import choice
import time

plv = ["carro", "casa", "cachorro", "capacete", "espelho", "porta", "cama", "cadeira", "chinelo", "quadro", "gato", "mesa", "fechadura", "toalha", "televisao", "paralelepipedo", "ventilador", "apaixonado", "desesperado", "varal", "cabide", "colher", "celular", "abajur", "caixa", "escova", "laranja", "sapato", "sabonete", "pente", "janela", "mochila", "mapa", "caminhao", "arroz", "cavalo", "grampeador", "camisa", "escritorio", "caderno", "biblioteca", "discoteca", "perfume", "desodorante", "livro"]

# Escolher uma palavra aleatória
sortear = choice(plv)
tentativas = 5
plv_esc = "_" * len(sortear)
plv_esc = list(plv_esc)

# Introdução
print("-=-" * 12)
print("JOGO DA FORCA".center(35))
print("-=-" * 12)

print(f"\n\033[1;34mVOCÊ TEM \033[1;33m{tentativas}\033[1;34m TENTATIVAS!\033[m\n")

letras_usadas = []

# Contador de segundos
tempo = 0
while True:
	time.sleep(1)
	tempo += 1

# Programa principal
while True:
	print(" ".join(plv_esc))
	chute = input("\nDigite uma letra: ").lower()
	if chute in sortear:
		for num, c in enumerate(sortear):
			if chute == c:
				plv_esc[num] = sortear[num]
				
	else:
		tentativas -= 1
		print(f"\n\033[1;34mVOCÊ TEM \033[1;33m{tentativas}\033[1;34m TENTATIVAS!\033[m\n")
		
	if tentativas == 0:
		print("\nVocê perdeu...")
		print(f"A palavra era \033[1;33m{sortear}\033[m")
		break
		
	if "_" not in plv_esc:
		print(" ".join(plv_esc))
		print("\n\n\033[1;35mPARABENS, VOCÊ GANHOU!!!\033[m")
		print(f"Seu tempo: {tempo}segundos.")
		break
		
	if chute in letras_usadas:
		print("\n\033[1;36mNÃO PODE USAR A MESMA LETRA MAIS DE UMA VEZ!!\033[m\n")
		
	letras_usadas.append(chute)
