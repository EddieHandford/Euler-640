# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 11:32:05 2019

@author: ED
"""



#
# Bob plays a single-player game of chance using two standard 6-sided dice and 
# twelve cards numbered 1 to 12. When the game starts, all cards are placed face
# up on a table.
#
# Each turn, Bob rolls both dice, getting numbers x and y respectively, each in
# the range 1,...,6. He must choose amongst three options: turn over card x, 
# card y, or card x+y. (If the chosen card is already face down, it is turned 
# to face up, and vice versa.)
#
# If Bob manages to have all twelve cards face down at the same time, he wins.
#
# Alice plays a similar game, except that instead of dice she uses two fair 
# coins, counting heads as 2 and tails as 1, and that she uses four cards instead
# of twelve. Alice finds that, with the optimal strategy for her game, the 
# expected number of turns taken until she wins is approximately 5.673651.
#
# Assuming that Bob plays with an optimal strategy, what is the expected number
# of turns taken until he wins? Give your answer rounded to 6 places after the
# decimal point.
#





import random
import numpy as np


#probability lookup table
n0  = 0.99
n1  = 11/36
n2  = 12/36
n3  = 13/36
n4  = 14/36
n5  = 15/36
n6  = 16/36
n7  = 6/36
n8  = 5/36
n9  = 4/36
n10 = 3/36
n11 = 2/36
n12 = 1/36


countList = []


#how may times do you want to play the game ?
play = 0

while ( play<10000000) :
    
    prob = np.array([n0 , n1 , n2 , n3 , n4 , n5 , n6 , n7 , n8 , n9 , n10 , n11 , n12])
    #n0 is a dud to help with dice rolling code ease of viewing later
#    print (prob)
    
    
    #Flags for cards 1:12 #note 0 means face up
    c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c10 = c11 = c12  = 0 
    c0 = 0;
    #note c0 is a dud , to help make the code easier to read later on
    
    card = np.array([c0 , c1 , c2 , c3 , c4 , c5 , c6, c7 , c8 , c9 , c10 , c11 , c12])
#    print (card)
    
    #setup for d6
    dmin = 1
    dmax = 6
    
    #chose which card to flip
    
    listf = [1,2,3];
    count = 0
    

    while ( sum(card) < 12) :
        count = count + 1 
        x = random.randint(dmin,dmax)
        y = random.randint(dmin,dmax)
        z = x+y
        
        

        options = [x,y,z]
      #  print(options)
        
        p1 = (prob[(x)])
        p2 = (prob[(y)])
        p3 = (prob[(z)])
        
        listf[0] = p1
        listf[1] = p2
        listf[2] = p3
        
        
            ##this picks which card is best to flip
        GG = options[listf.index(min(listf))];
#        print(GG)
        if card[GG] == 0:
          
            card[GG] = 1
            
        else:
           
            listf[listf.index(min(listf))] = 1;
            
            GG = options[listf.index(min(listf))]; 
                
            if card[GG] == 0:
                     
                card[GG] = 1
                     
            else:
                listf[listf.index(min(listf))] = 1;
                GG = options[listf.index(min(listf))]; 
                
                if card[GG] == 1:
                    card[GG] = 0
                else:
                    card[GG] = 1
                
        
        
        
        
        
#        
#        print('yo mamma')
#        print(GG)
#    print (card)
#    #
    countList.append(count)
  
    play = play+1
 #print(play)
    
    
    
    
    
    
    
    
#print(countList)#    


fc = sum(countList)

fclen = len(countList)

ANS = fc/fclen
print(ANS)















