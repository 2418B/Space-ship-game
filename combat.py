#!/usr/bin/env python3
import pygame
def setup():
    
    global pygame, threading, sys, math, thorpy, ship, ship2, ship3, beez, bigfont, smallfont, green, red, blue, black, yellow
    global white, arrow, clock, ship3_fire, ship2_fire, ship_fire, bullet, random, bounce, fire, explode
    global disk
    import pygame, threading, sys, math, thorpy, random
    
    ship = pygame.image.load('Ship.png')
    ship_fire = pygame.image.load('Ship_withfire.png')
    ship2 = pygame.image.load('Ship2_nofire.png')
    ship2_fire = pygame.image.load('Ship2.png')
    ship3 = pygame.image.load('Ship3_nofire.png')
    ship3_fire = pygame.image.load('Ship3.png')
    beez = pygame.image.load('Beez.gif')
    arrow = pygame.image.load('Arrow.png')
    bullet = pygame.image.load('bullet.png')
    fire = pygame.image.load('Fireball.png')
    explode = ((pygame.image.load('expode1.png')), (pygame.image.load('expode2.png')), (pygame.image.load('expode3.png')), (pygame.image.load('expode4.png')), (pygame.image.load('expode5.png')), (pygame.image.load('expode6.png')), (pygame.image.load('expode7.png')))
    disk = pygame.image.load('disk.png')
    
    bounce = 0.3
    
    #colors in RGB
    green = (0,250,0)
    blue = (0,0,250)
    red = (250,0,0)
    black = (0,0,0)
    white = (250,250,250)
    yellow = (250, 250, 0)
    
    clock = pygame.time.Clock()
    
    #import libraries and stuff
    
    
    
    pygame.init()
    #initialise pygame

    #fonts
    bigfont = pygame.font.Font(None, 106)
    smallfont = pygame.font.Font(None, 32)
    

#threading function
def Go(y):    
    x = threading.Thread(target=y, args=(1))
    x.start()

def play(x, loop = -1):
    #a function for playing music via threadding.
    pygame.mixer.music.load(x)
    pygame.mixer.music.play(loop)
def playsound(x):
    pygame.mixer.Sound.play(pygame.mixer.Sound(x))
def stop():
    pygame.mixer.music.unload()
def scaleImage(img, scale):
    size = img.get_size()
    img = pygame.transform.scale(img, (int(size[0]*scale), int(size[1]*scale)))
    return img  
