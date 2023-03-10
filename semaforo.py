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

#Programa Principal

s1 = Semaforo('vermelho', 2)

for i in range(10):
    s1.mudarCor()
    time.sleep(s1.tempo)
