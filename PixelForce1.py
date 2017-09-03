
import pygame
import math
import random

pygame.init()

window = pygame.display.set_mode((1280,700))

pygame.display.set_caption("Pixel Force Zombies")

BLACK = (0,0,0)
WHITE=(255,255,255)
RED = (255,0,0)
moveX = 0
moveY = 0
bulletX = 0
bulletY = 0



clock = pygame.time.Clock()
direction = 'right'
bulletalive = 'no'
shoot = 'no'

##class M1911:
##    def __init__(self,x,y):
##        self.x=x
##        self.y=y
##        self.width=50
##        self.height=50
##        self.i0 = pygame.image.load('Military(right.1_M1911).png')
##        self.i1 = pygame.image.load('Military(right.2_M1911).png')
##        self.i2 = pygame.image.load('Military(right.3_M1911).png')
##        self.i3 = pygame.image.load('Military(left.1_M1911).png')
##        self.i4 = pygame.image.load('Military(left.2_M1911).png')
##        self.i5 = pygame.image.load('Military(left.3_M1911).png')
##        self.timeTarget=10
##        self.timeNum=0
##        self.currentImage=0
##    def update(self):
##        self.timeNum+=1
##        if self.timeNum==self.timeTarget:
##            if self.currentImage==2:
##                self.currentImage=0
##            else:
##                self.currentImage+=1
##            self.timeNum=0
##        self.render()
##    def render(self):
##        if self.currentImage==0:
##            window.blit(self.i0, (self.x,self.y))
##        elif self.currentImage==1:
##            window.blit(self.i1, (self.x,self.y))
##        elif self.currentImage==2:
##            window.blit(self.i2, (self.x,self.y))

