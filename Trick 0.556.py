# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:55:14 2020

@author: Troy
"""
from pg import *

class card:
    def __init__(self,suit,rank):            
        self.suit = suit
        self.rank = rank
        if type(self.rank) == int:
            self.value = rank
        elif self.rank == 'ACE':
            self.value = 11
        else:
            self.value = 10
    def showval(self):
         print('{} of {}'.format(self.rank, self.suit))
    def showcard(self,x,y):
        gameDisplay.blit((cardpngs[self.suit][self.rank]),(x,y))

class deck():

    def __init__(self):
        ranks = [i for i in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
        suits = ['SPADE', 'HEART','DIAMOND','CLUB']

        self.cards = []
        for i in suits:
            for j in ranks:
                self.cards.append(card(i,j))
        self.shuffle()
    def show(self):
        for card in self.cards:
            card.showval()
    def showfifteen(self):
            for card in self.fifteencards:
                card.showval()

    def __len__(self):
        return len(self.cards)
    def shuffle(self):
        shuffle(self.cards)
        print('shuffling the deck!')
    '''
    # def getfifteen(self):
    #     self.cardsleft = [i for i in self.cards]
    #     print(len(self.cardsleft))
    #     shuffle(self.cardsleft)
    #     self.fifteencards = []
    #     while len(self.fifteencards)<51:
    #         self.fifteencards.append(self.cardsleft.pop(randint(0,len(self.cardsleft)-1)))
    #     self.showfifteen()
    #     print(len(self.cardsleft))
'''

    



    

class splitdeck:
    def __init__(self,cardpile):
        self.cards=[i for i in cardpile]
        gameDisplay.blit(back_ground,(0,0))
        for card in cardpile:
            card.showval()
        self.make_piles()
        self.showpiles()
    def make_piles(self):
        
        self.firstpile = []
        self.secondpile = []
        self.thirdpile = []
        
        for j in range (5):
            self.firstpile.append(self.cards.pop(0))
            self.secondpile.append(self.cards.pop(0))
            self.thirdpile.append(self.cards.pop(0))
        
    def showpiles(self):
        self.choice = 0
        cardy=250
        firstpilex = 50
        secondpilex = 300
        thirdpilex=550
        choice= False        
        gameDisplay.blit(back_ground,(0,0))

        for i in self.firstpile:
            i.showcard(firstpilex,cardy)
            firstpilex+=30

        for i in self.secondpile:
            i.showcard(secondpilex,cardy)
            secondpilex+=30        
  
        for i in self.thirdpile:
            i.showcard(thirdpilex,cardy)
            thirdpilex+=30 
    #     i.showval()
        pygame.display.update() 


        while self.choice not in (1,2,3):
            
                
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                button(100,375,100,40,YELLOW,(255, 0, 175),'This pile?',16,self.choice1)
                button(345,375,100,40,YELLOW,(255, 0, 175),'This pile?',16,self.choice2)
                button(600,375,100,40,YELLOW,(255, 0, 175),'This pile?',16,self.choice3)
                message_display('Which pile is your card in?',400,150,20,color=BLACK)
                pygame.display.flip()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print('click!')
                    
    def choice1(self):
        self.choice = 1
        self.redeal()
    def choice2(self):
        self.choice = 2
        self.redeal()
    def choice3(self):
        self.choice = 3
        self.redeal()
    def redeal (self):
        global counter
        global replay
        if self.choice == 1:
            self.cards=self.secondpile+self.firstpile+self.thirdpile
        if self.choice == 2:
            self.cards=self.firstpile+self.secondpile+self.thirdpile
        if self.choice == 3:
            self.cards=self.secondpile+self.thirdpile+self.firstpile
        counter+=1
        while counter==3:
            gameDisplay.blit(back_ground,(0,0))
            self.cards[7].showcard(365,200)
            message_display('This was your card!',400,150,20,color=BLACK)
    
            button(450,350,100,40,YELLOW,(255, 0, 175),'Quit',16,pygame.quit)
            button(250,350,100,40,YELLOW,(255, 0, 175),'replay',16,replay)
    
            pygame.display.flip()
            for event in pygame.event.get():
              
                if event.type == pygame.QUIT:
                    pygame.quit()
        if counter<3:
            self.make_piles()
            self.showpiles()

cardpositions={}
chosen = []

def displayit(cardlist):

    while len( cardpositions)!=52:
        cardx = 43
        cardy=250

        for i in cardlist: 
            cardpositions[i]=(cardx,cardy)
            cardx+=13 
    message_display('choose 15 cards or press the button below to use 15 random cards !',400,100,20,color=BLACK)
    
    for i in cardlist: 
        i.showcard(cardpositions[i][0],cardpositions[i][1])
    
    for event in pygame.event.get():
        if len(chosen)==15:
            button(100,100,250,40,YELLOW,(255, 0, 175),'READY!!',16,got15)
        else:
            button(250,450,250,40,YELLOW,(255, 0, 175),'15 random cards!',16,getrandom15)

        if event.type == pygame.QUIT:
            pygame.quit()
        # button(250,450,250,40,YELLOW,(255, 0, 175),'15 random cards!',16,None)
        # message_display('choose 15 cards or press the button below to use 15 random cards !',400,100,20,color=BLACK)

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in cardlist:    
                if (cardpositions[i][0]< event.pos[0]<cardpositions[i][0]+13) and (cardpositions[i][1]< event.pos[1]<cardpositions[i][1]+85):
                    if cardpositions[i][1]<249:
                        cardpositions[i]=(cardpositions[i][0],cardpositions[i][1]+30)
                        chosen.remove(i)
                    else:
                        cardpositions[i]=(cardpositions[i][0],cardpositions[i][1]-30)
                        chosen.append(i)
                    gameDisplay.blit(back_ground,(0,0))
                    
                for i in cardlist: 
                
                   i.showcard(cardpositions[i][0],cardpositions[i][1])

            
                # aa=(splitdeck(chosen))


counter=0
def getrandom15():
    global chosen
    bb= deck()
    print(chosen)
    while len(chosen)<15:
        chosen.append(bb.cards.pop(randint(0,len(bb.cards)-1)))
    if len(chosen) == 15:
        aa= splitdeck(chosen)

def got15():
    global chosen
    if len(chosen) == 15:
        aa= splitdeck(chosen)

def replay():
    global counter
    global chosen
    global cardpositions
    cardpositions={}
    chosen = []
    counter=0
    tdeck=deck()
    displayit(tdeck.cards)
    
    
    

tdeck=deck()
displayit(tdeck.cards)
while True:
    displayit(tdeck.cards)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


# print("choose a card from the list by just thinking about it")
# ready=input("are you ready?")
# trickdeckdeal = splitdeck(tdeck)