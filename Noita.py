import numpy, pygame, random,cProfile
WIDTH, HEIGHT = 640, 480
ILMA = 0
TIILI = 2
HIEKKA = 100
VESI = 255


tiilta = False
hiekkaa = False
vetta = False
testi = numpy.full((HEIGHT, WIDTH),ILMA)
kello = pygame.time.Clock()
pygame.init()

naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()


def check_down(array,row,blokki):
    mask = (array[row] == blokki) & (array[row + 1] == ILMA)
    return mask

def check_diagonal_left(array,row, blokki):
    mask = (array[row + 1][:-1] == ILMA) & (array[row + 1][1:] == blokki) & (array[row][1:] == blokki)
    return mask

def check_diagonal_right(array,row, blokki):
    mask = (array[row + 1][1:] == ILMA) & (array[row + 1][:-1] != ILMA) & (array[row][:-1] == blokki)
    return mask

def check_left(array,row,blokki):
    mask = (array[row][1:] == blokki) & (array[row][:-1] == ILMA)
    return mask

def check_right(array,row,blokki):
    mask = (array[row][:-1] == blokki) & (array[row][1:] == ILMA)
    return mask

def hiekka_fysiikka(array):
    for row in range(array.shape[0] - 2, -1, -1):
        current_row = array[row]
        below_row = array[row + 1]
        can_movedown = check_down(array,row,HIEKKA)
        current_row[can_movedown] = ILMA
        below_row[can_movedown] = HIEKKA

        can_moveleft = check_diagonal_left(array,row, HIEKKA)
        current_row[1:][can_moveleft] = ILMA
        below_row[:-1][can_moveleft] = HIEKKA
        
        can_moveright = check_diagonal_right(array,row, HIEKKA)
        current_row[:-1][can_moveright] = ILMA
        below_row[1:][can_moveright] = HIEKKA

    return array

def vesi_fysiikka(array):
    for row in range(array.shape[0] - 2, -1, -1):
        current_row = array[row]
        below_row = array[row + 1]

        can_movedown = check_down(array,row,VESI)
        current_row[can_movedown] = ILMA
        below_row[can_movedown] = VESI

        can_move_diagonal_left = check_diagonal_left(array,row, VESI)
        current_row[1:][can_move_diagonal_left] = ILMA
        below_row[:-1][can_move_diagonal_left] = VESI
        
        can_move_diagonal_right = check_diagonal_right(array,row, VESI)
        current_row[:-1][can_move_diagonal_right] = ILMA
        below_row[1:][can_move_diagonal_right] = VESI

        # can_moveleft = check_left(array, row, VESI)
        # current_row[1:][can_moveleft] = ILMA
        # current_row[:-1][can_moveleft] = VESI

        can_moveright = check_right(array, row, VESI)
        current_row[:-1][can_moveright] = ILMA
        current_row[1:][can_moveright] = VESI

    return array
cProfile.run("vesi_fysiikka(testi)")
while True:
    
    x, y = pygame.mouse.get_pos()
    for tapahtuma in pygame.event.get():
        
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_1:
                hiekkaa = True
            if tapahtuma.key == pygame.K_2:
                vetta = True
            if tapahtuma.key == pygame.K_3:
                tiilta = True
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_1:
                hiekkaa = False
            if tapahtuma.key == pygame.K_2:
                vetta = False
            if tapahtuma.key == pygame.K_3:
                tiilta = False
        if tapahtuma.type == pygame.QUIT:
            exit()
        
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_ESCAPE:
                exit()       

    testi = hiekka_fysiikka(testi)
    testi = vesi_fysiikka(testi)

    if hiekkaa:
        testi[y,x] = HIEKKA
    if vetta:
        testi[y,x] = VESI
    if tiilta:
        testi[y,x] = TIILI

    surface = pygame.surfarray.make_surface(testi.T)
    naytto.blit(surface, (0, 0))
    pygame.display.set_caption(f"{kello.get_fps():.1f}")
    kello.tick(0)
    pygame.display.flip()


        
        