class Commando(pygame.sprite.Sprite):
    def __init__(self):
     
        pygame.sprite.Sprite.__init__(self)
        
        self.i0 = pygame.image.load('Military(right.1_Commando).png')
        self.rect = self.i0.get_rect()
        self.i1 = pygame.image.load('Military(right.2_Commando).png')
        self.rect = self.i1.get_rect()
        self.i2 = pygame.image.load('Military(right.3_Commando).png')
        self.rect = self.i2.get_rect()
        self.i3 = pygame.image.load('Military(left.1_Commando).png')
        self.rect = self.i3.get_rect()
        self.i4 = pygame.image.load('Military(left.2_Commando).png')
        self.rect = self.i4.get_rect()
        self.i5 = pygame.image.load('Military(left.3_Commando).png')
        self.rect = self.i5.get_rect()
        
        self.i6 = pygame.image.load('Military(back.1_Commando).png')
        self.rect = self.i6.get_rect()
        self.i7 = pygame.image.load('Military(back.2_Commando).png')
        self.rect = self.i7.get_rect()
        self.i8 = pygame.image.load('Military(front.1_Commando).png')
        self.rect = self.i8.get_rect()
        self.i9 = pygame.image.load('Military(front.2_Commando).png')
        self.rect = self.i9.get_rect()
        self.i10 = pygame.image.load('Military(rightshoot.1.0_Commando).png')
        self.rect = self.i10.get_rect()
        self.i11 = pygame.image.load('Military(rightshoot.1.1_Commando).png')
        self.rect = self.i11.get_rect()
        self.i12 = pygame.image.load('Military(rightshoot.2.0_Commando).png')
        self.rect = self.i12.get_rect()
        self.i13 = pygame.image.load('Military(rightshoot.2.1_Commando).png')
        self.rect = self.i13.get_rect()

        self.i14 = pygame.image.load('Military(rightshoot.3.0_Commando).png')
        self.rect = self.i14.get_rect()
        self.i15 = pygame.image.load('Military(rightshoot.3.1_Commando).png')
        self.rect = self.i15.get_rect()
        
        self.i16 = pygame.image.load('Military(leftshoot.1.0_Commando).png')
        self.rect = self.i16.get_rect()
        self.i17 = pygame.image.load('Military(leftshoot.1.1_Commando).png')
        self.rect = self.i17.get_rect()
        self.i18 = pygame.image.load('Military(leftshoot.2.0_Commando).png')
        self.rect = self.i18.get_rect()
        self.i19 = pygame.image.load('Military(leftshoot.2.1_Commando).png')
        self.rect = self.i19.get_rect()
        self.i20 = pygame.image.load('Military(leftshoot.3.0_Commando).png')
        self.rect = self.i20.get_rect()
        self.i21 = pygame.image.load('Military(leftshoot.3.1_Commando).png')
        self.rect = self.i21.get_rect()
        
        self.i22 = pygame.image.load('Military(frontshoot.1.0).png')
        self.rect = self.i22.get_rect()
        self.i23 = pygame.image.load('Military(frontshoot.1.1).png')
        self.rect = self.i23.get_rect()
        self.i24 = pygame.image.load('Military(frontshoot.2.0).png')
        self.rect = self.i24.get_rect()
        self.i25 = pygame.image.load('Military(frontshoot.2.1).png')
        self.rect = self.i25.get_rect()
        
        self.i26 = pygame.image.load('Military(backshoot.1.0).png')
        self.rect = self.i26.get_rect()
        self.i27 = pygame.image.load('Military(backshoot.1.1).png')
        self.rect = self.i27.get_rect()
        self.i28 = pygame.image.load('Military(backshoot.2.0).png')
        self.rect = self.i28.get_rect()
        self.i29 = pygame.image.load('Military(backshoot.2.1).png')
        self.rect = self.i29.get_rect()
        
        self.timeTarget=10
        self.timeNum=0
        self.currentImage=0
        
    def update(self):
        
        self.timeNum+=1
        if self.timeNum==self.timeTarget:
            if self.currentImage==5:
                self.currentImage=0
            else:
                self.currentImage+=1
            self.timeNum=0
        self.render()
    
    def render(self):
        if shoot == 'no':
            if direction == 'right':
                if self.currentImage==0:
                    window.blit(self.i0, (self.rect.x,self.rect.y))
                elif self.currentImage==1:
                    window.blit(self.i1, (self.rect.x,self.rect.y))
                elif self.currentImage==2:
                    window.blit(self.i2, (self.rect.x,self.rect.y))
                elif self.currentImage==3:
                    window.blit(self.i0, (self.rect.x,self.rect.y))
                elif self.currentImage==4:
                    window.blit(self.i1, (self.rect.x,self.rect.y))
                elif self.currentImage==5:
                    window.blit(self.i2, (self.rect.x,self.rect.y))
                    
            if direction == 'left':
                if self.currentImage==0:
                    window.blit(self.i3, (self.rect.x,self.rect.y))
                elif self.currentImage==1:
                    window.blit(self.i4, (self.rect.x,self.rect.y))
                elif self.currentImage==2:
                    window.blit(self.i5, (self.rect.x,self.rect.y))
                elif self.currentImage==3:
                    window.blit(self.i3, (self.rect.x,self.rect.y))
                elif self.currentImage==4:
                    window.blit(self.i4, (self.rect.x,self.rect.y))
                elif self.currentImage==5:
                    window.blit(self.i5, (self.rect.x,self.rect.y))
                
            if direction == 'up':
                if self.currentImage==0:
                    window.blit(self.i6, (self.rect.x,self.rect.y))
                elif self.currentImage==1:
                    window.blit(self.i7, (self.rect.x,self.rect.y))
                elif self.currentImage==2:
                    window.blit(self.i6, (self.rect.x,self.rect.y))
                if self.currentImage==3:
                    window.blit(self.i7, (self.rect.x,self.rect.y))
                elif self.currentImage==4:
                    window.blit(self.i6, (self.rect.x,self.rect.y))
                elif self.currentImage==5:
                    window.blit(self.i7, (self.rect.x,self.rect.y))
                    
            if direction == 'down':
                if self.currentImage==0:
                    window.blit(self.i8, (self.rect.x,self.rect.y))
                elif self.currentImage==1:
                    window.blit(self.i9, (self.rect.x,self.rect.y))
                elif self.currentImage==2:
                    window.blit(self.i8, (self.rect.x,self.rect.y))
                elif self.currentImage==3:
                    window.blit(self.i9, (self.rect.x,self.rect.y))
                elif self.currentImage==4:
                    window.blit(self.i8, (self.rect.x,self.rect.y))
                elif self.currentImage==5:
                    window.blit(self.i9, (self.rect.x,self.rect.y))
                    

                    
        elif shoot == 'yes':
            if direction == 'right':
                if self.currentImage==0:
                    window.blit(self.i10, (self.rect.x,self.rect.y))
                elif self.currentImage==1:
                    window.blit(self.i11, (self.rect.x,self.rect.y))
                elif self.currentImage==2:
                    window.blit(self.i12, (self.rect.x,self.rect.y))
                elif self.currentImage==3:
                    window.blit(self.i13, (self.rect.x,self.rect.y))
                elif self.currentImage==4:
                    window.blit(self.i14, (self.rect.x,self.rect.y))
                elif self.currentImage==5:
                    window.blit(self.i15, (self.rect.x,self.rect.y))
                    
            if direction == 'left':
                if self.currentImage==0:
                    window.blit(self.i16, (self.rect.x,self.rect.y))
                elif self.currentImage==1:
                    window.blit(self.i17, (self.rect.x,self.rect.y))
                elif self.currentImage==2:
                    window.blit(self.i18, (self.rect.x,self.rect.y))
                elif self.currentImage==3:
                    window.blit(self.i19, (self.rect.x,self.rect.y))
                elif self.currentImage==4:
                    window.blit(self.i20, (self.rect.x,self.rect.y))
                elif self.currentImage==5:
                    window.blit(self.i21, (self.rect.x,self.rect.y))
                    
            if direction == 'down':
                if self.currentImage==0:
                    window.blit(self.i22, (self.rect.x,self.rect.y))
                elif self.currentImage==1:
                    window.blit(self.i23, (self.rect.x,self.rect.y))
                elif self.currentImage==2:
                    window.blit(self.i24, (self.rect.x,self.rect.y))
                elif self.currentImage==3:
                    window.blit(self.i25, (self.rect.x,self.rect.y))
                elif self.currentImage==4:
                    window.blit(self.i22, (self.rect.x,self.rect.y))
                elif self.currentImage==5:
                    window.blit(self.i23, (self.rect.x,self.rect.y))
                    
            if direction == 'up':
                if self.currentImage==0:
                    window.blit(self.i26, (self.rect.x,self.rect.y))
                elif self.currentImage==1:
                    window.blit(self.i27, (self.rect.x,self.rect.y))
                elif self.currentImage==2:
                    window.blit(self.i28, (self.rect.x,self.rect.y))
                elif self.currentImage==3:
                    window.blit(self.i29, (self.rect.x,self.rect.y))
                elif self.currentImage==4:
                    window.blit(self.i26, (self.rect.x,self.rect.y))
                elif self.currentImage==5:
                    window.blit(self.i27, (self.rect.x,self.rect.y))


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Bullet.png')
        self.rect = self.image.get_rect()
        
    def update(self):
        if direction == 'left':
            self.rect.x -= 10
            window.blit(self.image, (self.rect.x,self.rect.y))
        elif direction == 'right':
            self.rect.x += 10
            window.blit(self.image, (self.rect.x,self.rect.y))
        elif direction == 'up':
            self.rect.y -= 10
            window.blit(self.image, (self.rect.x,self.rect.y))
        elif direction == 'down':
            self.rect.y += 10
            window.blit(self.image, (self.rect.x,self.rect.y))

