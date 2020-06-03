from random import shuffle
from random import randint 
import pygame
pygame.font.init()

cardpngs={'CLUB':{'ACE':pygame.image.load('pcp\\CLUB\\1.png'),2:pygame.image.load('pcp\\CLUB\\2.png'),3:pygame.image.load('pcp\\CLUB\\3.png'),4:pygame.image.load('pcp\\CLUB\\4.png'),5:pygame.image.load('pcp\\CLUB\\5.png'),6:pygame.image.load('pcp\\CLUB\\6.png'),7:pygame.image.load('pcp\\CLUB\\7.png'),8:pygame.image.load('pcp\\CLUB\\8.png'),9:pygame.image.load('pcp\\CLUB\\9.png'),10:pygame.image.load('pcp\\CLUB\\10.png'),'JACK':pygame.image.load('pcp\\CLUB\\J.png'),'QUEEN':pygame.image.load('pcp\\CLUB\\Q.png'),'KING':pygame.image.load('pcp\\CLUB\\K.png')},'DIAMOND':{'ACE':pygame.image.load('pcp\\DIAMOND\\1.png'),2:pygame.image.load('pcp\\DIAMOND\\2.png'),3:pygame.image.load('pcp\\DIAMOND\\3.png'),4:pygame.image.load('pcp\\DIAMOND\\4.png'),5:pygame.image.load('pcp\\DIAMOND\\5.png'),6:pygame.image.load('pcp\\DIAMOND\\6.png'),7:pygame.image.load('pcp\\DIAMOND\\7.png'),8:pygame.image.load('pcp\\DIAMOND\\8.png'),9:pygame.image.load('pcp\\DIAMOND\\9.png'),10:pygame.image.load('pcp\\DIAMOND\\10.png'),'JACK':pygame.image.load('pcp\\DIAMOND\\J.png'),'QUEEN':pygame.image.load('pcp\\DIAMOND\\Q.png'),'KING':pygame.image.load('pcp\\DIAMOND\\K.png')},'HEART':{'ACE':pygame.image.load('pcp\\HEART\\1.png'),2:pygame.image.load('pcp\\HEART\\2.png'),3:pygame.image.load('pcp\\HEART\\3.png'),4:pygame.image.load('pcp\\HEART\\4.png'),5:pygame.image.load('pcp\\HEART\\5.png'),6:pygame.image.load('pcp\\HEART\\6.png'),7:pygame.image.load('pcp\\HEART\\7.png'),8:pygame.image.load('pcp\\HEART\\8.png'),9:pygame.image.load('pcp\\HEART\\9.png'),10:pygame.image.load('pcp\\HEART\\10.png'),'JACK':pygame.image.load('pcp\\HEART\\J.png'),'QUEEN':pygame.image.load('pcp\\HEART\\Q.png'),'KING':pygame.image.load('pcp\\HEART\\K.png')},'SPADE':{'ACE':pygame.image.load('pcp\\SPADE\\1.png'),2:pygame.image.load('pcp\\SPADE\\2.png'),3:pygame.image.load('pcp\\SPADE\\3.png'),4:pygame.image.load('pcp\\SPADE\\4.png'),5:pygame.image.load('pcp\\SPADE\\5.png'),6:pygame.image.load('pcp\\SPADE\\6.png'),7:pygame.image.load('pcp\\SPADE\\7.png'),8:pygame.image.load('pcp\\SPADE\\8.png'),9:pygame.image.load('pcp\\SPADE\\9.png'),10:pygame.image.load('pcp\\SPADE\\10.png'),'JACK':pygame.image.load('pcp\\SPADE\\J.png'),'QUEEN':pygame.image.load('pcp\\SPADE\\Q.png'),'KING':pygame.image.load('pcp\\SPADE\\K.png')}}

WIDTH = 800
HEIGHT = 600
FPS = 30



# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
back_ground = pygame.image.load('pcp\\tablesmall.png')
randomcardsbuttoncover = pygame.image.load('pcp\\buttoncover.png')
cardscover = pygame.image.load('pcp\\cardscover.png')

gameDisplay = screen
pygame.display.set_caption('Card Trick')
gameDisplay.blit(back_ground,(0,0))
clock = pygame.time.Clock()
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)
ORANGE = (255, 154, 0)
YELLOW = (218,200,41)
# Text backgound colours for money, and hand totals!
RED2 = (237,28,36)
GREEN2 = (0, 146, 1)
GREEN3 = (1,111,0)
GREEN4 = (0,134,0)
GREEN5 = (0,123,0)

buttonpressed = 0
def button(x,y,w,h,inactive_color,active_color,msg='',font_size=15,action=None):
    global buttonpressed
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_color,(x,y,w,h))
        if action != None:
            if click[0] == 1:
                if buttonpressed == 0:
                    buttonpressed = 1
                    action()
            if click[0] == 0:
                buttonpressed = 0
            
    else:
        pygame.draw.rect(gameDisplay, inactive_color,(x,y,w,h))

    def text_objects(text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()

    smallText = pygame.font.Font("freesansbold.ttf",font_size)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
        
    

def message_display(text,x,y,font,color=BLACK):
    def text_objects(text, font):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()
    largeText = pygame.font.Font('freesansbold.ttf',font)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center =((x),(y))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.flip()