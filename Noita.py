import pygame,numpy
global pikselit,bgcolor
pygame.init()
naytto = pygame.display.set_mode((640, 480))
pikselit = pygame.PixelArray(naytto)
arr = pygame.surfarray.pixels2d(naytto)
kello = pygame.time.Clock()
bgcolor = 2
lista = []
clock = pygame.time.Clock()
class Vesi:

    def __init__(self, x,y) -> None:
        self.color = (0,0,250)
        self.x = x
        self.y = y
        self.rest = 0

    def piirra(self):
        pikselit[self.x,self.y] = self.color

    def fysiikka(self):
        alapikseli = pikselit[self.x,self.y + 1]
        vasenpikseli = pikselit[self.x - 1, self.y]
        oikeapikseli = pikselit[self.x + 1, self.y]
        if alapikseli == bgcolor:
            self.y += 1
        elif vasenpikseli == bgcolor and self.x > 0:
            self.x -= 1
        elif oikeapikseli == bgcolor:
            self.x += 1



    def timestep(self):
        if self.y < 479:
            self.fysiikka()
            if self.y < 478:
                print(pikselit[self.x,self.y+1])
        self.piirra()

while True:
    arr.fill(bgcolor)
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            x = tapahtuma.pos[0]
            y = tapahtuma.pos[1]
            lista.append(Vesi(x,y))
        if tapahtuma.type == pygame.QUIT:
            exit()
        
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_ESCAPE:
                exit()       
        
    for vesi in lista: 
        vesi.timestep()         
    
    kello.tick(60)
    pygame.display.flip()

        
        