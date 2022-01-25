import random
import pygame


pygame.init()

dis_w = 1080
dis_h = 600



display = pygame.display.set_mode((dis_w, dis_h))
pygame.display.set_caption('SOUL&DEMONS')

logo = pygame.image.load('logo.jpg')
pygame.display.set_icon(logo)

gg_w = 60
gg_h = 100
gg_x = 20
gg_y = 440
ggw = pygame.image.load('ggw.png')
ggs = pygame.image.load('ggs.png')
ggd = pygame.image.load('ggd.png')
gga = pygame.image.load('gga.png')
onis = pygame.image.load('onis.png')
onid = pygame.image.load('onid.png')
onia = pygame.image.load('onia.png')
oniw = pygame.image.load('oniw.png')
liveg = pygame.image.load('live.png')
death = pygame.image.load('death.jpg')
pygame.mixer.music.set_volume(0.02)
clock = pygame.time.Clock()
enem_s = 5
coef = 0
en_x = 1080
en_y = 440
lives = 3

class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.unactive = (0, 0, 0)
        self.active = (62, 180, 137)

    def draw(self, x, y, text, action=None):
        coord = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < coord[0] < x + self.width:
            if y < coord[1] < y + self.height:
                pygame.draw.rect(display, self.active, (x, y, self.width, self.height))
                if click[0] == 1 and action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()


            else:
                pygame.draw.rect(display, self.unactive, (x, y, self.width, self.height))
        else:
            pygame.draw.rect(display, self.unactive, (x, y, self.width, self.height))
        write3(text, x + 10, y + 10)

class Buttond:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.unactive = (0, 0, 0)
        self.active = (186, 1, 32)

    def draw(self, x, y, text, action=None):
        coord = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < coord[0] < x + self.width:
            if y < coord[1] < y + self.height:
                pygame.draw.rect(display, self.active, (x, y, self.width, self.height))
                if click[0] == 1 and action is not None:
                    action()

            else:
                pygame.draw.rect(display, self.unactive, (x, y, self.width, self.height))
        else:
            pygame.draw.rect(display, self.unactive, (x, y, self.width, self.height))
        write3(text, x + 10, y + 10)

class Buttonp:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.unactive = (50, 50, 50)
        self.active = (0, 255, 80)

    def draw(self, x, y, text, action=None):
        coord = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < coord[0] < x + self.width:
            if y < coord[1] < y + self.height:
                pygame.draw.rect(display, self.active, (x, y, self.width, self.height))
                if click[0] == 1 and action is not None:
                    action()

            else:
                pygame.draw.rect(display, self.unactive, (x, y, self.width, self.height))
        else:
            pygame.draw.rect(display, self.unactive, (x, y, self.width, self.height))
        write3(text, x + 10, y + 10)


class Enems:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self):
        if self.x >= 40:
            display.blit(onis, (self.x, self.y))
            self.x -= self.speed
        else:
            self.x = dis_w - 50

class Enemd:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self):
        if self.x >= 40:
            display.blit(onid, (self.x, self.y))
            self.x -= self.speed
        else:
            self.x = dis_w - 50

class Enemw:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self):
        if self.x >= 40:
            display.blit(oniw, (self.x, self.y))
            self.x -= self.speed
        else:
            self.x = dis_w - 50

class Enema:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self):
        if self.x >= 40:
            display.blit(onia, (self.x, self.y))
            self.x -= self.speed
        else:
            self.x = dis_w - 50





warn_w = False
warn_s = False
warn_a = False
warn_d = False
gg = ggs
count = 20
lets = ['s']
tipes = [' ']
enemes = []
destr = 0


