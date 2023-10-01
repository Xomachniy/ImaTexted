from pygame import *
from random import randint
init()
mixer.init()

class GameSprite(sprite.Sprite):
    def __init__(self, Sprite_image, SpriteWidght, SpriteHeight, SpriteX, SpriteY, SpriteHP, SpriteDef, SpriteAttack):
        super().__init__()
        self.image = transform.scale(image.load(Sprite_image), (SpriteWidght, SpriteHeight))
        self.rect = self.image.get_rect()
        self.rect.x = SpriteX
        self.rect.y = SpriteY
        self.hp = SpriteHP
        self.MaxHp = SpriteHP
        self.defence = SpriteDef
        self.MaxDefence = SpriteDef
        self.attack = SpriteAttack
        self.def_ = False

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def Defence(self):
        self.def_ = True
    def Undefence(self):
        self.def_ = False
    def attack(self, attacked):
        if attacked.defence > 0:
            attacked.defence -= self.attack
        if attacked.defence <= 0:
            attacked.hp -= self.attack

class Knight(Player):
    def ArmorRegen(self):
        self.defence = self.MaxDefence
    def Def(self):
        NoDamage == True
        return
class Archer(Player):
    def Dodge(self):
        dodge = randint(1, 21)
        if dodge == 20:
            NoDamage == True
            return
    def miss(self):
        miss = randint(1, 11)
        if dodge == 10:
            pass
class Mage(Player):
    def __init__(self, Sprite_image, SpriteWidght, SpriteHeight, SpriteX, SpriteY, SpriteHP, SpriteDef, SpriteAttack, mana):
        super().__init__(Sprite_image, SpriteWidght, SpriteHeight, SpriteX, SpriteY, SpriteHP, SpriteDef, SpriteAttack)
        self.mana = mana
        self.maxMana = mana
        self.MaxAttack = self.attack
    def ManaRegen(self):
        self.mana += self.maxMana/2
        if self.mana > self.maxMana:
            self.mana = self.maxMana
    def allMana(self):
        self.mana = self.maxMana
    def damageMana(self):
        if self.mana >= 33:
            self.attack = self.MaxAttack
            self.mana -= 33
            if self.mana <= 0:
                self.mana = 0
        if self.mana < 33:
            self.attack = 6
        
window = display.set_mode((900, 600))
display.set_caption('ImaTexted')

Plain = transform.scale(image.load('Plain.jpg'), (900, 600))
Forest = transform.scale(image.load('Forest.jpg'), (900, 600))
Tavern = transform.scale(image.load('Tavern.jpg'), (900, 600))
Plain2 = transform.scale(image.load('Plain2.jpg'), (900, 600))
City = transform.scale(image.load('City.jpg'), (900, 600))

RPGLogo = transform.scale(image.load('RPGLogo.png'), (512, 128))
Back = transform.scale(image.load('Background.png'), (128, 256))

KnightArt = transform.scale(image.load('Warrior.png'), (128, 128))
ArcherArt = transform.scale(image.load('Archer.png'), (128, 128))
MageArt = transform.scale(image.load('Mage.png'), (128, 128))

fontTXT = font.SysFont('Arial', 20)
fontText = font.SysFont('Arial', 15)

mixer.init()
mixer.music.load('In-tavern.ogg')
mixer.music.play()

clock = time.Clock()
fps = 60

NoDamage = False
ok = False
StartScreen = True
ForуstScore = 0
PlainScore = 0
Plain2Score = 0
CityScore = 0
ForestClear = True
PlainClear = True
Plain2Clear = True
CityClear = True
MusicReload = False

game = True
while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if StartScreen == True:
            window.blit(Tavern, (0, 0))
            window.blit(RPGLogo, (199, 50))
            window.blit(Back, (100, 250))
            window.blit(Back, (672, 250))
            window.blit(Back, (385, 250))
            window.blit(KnightArt, (100, 250))
            window.blit(ArcherArt, (385, 250))
            window.blit(MageArt, (672, 250))
            window.blit(fontTXT.render('1.Рыцарь',True,(255, 255, 255)), (100, 380))
            window.blit(fontText.render('Чинит всю броню',True,(255, 255, 255)), (100, 410))
            window.blit(fontText.render('при переходе в',True,(255, 255, 255)), (100, 425))
            window.blit(fontText.render('другую локацию.',True,(255, 255, 255)), (100, 440))
            window.blit(fontText.render('Защищается от',True,(255, 255, 255)), (100, 455))
            window.blit(fontText.render('всего получаемого',True,(255, 255, 255)), (100, 470))
            window.blit(fontText.render('урона.',True,(255, 255, 255)), (100, 485))

            window.blit(fontTXT.render('2.Лучник',True,(255, 255, 255)), (385, 380))
            window.blit(fontText.render('Наносит',True,(255, 255, 255)), (385, 410))
            window.blit(fontText.render('повышенный урон',True,(255, 255, 255)), (385, 425))
            window.blit(fontText.render('с шансем',True,(255, 255, 255)), (385, 440))
            window.blit(fontText.render('промахнуться.',True,(255, 255, 255)), (385, 455))
            window.blit(fontText.render('Может увернуться',True,(255, 255, 255)), (385, 470))
            window.blit(fontText.render('и не получить урон.',True,(255, 255, 255)), (385, 485))

            window.blit(fontTXT.render('3.Маг',True,(255, 255, 255)), (672, 380))
            window.blit(fontText.render('Наносит большой',True,(255, 255, 255)), (672, 410))
            window.blit(fontText.render('урон за ману.',True,(255, 255, 255)), (672, 425))
            window.blit(fontText.render('Восстанавливает',True,(255, 255, 255)), (672, 440))
            window.blit(fontText.render('ману при защите.',True,(255, 255, 255)), (672, 455))
            if e.type == KEYDOWN:
                if e.key == K_1:
                    Player = Knight('Warrior.png', 200, 200, 100, 350, 150, 50, 30)
                    StartScreen = False
                    ForestClear = False
                    MusicReload = True
                if e.key == K_2:
                    Player = Archer('Archer.png', 200, 200, 100, 350, 150, 50, 30)
                    StartScreen = False
                    ForestClear = False
                    MusicReload = True
                if e.key == K_3:
                    Player = Mage('Mage.png', 200, 200, 100, 350, 150, 50, 30, 100)
                    StartScreen = False
                    ForestClear = False
                    MusicReload = True
        if ForestClear == False:
            if MusicReload == True:
                mixer.music.load('Forest.ogg')
                mixer.music.play()
                MusicReload = False
            window.blit(Forest, (0, 0))
            Player.reset()

    clock.tick(fps)
    display.update()