all_sprites_list = pygame.sprite.Group()
zombie_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()


##PlayerBulletRIGHT = Bullet()
##PlayerBulletRIGHT.x = int(Player1.x) + 38
##PlayerBulletRIGHT.y = int(Player1.y) + 21
##PlayerBulletRIGHT.change_x = 0
##PlayerBulletRIGHT.change_y = 0
##PlayerBulletRIGHT.color = [0,0,0]

##class M1911:
##    def __init__(self,x,y):
##        self.x=x
##        self.y=y
##        self.width=50
##        self.height=50
##        self.i0 = pygame.image.load('Military(right.1_M1911).png')
##        self.i1 = pygame.image.load('Military(right.2_M1911).png')
##        self.i2 = pygame.image.load('Military(right.3_M1911).png')
##        self.i3 = pygame.image.load('Military(left.1_M1911).png')
##        self.i4 = pygame.image.load('Military(left.2_M1911).png')
##        self.i5 = pygame.image.load('Military(left.3_M1911).png')
##        self.timeTarget=10
##        self.timeNum=0
##        self.currentImage=0
##def update(self):
##        self.timeNum+=1
##        if self.timeNum==self.timeTarget:
##            if self.currentImage==2:
##                self.currentImage=0
##            else:
##                self.currentImage+=1
##            self.timeNum=0
##        self.render()
##    def render(self):
##        if self.currentImage==0:
##            window.blit(self.i0, (self.x,self.y))
##        elif self.currentImage==1:
##            window.blit(self.i1, (self.x,self.y))
##        elif self.currentImage==2:
##            window.blit(self.i2, (self.x,self.y))


