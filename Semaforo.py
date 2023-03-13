import time

class Semaforo:
    def __init__(self, cor, tempo):
        self.cor = cor
        self.tempo = tempo
    
    def mudarCor(self):
        if self.cor == 'vermelho':
            self.cor = 'verde'
        elif self.cor == 'verde':
            self.cor = 'amarelo'
        else:
            self.cor = 'vermelho'
        print(f'O semáforo está {self.cor}')

    def mudarTempo(self, novoTempo):
        self.tempo = novoTempo
        print(f'O tempo de transição mudou para {self.tempo} segundos.')

#Programa Principal

s1 = Semaforo('vermelho', 5)

for i in range(5):
    for i in range(s1.tempo):
        print(i)
        time.sleep(1)
    s1.mudarCor()

s1.mudarTempo(3)

for i in range(5):
    for i in range(s1.tempo):
        print(i)
        time.sleep(1)
    s1.mudarCor()