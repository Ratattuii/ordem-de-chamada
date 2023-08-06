N, K = map(int, input().split())

alunos = []

for _ in range(N):
    nome = input()
    alunos.append(nome)

alunos.sort()

ganhador = alunos[K - 1]

print("ganhador = ", ganhador)