gun = 'Commando'


if gun == 'M1911':
    player=M1911(100,150)
elif gun == 'Commando':
    player=Commando()
    all_sprites_list.add(player)
    bullet=Bullet()
    all_sprites_list.add(bullet)
##    bullet = Bullet(0,0)
##    bullet.x = int(player.x) + 38
##    bullet.y = int(player.y) + 21

gameLoop=True
while gameLoop:

##    if gun == 'M1911':
##        player=M1911(100,150)
##    elif gun == 'Commando':
##        player=Commando(player.x,player.y)
##        bullet = Bullet(0,0)
##        bullet.x = int(player.x) + 38
##        bullet.y = int(player.y) + 21
    
##    if gun == 'Commando':
##        bullet = Bullet(0,0)
##        bullet.x = int(player.x) + 38
##        bullet.y = int(player.y) + 21
##LOL
        
    for event in pygame.event.get():
        if (event.type==pygame.QUIT):
            gameLoop=False
        if (event.type==pygame.KEYDOWN):
            keys = pygame.key.get_pressed()
                
            if keys[pygame.K_LEFT]:
                moveX = -3
                direction = 'left'
                if keys[pygame.K_q]:
                    shoot = 'yes'
                    bullet = Bullet()
                    bullet.rect.x = player.rect.x
                    bullet.rect.y = player.rect.y
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)
                
    
                
            if keys[pygame.K_RIGHT]:
                moveX = 3
                direction = 'right'
                if keys[pygame.K_q]:
                    shoot = 'yes'
                    bullet = Bullet()
                    bullet.rect.x = player.rect.x
                    bullet.rect.y = player.rect.y
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)
                
    
            if keys[pygame.K_UP]:
                moveY = -3
                direction = 'up'
                if keys[pygame.K_q]:
                    shoot = 'yes'
                    bullet = Bullet()
                    bullet.rect.x = player.rect.x
                    bullet.rect.y = player.rect.y
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)
                
         
            if keys[pygame.K_DOWN]:
                moveY = 3
                direction = 'down'
                if keys[pygame.K_q]: 
                    shoot = 'yes'
                    bullet = Bullet()
                    bullet.rect.x = player.rect.x
                    bullet.rect.y = player.rect.y
##                    bullet.rect.x += 
                    all_sprites_list.add(bullet)
                    bullet_list.add(bullet)
                
 
                
    
        if (event.type==pygame.KEYUP):
            if (event.key==pygame.K_LEFT):
                moveX=0
            if (event.key==pygame.K_RIGHT):
                moveX=0
            if (event.key==pygame.K_UP):
                moveY=0
            if (event.key==pygame.K_DOWN):
                moveY=0
            if (event.key==pygame.K_q):
                shoot = 'no'
                
    all_sprites_list.update()               
                    
    
    window.fill(WHITE)
    
##    bullet.y+=BulletY
##    bullet.x+=BulletX
   
##    bullet.update()
    
##    bullet.rect.x+=bulletX
##    bullet.rect.y+=bulletY
    bullet.update()
    player.rect.x+=moveX
    player.rect.y+=moveY
    player.update()
    
    pygame.display.flip()
    clock.tick(50)

    
pygame.quit()