def BGM(song):
    #background music
    if song == 1:
        pygame.mixer.music.load("Hacker Duels - INTRO.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.load("Hacker Duels - MAIN LOOP.mp3")
        pygame.mixer.music.play(-1)
    if song == 2:
        pygame.mixer.music.load("Neon Trip - INTRO.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.load("Neon Trip - MAIN LOOP.mp3")
        pygame.mixer.music.play(-1)
    if song == 3:
        pygame.mixer.music.load("Space combat.ogg")
        pygame.mixer.music.play(-1)

class projectile(pygame.sprite.Sprite):
   #projectile class 
    def __init__(self, pos, scale, angle):
        global bullet
        super().__init__()
        self.angle = angle
        self.currentAngle = 0
        self.pos = pos
        self.speed = 300
        self.multiplier = self.speed 
        self.originalImage = scaleImage(bullet, scale)
        self.image = self.originalImage
        self.rect = self.image.get_rect(center=pos)
        self.name = "bullet"
        self.imageName = "bullet"
        self.vel = (0,0)
        if self.currentAngle != self.angle:
            self.image = pygame.transform.rotate(self.originalImage, self.angle)
            self.angle = self.angle % 360  # Value will reapeat after 359. This prevents angle to overflow.
            self.currentAngle = self.angle
        rad = math.radians(self.angle + 180)
        self.vel = (
            self.vel[0] + math.sin(rad) * self.multiplier,
            self.vel[1] + math.cos(rad) * self.multiplier
        
            
            )
            
    def update(self):


        self.rect = self.image.get_rect(center=self.pos)
        self.pos = (
            self.pos[0] + (self.vel[0] * self.speed/1000)/2,
            self.pos[1] + (self.vel[1] * self.speed/1000)/2
            )
        
        if self.pos[0] < 0 or self.pos[0] > size[0]:
            self.kill()
            
        if self.pos[1] < 0 or self.pos[1] > size[1]:
            self.kill()

class fireball(projectile):
    #fire ball class 
     def __init__(self, pos, scale, angle):
         global fire
         super().__init__(pos, scale, angle)
         self.angle = angle
         self.currentAngle = 0
         self.pos = pos
         self.speed = 100
         self.multiplier = self.speed 
         self.originalImage = scaleImage(fire, scale)
         self.image = self.originalImage
         self.rect = self.image.get_rect(center=pos)
         self.name = "bullet"
         self.imageName = "bullet"
         self.vel = (0,0)
         self.looped = 0
         if self.currentAngle != self.angle:
             self.image = pygame.transform.rotate(self.originalImage, self.angle)
             self.angle = self.angle % 360  # Value will reapeat after 359. This prevents angle to overflow.
             self.currentAngle = self.angle
         rad = math.radians(self.angle + 180)
         self.vel = (
             self.vel[0] + math.sin(rad) * self.multiplier,
             self.vel[1] + math.cos(rad) * self.multiplier
         
             
             )
     def update(self):

        self.looped += 1
        self.rect = self.image.get_rect(center=self.pos)
        self.pos = (
            self.pos[0] + (self.vel[0] * self.speed/1000)/2,
            self.pos[1] + (self.vel[1] * self.speed/1000)/2
            )
        
        if self.pos[0] < 0 or self.pos[0] > size[0]:
            self.kill()
            
        if self.pos[1] < 0 or self.pos[1] > size[1]:
            self.kill()
        
        if self.looped > 10:
            self.kill()
            

class circle(projectile):
    
    def __init__(self, pos, scale, angle, player):
        #op is opponet
        super().__init__(pos, scale, angle)     
        self.player = player
        self.angle = angle
        #only used for going forward
        self.currentAngle = 0
        self.pos = pos
        self.speed = 50
        self.multiplier = self.speed 
        self.originalImage = scaleImage(disk, 1)
        self.image = self.originalImage
        self.rect = self.image.get_rect(center=pos)
        self.name = "bullet"
        self.imageName = "bullet"
        rad = math.radians(self.angle + 180)
        self.vel = [
            self.vel[0] + math.sin(rad) * self.multiplier,
            self.vel[1] + math.cos(rad) * self.multiplier
        
            
            ]
        
    def update(self):


        self.rect = self.image.get_rect(center=self.pos)
        self.pos = (
            self.pos[0] + (self.vel[0] * self.speed/1000)/2,
            self.pos[1] + (self.vel[1] * self.speed/1000)/2
            )
        
        if self.pos[0] < 0 or self.pos[0] > size[0]:
            self.vel[0] = self.vel[0] * -1
            
        if self.pos[1] < 0 or self.pos[1] > size[1]:
            self.vel[1] = self.vel[1] * -1
   

#player class
class Ship(pygame.sprite.Sprite):
    #waffles
    def __init__(self, pos = (500,500)):
        super().__init__()
        
        self.op = 0
        #opponent
        
        global ship,ship_fire
            
        
        self.rect = pos 
        
        self.damage = 2
        #from shooting
            
        self.image = scaleImage(ship, 2)
        self.originalImage = self.image
        self.turnedimage = self.image
        self.fireimage = scaleImage(ship_fire, 2)
        self.Originfireimage = self.fireimage
        self.health = 15
        
        self.energy = 15
        self.energyrecover = 1
        #if at 10 or higher there is no cool down rate
        self.maxenergy = self.energy
        
        self.angle = 0
        self.currentAngle = 0
        self.pos = self.rect
        
        self.speed = 10
        
        self.vel = (0,0)
        
    def update(self):
        self.angle = self.angle % 360  # Value will reapeat after 359. This prevents angle to overflow.
        self.image = self.turnedimage
        if self.currentAngle != self.angle:
            self.image = pygame.transform.rotate(self.originalImage, self.angle)
            self.fireimage = pygame.transform.rotate(self.Originfireimage, self.angle)
            self.angle = self.angle % 360  # Value will reapeat after 359. This prevents angle to overflow.
            self.currentAngle = self.angle
            self.turnedimage = self.image      


        self.rect = self.image.get_rect(center=self.pos)
        self.pos = [
            self.pos[0] + (self.vel[0] * self.speed/100),
            self.pos[1] + (self.vel[1] * self.speed/100)
            ]
        #bounce
        if self.pos[0] < 0 or self.pos[0] > size[0]:
            self.vel = (self.vel[0] * -1, self.vel[1])
            self.update()
            self.vel = (self.vel[0] * bounce, self.vel[1])
            self.update()
            
        if self.pos[1] < 0 or self.pos[1] > size[1]:
            self.vel = (self.vel[0], self.vel[1] * -1)
            self.update()
            self.vel = (self.vel[0], self.vel[1] * bounce)
            self.update()
        self.energy = self.energy + self.energyrecover
        if self.energy > self.maxenergy:
            self.energy = self.maxenergy
    
    def moveForward(self):
        rad = math.radians(self.angle + 180)
        self.vel = (
            self.vel[0] + math.sin(rad) * self.speed,
            self.vel[1] + math.cos(rad) * self.speed
                    )
        self.image = self.fireimage
    
    def shoot(self, bg):
        #bg = bullet group
        
        self.energy -= 10
        
        if self.energy < 0:
            self.energy += 10
        
        else:
        
            Bullet = projectile(self.pos,2,self.angle)
            bg.add(Bullet)
        
            Go(playsound("lazer.mp3"))
        
    def hit(self, end):
        #opponent is op
        self.health = self.health - self.op.damage
        if self.health < 1:
            end = 0
            self.kill()
            
        
class Ship2(Ship):
    
    def __init__(self,  pos = (500,500)):
        super().__init__()
        
        self.op = 0
        #opponent
        
        global ship2, ship2_fire
            
        
        self.rect = pos
        
        self.damage = 3
        
        self.image = scaleImage(ship2, 2)
        self.originalImage = self.image
        self.turnedimage = self.image
        self.fireimage = scaleImage(ship2_fire, 2)
        self.Originfireimage = self.fireimage
        self.health = 4
        
        self.energy = 10
        self.energyrecover = 0.5
        self.maxenergy = self.energy
        
        self.angle = 0
        self.currentAngle = 0
        self.pos = self.rect
        
        self.speed = 14
        
        self.vel = (0,0)
    
    def shoot(self, bg):
        #bg = bullet group
        
        self.energy -= 10
        
        if self.energy < 0:
            self.energy += 10
        
        else:
        
            Bullet = circle(self.pos,2,self.angle,self)
            bg.add(Bullet)
        
            Go(playsound("lazer.mp3"))
        
class Ship3(Ship):
    
    def __init__(self,  pos = (500,500)):
        super().__init__()
        
        self.op = 0
        #opponent
            
        global ship3, ship3_fire
            
        
        self.rect = pos
            
        self.damage = 1
        
        self.image = scaleImage(ship3, 2)
        self.originalImage = self.image
        self.turnedimage = self.image
        self.fireimage = scaleImage(ship3_fire, 2)
        self.Originfireimage = self.fireimage
        self.health = 13
        
        self.energy = 17
        self.energyrecover = 1.5
        self.maxenergy = self.energy
        
        self.angle = 0
        self.currentAngle = 0
        self.pos = self.rect
        
        self.speed = 8
        
        self.vel = (0,0)
    
    def shoot(self, bg):
        #bg = bullet group
        
        self.energy -= 15
        
        if self.energy < 0:
            self.energy += 15
        
        else:
        
            Bullet = fireball(pos = self.pos, scale = 2, angle = self.angle)
            bg.add(Bullet)
            
            Bullet = fireball(pos = self.pos, scale = 2, angle = self.angle+20)
            bg.add(Bullet)
            
            Bullet = fireball(pos = self.pos, scale = 2, angle = self.angle-20)
            bg.add(Bullet)
        
            Go(playsound("fire.mp3"))

class battle():
    
    def __init__(self, p1,music = 0):
        global pygame
        
        Go(stop())
        
        if p1 == 0:
            self.Player1 = Ship()
        if p1 == 1:
            self.Player1 = Ship2()
        if p1 == 2:
            self.Player1 = Ship3()
        
        Go(BGM(music))

        self.update()
        
    
    def end(self,win):
        #win used to decide who wins
        
        global bigfont, screen, white, pygame, random, smallfont
        
        end = bigfont.render("Match over", True, white)
        
        
        if win == 1:
            winner = smallfont.render("You beat the sniper bot", True, white) 
        
        if win == 0:
            winner = smallfont.render("Ha, you lose, L", True, white)     
        
        
        screen.blit(end,(400,400)) 
        
        screen.blit(winner,(400,600))
        
        
        pygame.display.flip()
        
        while True:
        
            
        
            #input part
            for event in pygame.event.get():
                
                #quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Menu = menu()
            
        
    def update(self):
        global black, screen, pygame, clock, ship3_fire, smallfont, math, bounce, green, explode
        
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill(black)
        
        CPU = random.randrange(0,3)
        
        if CPU == 0:
        
            CPU = Ship((300,200))
        if CPU == 1:
        
            CPU = Ship2((300,200))
        if CPU == 2:
        
            CPU = Ship3((300,200))
            
        if CPU == 3:
            self.update()    
        
        CPU.op = self.Player1
        
        self.Player1.op = CPU
        
        self.ShipGroup = pygame.sprite.Group()
        self.ShipGroup.add(self.Player1)
        self.ShipGroup.add(CPU)
        
        self.P1BulletGroup = pygame.sprite.Group()
        self.CPUBullet = pygame.sprite.Group()
        
        self.going = 1
        
        self.index = 0
        
        while self.going == 1:
            
            p1health = smallfont.render(str(self.Player1.health), True, green)
            cpuhealth = smallfont.render(str(CPU.health), True, green)
            #updating text
        
        
            #input part
            for event in pygame.event.get():
                
                #quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #input       
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.Player1.moveForward()
            if keys[pygame.K_LEFT]:
                self.Player1.angle = self.Player1.angle + (self.Player1.speed)
            if keys[pygame.K_RIGHT]:
                self.Player1.angle = self.Player1.angle - (self.Player1.speed)
            if keys[pygame.K_SPACE]:
                self.Player1.shoot(self.P1BulletGroup)
            screen.blit(background,(0,0))
            for Bullet in self.P1BulletGroup:
                if CPU.rect.colliderect(Bullet.rect):
                    Bullet.kill()
                    CPU.hit(self.going)
            for Bullet in self.CPUBullet:
                if self.Player1.rect.colliderect(Bullet.rect):
                    Bullet.kill()
                    self.Player1.hit(self.going)
            if not self.ShipGroup.has(self.Player1):
                if self.index > 15:
                    self.index = 1
                if self.index == 1:
                    screen.blit(scaleImage(explode[0], 2), self.Player1.pos)
                if self.index == 2:
                    screen.blit(scaleImage(explode[0], 2), self.Player1.pos)
                if self.index == 3:
                    screen.blit(scaleImage(explode[1], 2), self.Player1.pos)
                if self.index == 4:
                    screen.blit(scaleImage(explode[1], 2), self.Player1.pos)
                if self.index == 5:
                    screen.blit(scaleImage(explode[2], 2), self.Player1.pos)
                if self.index == 6:
                    screen.blit(scaleImage(explode[2], 2), self.Player1.pos)
                if self.index == 7:
                    screen.blit(scaleImage(explode[3], 2), self.Player1.pos)
                if self.index == 8:
                    screen.blit(scaleImage(explode[3], 2), self.Player1.pos)
                if self.index == 9:
                    screen.blit(scaleImage(explode[4], 2), self.Player1.pos)
                if self.index == 10:
                    screen.blit(scaleImage(explode[4], 2), self.Player1.pos)
                if self.index == 11:
                    screen.blit(scaleImage(explode[5], 2), self.Player1.pos)
                if self.index == 12:
                    screen.blit(scaleImage(explode[5], 2), self.Player1.pos)
                if self.index == 13:
                    screen.blit(scaleImage(explode[6], 2), self.Player1.pos)
                if self.index == 14:
                    screen.blit(scaleImage(explode[6], 2), self.Player1.pos)
                if self.index == 15:
                    self.going = 0
                    self.end(0)
            
            if not self.ShipGroup.has(CPU):
                if self.index > 15:
                    self.index = 1
                if self.index == 1:
                    screen.blit(scaleImage(explode[0], 2), CPU.pos)
                if self.index == 2:
                    screen.blit(scaleImage(explode[0], 2), CPU.pos)
                if self.index == 3:
                    screen.blit(scaleImage(explode[1], 2), CPU.pos)
                if self.index == 4:
                    screen.blit(scaleImage(explode[1], 2), CPU.pos)
                if self.index == 5:
                    screen.blit(scaleImage(explode[2], 2), CPU.pos)
                if self.index == 6:
                    screen.blit(scaleImage(explode[2], 2), CPU.pos)
                if self.index == 7:
                    screen.blit(scaleImage(explode[3], 2), CPU.pos)
                if self.index == 8:
                    screen.blit(scaleImage(explode[3], 2), CPU.pos)
                if self.index == 9:
                    screen.blit(scaleImage(explode[4], 2), CPU.pos)
                if self.index == 10:
                    screen.blit(scaleImage(explode[4], 2), CPU.pos)
                if self.index == 11:
                    screen.blit(scaleImage(explode[5], 2), CPU.pos)
                if self.index == 12:
                    screen.blit(scaleImage(explode[5], 2), CPU.pos)
                if self.index == 13:
                    screen.blit(scaleImage(explode[6], 2), CPU.pos)
                if self.index == 14:
                    screen.blit(scaleImage(explode[6], 2), CPU.pos)
                if self.index == 15:
                    self.going = 0
                    self.end(1) 
            
            CPU_distance = ((self.Player1.pos[0]-CPU.pos[0]) , (self.Player1.pos[1]-CPU.pos[1]))
            #for calculating turn
            
            if CPU_distance[1] > 0:
                CPU.angle = math.degrees(math.atan(CPU_distance[0]/-CPU_distance[1]))
                CPU.angle = 180 - (CPU.angle + math.pi)
            
            else:
                
                CPU.angle = math.degrees(math.atan(CPU_distance[0]/CPU_distance[1]))
            
            #move and shoot
            CPU.moveForward()
            
                
            CPU.shoot(self.CPUBullet)
            
            
            self.P1BulletGroup.draw(screen)
            self.CPUBullet.draw(screen)
            self.ShipGroup.draw(screen)
            
            
            screen.blit(p1health,(0,0))
            screen.blit(cpuhealth, (100,0))
            
            pygame.display.flip()
            
            self.ShipGroup.update()
            self.P1BulletGroup.update()
            self.CPUBullet.update()
            
            self.index += 1
            
            clock.tick(24)
            
           

class menu():
    
    def __init__(self):
        global size, screen
        size = (1000,800)
        screen = pygame.display.set_mode(size)
        self.size = size
        
        self.P1Ship = ship
        
        #a few declerations
        
        Go(play("shiny-mall.mp3"))
        
        self.update()
        
        
    def update(self):
        global ship, ship2, ship3, screen, bigfont, smallfont, white, arrow, black, clock
        P1 = smallfont.render("Player1's ship", True, white)
        songtype = smallfont.render("song?", True, white)
        start = bigfont.render("start?", True, yellow)
        
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill(black)
        
        pressenter = smallfont.render("Push Enter to select", True, yellow)
        pressescape = smallfont.render("Push escape to go back", True, yellow)
        
        song = "null"
        
        self.index = 0
        #used for animations
        
        self.select = 0
        
        self.P1 = 0
        
        self.bgm = 0
        
        while True:
        
        
            #input part
            for event in pygame.event.get():
                
                #quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.select == 0:
                            self.P1 -= 1  
                        if self.select == 1:
                            self.bgm -= 1
                    if event.key == pygame.K_RIGHT:
                        if self.select == 0:
                            self.P1 += 1  
                        if self.select == 1:
                            self.bgm += 1
                    if event.key == pygame.K_ESCAPE:
                        self.select -= 1
                    if event.key == pygame.K_RETURN:
                        self.select += 1
            
            songtxt = smallfont.render(song, True, white)
            #a bit of logic
            if self.P1 > 2:
                self.P1 = 0
            if self.P1 < 0:
                self.P1 = 2
            if self.select < 0:
                self.select = 0
            if self.bgm < 0:
                self.bgm = 1
            if self.bgm > 3:
                self.bgm = 3
            
            if self.select > 2:
                Fight = battle(self.P1,self.bgm)
            
        #-----update part------
            
            #must come first
            screen.blit(background,(0,0))
            
            if self.P1 == 0:
                screen.blit(scaleImage(ship, 10),(200,500))
            if self.P1 == 1:
                screen.blit(scaleImage(ship2, 10),(235,525))
            if self.P1 == 2:
                screen.blit(scaleImage(ship3, 10),(220,550))
            if self.select > 0:
                screen.blit(songtxt,(600,150))
                screen.blit(songtype, (600,100))
            screen.blit(P1,(200,400))
            
            if self.select == 0:
            
                screen.blit(scaleImage(pygame.transform.rotate(arrow, 180), 2), (150,650))
                screen.blit(scaleImage(arrow, 2), (400,650))
            
            if self.select == 1:
            
                screen.blit(scaleImage(pygame.transform.rotate(arrow, 180), 2), (750,150))
                screen.blit(scaleImage(arrow, 2), (550,150))
            
            if self.index % 8 and self.select == 0:
                screen.blit(scaleImage(pygame.transform.rotate(arrow, 90), 4), (260,700))
            
            elif self.select == 0:
                screen.blit(scaleImage(pygame.transform.rotate(arrow, 90), 4), (260,715))
            
            if self.index % 8 and self.select == 1:
                screen.blit(scaleImage(pygame.transform.rotate(arrow, 90), 4), (600,170))
            
            elif self.select == 1:
                screen.blit(scaleImage(pygame.transform.rotate(arrow, 90), 4), (600,185))
                
            if self.select > 1:
                screen.blit(start,(700,500))
            
            if self.bgm == 1:
                song = "Hacker Duel"
            if self.bgm == 2:
                song = "Neon Trip"
            if self.bgm == 3:
                song = "Space combat"
            
            screen.blit(pressenter,(100,100))
            screen.blit(pressescape,(100,200))
            
            pygame.display.flip()
            
            clock.tick(24)
            
            self.index += 1
            
            
            
if __name__ == "__main__":
    #runs when game run
    setup()
    
    Menu = menu()
    
    
    
    
