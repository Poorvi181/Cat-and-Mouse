import pgzrun,random
import pygame
TITLE="Catch the Mouse"
WIDTH=800
HEIGHT=800
cat=Actor("cat")
cat.pos=100,100
mouse=Actor("mouse")
mouse.pos=200,200
score=0
gameover=False
img=pygame.image.load("Cat and Mouse\images\wood.jpeg")
imagescale=pygame.transform.scale(img,(WIDTH,HEIGHT))
def draw():
    screen.clear()
    screen.blit(imagescale,(0,0))
    cat.draw()
    mouse.draw()
    screen.draw.text("Score:"+str(score),center=(400,30),fontsize=30)
    if gameover:
        screen.fill("black")
        screen.draw.text("Time's up your final score is:"+str(score),midtop=(200,30),fontsize=30,color="white")
def update():
    global score
    if keyboard.left:
        cat.x-=2
    if keyboard.right:
        cat.x+=2
    if keyboard.up:
        cat.y-=2
    if keyboard.down:
        cat.y+=2
    mousecollected=cat.colliderect(mouse)
    if mousecollected:
        mouse.x=random.randint(50,750)
        mouse.y=random.randint(50,750)
        score+=1

def timeup():
    global gameover
    gameover=True

clock.schedule(timeup,60)
pgzrun.go()