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
    def attacking(self, attacked):
        if attacked.defence > 0:
            attacked.defence -= self.attack
        if attacked.defence <= 0:
            attacked.hp -= self.attack
    def WeakAttack(self, attacked):
        if attacked.defence > 0:
            attacked.defence -= self.attack//3
        if attacked.defence <= 0:
            attacked.hp -= self.attack//3

class Knight(Player):
    def ArmorRegen(self):
        self.defence = self.MaxDefence

class Archer(Player):
    def Dodge(self):
        dodge = randint(1, 20)
        if dodge == 20:
            NoDamage = True
            return
    def miss(self):
        miss = randint(1, 10)
        if miss == 10:
            attacked.hp -= 0
        else:
            self.attacking()
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
            self.attack = self.MaxAttack*2
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
TextBack = transform.scale(image.load('Background.png'), (900, 150))
HpBack = transform.scale(image.load('Background.png'), (150, 100))
ButtonBack = transform.scale(image.load('Button.png'), (150, 26))

TransitionBackFirst = transform.scale(image.load('Background.png'), (900, 700))

KnightArt = transform.scale(image.load('Warrior.png'), (128, 128))
ArcherArt = transform.scale(image.load('Archer.png'), (128, 128))
MageArt = transform.scale(image.load('Mage.png'), (128, 128))

fontTXT = font.SysFont('Arial', 20)
fontText = font.SysFont('Arial', 15)
fontDeath = font.SysFont('Arial', 50)

mixer.init()
mixer.music.load('In-tavern.ogg')
mixer.music.play()

clock = time.Clock()
fps = 60

