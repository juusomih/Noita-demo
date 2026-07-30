import pygame,numpy
global pikselit
pygame.init()
naytto = pygame.display.set_mode((640, 480))
pikselit = pygame.PixelArray(naytto)
arr = pygame.surfarray.pixels2d(naytto)
kello = pygame.time.Clock()

lista = []
clock = pygame.time.Clock()
class Vesi:

    def __init__(self, x,y) -> None:
        self.color = (0,0,250)
        self.x = x
        self.y = y

    def piirra(self):
        pikselit[self.x,self.y] = self.color

    def fysiikka(self):
        self.y += 1

    def timestep(self):
        if self.y < 479:
            self.fysiikka()
        self.piirra()

while True:
    arr.fill(2)
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            x = tapahtuma.pos[0]
            y = tapahtuma.pos[1]
            lista.append(Vesi(x,y))
        if tapahtuma.type == pygame.QUIT:
            for x in range(480):
                print(pikselit[x,240])
            exit()
        
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_ESCAPE:
                exit()       
        
    for vesi in lista: 
        vesi.timestep()         
    
    kello.tick(30)
    pygame.display.flip()

        
        