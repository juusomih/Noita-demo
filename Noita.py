import numpy, pygame, random
HEIGHT, WIDTH = 640, 480
HIEKKA = 100
VESI = 255

testi = numpy.zeros((HEIGHT, WIDTH))

pygame.init()

naytto = pygame.display.set_mode((HEIGHT, WIDTH))
kello = pygame.time.Clock()
bgcolor = 0

def hiekkafysiikka(array):
    for row in range(array.shape[0] - 2, -1, -1):
            can_move = (array[row] == HIEKKA) & (array[row + 1] == 0)
            array[row][can_move] = 0
            array[row + 1][can_move] = HIEKKA

    return array


while True:
    for tapahtuma in pygame.event.get():
        
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            testi[x,y] = HIEKKA
        if tapahtuma.type == pygame.QUIT:
            exit()
        
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_ESCAPE:
                exit()       
        
    testi = hiekkafysiikka(testi)

    
    surface = pygame.surfarray.make_surface(testi)
    naytto.blit(surface, (0, 0))
    pygame.display.flip()


        
        