ThisText = 'Для начала битвы нажмите кнопку атаки или защиты!'
Transition = False
TransitionTime = 0
NoDamage = False
ok = False
StartScreen = True
ForestScore = 0
PlainScore = 0
Plain2Score = 0
CityScore = 0
ForestClear = True
PlainClear = True
Plain2Clear = True
CityClear = True
MusicReload = False
PlayerMage = False
PlayerKnight = False
PlayerArcher = False
battlemode = False
startBattle = False
Defending = False
Attacks = False
EnemyAttack = False
EnemyDefend = False
MoveWas = False

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
        window.blit(fontText.render('в начале новго',True,(255, 255, 255)), (100, 425))
        window.blit(fontText.render('боя.',True,(255, 255, 255)), (100, 440))
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
                RealPlayer = Knight('Warrior.png', 200, 200, 100, 350, 150, 50, 30)
                StartScreen = False
                Transition = True
                MusicReload = True
                PlayerKnight = True
            if e.key == K_2:
                RealPlayer = Archer('Archer.png', 200, 200, 100, 350, 100, 50, 30)
                StartScreen = False
                Transition = True
                MusicReload = True
                PlayerArcher = True
            if e.key == K_3:
                RealPlayer = Mage('Mage.png', 200, 200, 100, 350, 75, 100, 30, 100)
                StartScreen = False
                Transition = True
                MusicReload = True
                PlayerMage = True
        
    if Transition == True:
        if TransitionTime >= 0 and TransitionTime <= 30:
            window.blit(TransitionBackFirst, (0, 0))
        if TransitionTime > 60:
            ForestClear = False
            Transition = False
        TransitionTime += 1

    if ForestClear == False:
        if MusicReload == True:
            mixer.music.load('Forest.ogg')
            mixer.music.play()
            MusicReload = False
        window.blit(Forest, (0, 0))
        window.blit(TextBack, (0, 0))
        window.blit(HpBack, (0, 150))
        window.blit(HpBack, (750, 150))
        window.blit(ButtonBack, (0, 250))
        window.blit(ButtonBack, (0, 276))
        window.blit(fontTXT.render('ОЗ: ' + str(RealPlayer.hp) + '/' + str(RealPlayer.MaxHp),True,(255, 0, 0)), (0, 170))
        window.blit(fontTXT.render('Защита: ' + str(RealPlayer.defence) + '/' + str(RealPlayer.MaxDefence),True,(255, 255, 255)), (0, 190))
        window.blit(fontTXT.render('1.Атака',True,(255, 255, 255)), (3, 252))
        window.blit(fontTXT.render('2.Защита',True,(255, 255, 255)), (3, 278))
        if PlayerMage == True:
            window.blit(fontTXT.render('Мана: ' + str(RealPlayer.mana) + '/' + str(RealPlayer.maxMana),True,(0, 0, 255)), (0, 210))
        if battlemode == False:
            EnemyNum = randint(1, 5)
            if EnemyNum == 1:
                Enemy = Player('BanditLeft.png', 200, 200, 600, 350, 100, 25, 25)
                TextAttack = 'Бандит замахивается кинжалом...'
                TextDefend = 'Бандит защищается...'
            if EnemyNum == 2:
                Enemy = Player('Bear.png', 300, 150, 575, 400, 200, 10, 30)
                TextAttack = 'Медведь бежит на вас...'
                TextDefend = 'Медведь прикрывается лапами...'
            if EnemyNum == 3:
                Enemy = Player('Ent.png', 200, 200, 600, 350, 200, 10, 20)
                TextAttack = 'Энт поднимает ветви вверх...'
                TextDefend = 'Энт защищается корнями...'
            if EnemyNum == 4:
                Enemy = Player('Squibear.png', 350, 150, 550, 400, 200, 30, 30)
                TextAttack = 'Белко-медведь кричит в вашу сторону...'
                TextDefend = 'Белко-медведь прикрывается хвостом...'
            if EnemyNum == 5:
                Enemy = Player('Skeleton.png', 200, 200, 600, 350, 120, 20, 30)
                TextAttack = 'Скелет замахивается дубиной...'
                TextDefend = 'Скелет стоит, прикрываясь дуюиной...'
            battlemode = True
        if battlemode == True:
            if RealPlayer.hp > 0 and Enemy.hp > 0:
                for e in event.get():
                    if e.type == KEYDOWN:
                        if e.key == K_1:
                            if PlayerArcher == True:
                                miss = randint(1, 10)
                                if miss == 10:
                                    Enemy.hp -= 0
                                else:
                                    if Enemy.def_ == True:
                                        RealPlayer.WeakAttack(Enemy)
                                    else:
                                        RealPlayer.attacking(Enemy)
                            elif PlayerMage == True:
                                RealPlayer.damageMana()
                                if Enemy.def_ == True:
                                    RealPlayer.WeakAttack(Enemy)
                                else:
                                    RealPlayer.attacking(Enemy)
                            else:
                                if Enemy.def_ == True:
                                    RealPlayer.WeakAttack(Enemy)
                                else:
                                    RealPlayer.attacking(Enemy)
                            MoveWas = True
                        if e.key == K_2:
                            RealPlayer.Defence()
                            MoveWas = True
                            if PlayerKnight == True:
                                NoDamage = True
                            if PlayerArcher == True:
                                dodge = randint(1, 20)
                                if dodge == 20:
                                    NoDamage = True
                            if PlayerMage == True:
                                RealPlayer.ManaRegen()
                if MoveWas == True:
                    Enemy.Undefence()
                    if EnemyNum == 4:
                        Enemy.image = transform.scale(image.load('Squibear.png'), (350, 150))
                    if EnemyAttack == True:
                        if NoDamage == True:
                            pass
                        elif RealPlayer.def_ == True:
                            Enemy.WeakAttack(RealPlayer)
                        else:
                            Enemy.attacking(RealPlayer)
                        EnemyAttack = False
                    else:
                        EnemyMove = randint(1, 2)
                        if EnemyMove == 1:
                            ThisText = TextAttack
                            EnemyAttack = True
                        if EnemyMove == 2:
                            if EnemyNum == 4:
                                Enemy.image = transform.scale(image.load('SquibearDefend.png'), (350, 150))
                            ThisText = TextDefend
                            Enemy.Defence()
                    if RealPlayer.defence < 0:
                        RealPlayer.defence = 0
                    if Enemy.defence < 0:
                        Enemy.defence = 0
                    MoveWas = False
                    RealPlayer.Undefence()
                    NoDamage = False
            if Enemy.hp <= 0:
                battlemode = False
                ForestScore += 1
                RealPlayer.hp += RealPlayer.MaxHp//5
                if RealPlayer.hp > RealPlayer.MaxHp:
                    RealPlayer.hp = RealPlayer.MaxHp
                if PlayerKnight == True:
                    RealPlayer.ArmorRegen()
            if RealPlayer.hp <= 0:
                window.blit(TransitionBackFirst, (0, 0))
                window.blit(fontDeath.render('Вы погибли',True,(255, 0, 0)), (425, 300))
            window.blit(fontTXT.render('ОЗ: ' + str(Enemy.hp) + '/' + str(Enemy.MaxHp),True,(255, 0, 0)), (750, 170))
            window.blit(fontTXT.render('Защита: ' + str(Enemy.defence) + '/' + str(Enemy.MaxDefence),True,(255, 255, 255)), (750, 190))
            Enemy.reset()
        window.blit(fontTXT.render(ThisText,True,(255, 255, 255)), (0, 0))
        window.blit(fontTXT.render('Пройдено: ' + str(ForestScore),True,(255, 255, 255)), (150, 150))
        RealPlayer.reset()

    clock.tick(fps)
    display.update()