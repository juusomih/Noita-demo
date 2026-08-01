import numpy, pygame, random
WIDTH, HEIGHT = 640, 480
ILMA = 0
HIEKKA = 100
VESI = 255

testi = numpy.full((HEIGHT, WIDTH),ILMA)

pygame.init()

naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()
bgcolor = 0

def hiekka_fysiikka(array):
    for row in range(array.shape[0] - 2, -1, -1):
        can_move = (array[row] == HIEKKA) & (array[row + 1] == ILMA)
        array[row][can_move] = ILMA
        array[row + 1][can_move] = HIEKKA

    return array

def vesi_fysiikka(array):
    for row in range(array.shape[0] - 2, -1, -1):
        can_move = (array[row] == VESI) & (array[row + 1] == ILMA)
        array[row][can_move] = ILMA
        array[row + 1][can_move] = VESI
    
    return array

while True:
    for tapahtuma in pygame.event.get():
        
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            testi[y,x] = VESI
        if tapahtuma.type == pygame.QUIT:
            exit()
        
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_ESCAPE:
                exit()       
        
    testi = hiekka_fysiikka(testi)
    testi = vesi_fysiikka(testi)

    
    surface = pygame.surfarray.make_surface(testi.T)
    naytto.blit(surface, (0, 0))
    pygame.display.flip()


        
        