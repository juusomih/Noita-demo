import numpy as np, pygame, random,cProfile,time

WIDTH, HEIGHT = 640, 480
ILMA = 0
TIILI = 100
HIEKKA = 249
SAVU = 50
VESI = 2


tiilta = False
hiekkaa = False
vetta = False
savua = False
testi = np.full((HEIGHT, WIDTH),ILMA)
mask = np.zeros_like(testi, dtype=bool)
kello = pygame.time.Clock()
pygame.init()

naytto = pygame.display.set_mode((WIDTH, HEIGHT))
kello = pygame.time.Clock()

def old_move_particle(particle, destination: str, current_row, below_row, mask):
    if destination == "down":
        current_row[mask] = ILMA
        below_row[mask] = particle

    elif destination == "down_left":
        current_row[1:][mask] = ILMA
        below_row[:-1][mask] = particle

    elif destination == "down_right":
        current_row[:-1][mask] = ILMA
        below_row[1:][mask] = particle

    elif destination == "left":
        pass

    elif destination == "right":
        pass

    elif destination == "up":
        current_row[mask] = particle
        below_row[mask] = ILMA

    elif destination == "up_left":
        pass

    elif destination == "up_right":
        pass

def spawn_particle(array, particle,y:int = 1,x:int = 1):
    pass
	
def explosion():
    pass

def print_partikkeli_lkm():
    hiekkalkm = np.count_nonzero(testi == HIEKKA)
    vesilkm = np.count_nonzero(testi == VESI)
    #print(f"hiekka: {hiekkalkm} vesi: {vesilkm}")
    return hiekkalkm, vesilkm

def old_check_down(array,row,blokki):
    mask = (array[row] == blokki) & (array[row + 1] == ILMA)
    return mask

def old_check_diagonal_down_left(array,row, blokki):
    mask = (array[row + 1][:-1] == ILMA) & (array[row + 1][1:] == blokki) & (array[row][1:] == blokki)
    return mask

def old_check_diagonal_down_right(array,row, blokki):
    mask = (array[row + 1][1:] == ILMA) & (array[row + 1][:-1] == blokki) & (array[row][:-1] == blokki)
    return mask

def old_check_left(array,row,blokki):
    mask = (array[row][1:] == blokki) & (array[row][:-1] == ILMA)
    return mask

def old_check_right(array,row,blokki):
    mask = (array[row][:-1] == blokki) & (array[row][1:] == ILMA)
    return mask

def down(array,mask,blokki):
    mask[1:,1:] = (array[1:,1:] == ILMA) & (array[:-1,1:] == blokki)
    array[:-1,1:][mask[1:,1:]] = ILMA
    array[mask] = blokki

def diag_left(array,mask,blokki):
    mask[1:,:-1] = (array[:-1,1:] == blokki) & (array[1:,:-1] == ILMA) & (array[1:,1:] != ILMA)
    array[:-1,1:][mask[1:,:-1]] = ILMA
    array[mask] = blokki

def diag_right(array,mask,blokki):
    mask[1:,1:] = (array[:-1,:-1] == blokki) & (array[1:,1:] == ILMA) & (array[1:,:-1] != ILMA)
    array[:-1,:-1][mask[1:,1:]] = ILMA
    array[mask] = blokki

def hiekka_fysiikka(array,mask):
    down(array,mask,HIEKKA)
    diag_left(array,mask,HIEKKA)
    diag_right(array,mask,HIEKKA)

    return array

def vesi_fysiikka(array,mask):
    pass
    #left
    # mask[:-1,:-1] = (testi[:-1,:-1] == ILMA) & (testi[:-1,1:] == HIEKKA) & (testi[1:,1:] != ILMA) & (testi[1:,:-1] != ILMA) 
    # testi[:-1,1:][mask[:-1,:-1]] = ILMA
    # testi[mask] = HIEKKA
    # #right
    # mask[:-1,1:] = (testi[:-1,1:] == ILMA) & (testi[:-1,:-1] == HIEKKA) & (testi[1:,:-1] != ILMA) & (testi[1:,1:] != ILMA) 
    # testi[:-1,:-1][mask[:-1,1:]] = ILMA
    # testi[mask] = HIEKKA

def vanha_vesi_fysiikka(array):
    for row in range(array.shape[0] - 2, -1, -1):
        current_row = array[row]
        below_row = array[row + 1]

        old_move_particle(
            VESI,
            "down", 
            current_row, 
            below_row, 
            old_check_down(array, row, VESI)
        )

        old_move_particle(
            VESI,
            "down_left",
            current_row,
            below_row,
            old_check_diagonal_down_left(array, row, VESI),
        )

        old_move_particle(
            VESI,
            "down_right",
            current_row,
            below_row,
            old_check_diagonal_down_right(array, row, VESI),
        )

        can_moveleft = old_check_left(array, row, VESI)
        can_moveright = old_check_right(array, row, VESI)
        
        if random.random() < 0.3:
            left_mask = can_moveleft
            right_mask = can_moveright & ~can_moveleft

            current_row[1:][left_mask] = ILMA
            current_row[:-1][left_mask] = VESI
        else:
            right_mask = can_moveright
            left_mask = can_moveleft & ~can_moveright

            current_row[:-1][right_mask] = ILMA
            current_row[1:][right_mask] = VESI

    return array

#cProfile.run("hiekka_fysiikka(testi,mask)")
while True:
    start = time.perf_counter()
    
    print_partikkeli_lkm()
    x, y = pygame.mouse.get_pos()
    for tapahtuma in pygame.event.get():
        
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_1:
                hiekkaa = True
            if tapahtuma.key == pygame.K_2:
                vetta = True
            if tapahtuma.key == pygame.K_3:
                tiilta = True
            if tapahtuma.key == pygame.K_4:
                savua = True
            if tapahtuma.key == pygame.K_ESCAPE:
                exit()
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_1:
                hiekkaa = False
            if tapahtuma.key == pygame.K_2:
                vetta = False
            if tapahtuma.key == pygame.K_3:
                tiilta = False
            if tapahtuma.key == pygame.K_4:
                savua = False
        if tapahtuma.type == pygame.QUIT:
            exit()
        
    testi = hiekka_fysiikka(testi,mask)
    #testi = vanha_vesi_fysiikka(testi)
    if hiekkaa:
        testi[y,x] = HIEKKA
    if vetta and x+3 < WIDTH:
        testi[y,x] = VESI
        testi[y,x+1] = VESI
        testi[y,x+2] = VESI
        testi[y,x+3] = VESI
    if tiilta:
        testi[y,x] = TIILI
    if savua:
        testi[y,x] = SAVU
        
    surface = pygame.surfarray.make_surface(testi.T)
    naytto.blit(surface, (0, 0))
    
    kello.tick(0)
    pygame.display.flip()
    end = time.perf_counter()
    pygame.display.set_caption(f"{kello.get_fps():.1f} fps -- {(end - start) * 1000 :.3f} ms -- {print_partikkeli_lkm()[0]} hiekka {print_partikkeli_lkm()[1]} vesi ")
    

        
        