def menu():
    start_b = Button(260, 70)
    lore_b = Button(650, 80)
    music_b = Button(270, 70)
    quit_b = Button(180, 80)
    bg = pygame.image.load('MENU.png')
    pygame.mixer.music.load('HateYou.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        display.blit(bg, (0, 0))
        start_b.draw(410, 150, 'Start', gogo)
        lore_b.draw(210, 250, 'Lore&Tutorial', sets)
        music_b.draw(405, 360, 'Music', mus)
        quit_b.draw(450, 460, 'Quit', quit)
        pygame.display.update()
        clock.tick(60)

def m1():
    menu()

def m2():
    menu()

def gogo():
    while game_ready():
        pass

def sets():
    bg2 = pygame.image.load('titr2.png')
    qwer = True
    back_b2 = Button(260, 70)
    while qwer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        display.blit(bg2, (0, 0))
        back_b2.draw(510, 510, 'Back', m1)
        pygame.display.update()

def mus():
    bg1 = pygame.image.load('titr1.png')
    qwer = True
    back_b1 = Button(260, 70)
    while qwer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        display.blit(bg1, (0, 0))
        back_b1.draw(510, 510, 'Back', m2)
        pygame.display.update()




def game_ready():
    global warn_w, warn_d, warn_a, warn_s, gg, count, lets, lives, enemes
    pygame.mixer.music.load('Ropes.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    game = True
    location = pygame.image.load('bg1.png')
    color_key = location.get_at((0, 0))
    ggs.set_colorkey(color_key)
    ggw.set_colorkey(color_key)
    gga.set_colorkey(color_key)
    ggd.set_colorkey(color_key)


    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            warn_w = True

        if warn_w:
            gg = ggw
            warn_w = False
            lets.append('w')

        if keys[pygame.K_s]:
            warn_s = True

        if warn_s:
            gg = ggs
            warn_s = False
            lets.append('s')

        if keys[pygame.K_a]:
            warn_a = True

        if warn_a:
            gg = gga
            warn_a = False
            lets.append('a')

        if keys[pygame.K_d]:
            warn_d = True

        if warn_d:
            gg = ggd
            warn_d = False
            lets.append('d')

        if keys[pygame.K_ESCAPE]:
            pause()

        if cosan(enemes):
            lives -= 1

        if lives <= 0:
            return la_finita()

        display.blit(location, (0, 0))

        display.blit(gg, (gg_x, gg_y))

        rand_enem()

        draw_array(enemes)
        live()
        speedup()
        #button.draw(50, 50, 'QUIT', )
        write1(f'KILLS×{destr}', 900, 30)

        if len(lets) == 0:
            display.blit(gg, (gg_x, gg_y))

        count += 1

        pygame.display.update()
        clock.tick(60)


def draw_array(array):
    for enem in array:
        enem.move()

def rand_enem():
    en = random.randint(1,4)
    if tipes[-1] == ' ':
        if en == 1:
            tipes.append('s')
            enemes.append(Enemw(1080, 450, 20, 70, enem_s + coef))
        elif en == 2:
            tipes.append('a')
            enemes.append(Enemd(1080, 450, 20, 70, enem_s + coef))
        elif en == 3:
            tipes.append('d')
            enemes.append(Enema(1080, 450, 20, 70, enem_s + coef))
        elif en == 4:
            tipes.append('w')
            enemes.append(Enems(1080, 450, 20, 70, enem_s + coef))


def write(text, x, y, colour = (0, 255, 80), tipe='FSAMURAI.otf', size=60):
    tipe = pygame.font.Font(tipe, size)
    text = tipe.render(text, True, colour)
    display.blit(text, (x, y))

def write1(text, x, y, colour = (0, 255, 80), tipe='ISH.otf', size=60):
    tipe = pygame.font.Font(tipe, size)
    text = tipe.render(text, True, colour)
    display.blit(text, (x, y))

def write2(text, x, y, colour = (188, 1, 32), tipe='Razer.otf', size=50):
    tipe = pygame.font.Font(tipe, size)
    text = tipe.render(text, True, colour)
    display.blit(text, (x, y))

def write3(text, x, y, colour = (255, 255, 255), tipe='Razer.otf', size=60):
    tipe = pygame.font.Font(tipe, size)
    text = tipe.render(text, True, colour)
    display.blit(text, (x, y))



def pause():
    paused = True
    pygame.mixer.music.pause()
    quit_b = Buttonp(220, 75)
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        write('You are on pause.', 150, 150)
        write('Press Enter', 250, 250)
        quit_b.draw(410, 500, 'Quit', quit)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False
        pygame.display.update()
        clock.tick(15)
    pygame.mixer.music.unpause()


def cosan(enem):
    global destr
    if not (lets[-1] == tipes[-1]):
        for el in enem:
            if el.x <= 150:
                tipes.append(' ')
                enem.clear()
                return True
    else:
        for el in enem:
            if el.x <= 150:
                tipes.append(' ')
                enem.clear()
                destr += 1
                return False



def la_finita():
    global lives, destr
    display.blit(death, (0, 0))
    pygame.mixer.music.stop()
    dead = True
    destr = 0
    rerun_b = Buttond(450, 80)
    away_b = Buttond(260, 75)
    while dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        rerun_b.draw(350, 400, 'Try again', game_ready)
        away_b.draw(450, 500, 'Quit', quit)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            return True
        lives = 3
        if keys[pygame.K_f]:
            return False
        pygame.display.update()
        clock.tick(15)

def speedup():
    global destr, coef
    coef = destr // 5

def live():
    global lives
    liv = lives
    x = 20
    while liv != 0:
        display.blit(liveg, (x, 20))
        x += 20
        liv -= 1


menu()
while game_ready():
    pass
pygame.quit()
quit()