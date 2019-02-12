# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 09:25:01 2019

@author: ED
"""

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
n1  = 0.75
n2  = 1
n3  = 0.5
n4  = 0.25


#variable to count how many times you had to roll the dice each game
countList = []

play = 0
yeet = 1

#how may times do you want to play the game ?
while ( play<10000000) :
    
    #probability array of the out comes
    prob = np.array([n1 , n2 , n3 , n4])
#    print (prob)
    
    
    #Flags for cards 1:12 #note 0 means face up
    c1 = c2 = c3 = c4 = 0 
    
    card = np.array([c1 , c2 , c3 , c4 ])
#    print (card)
    
    #setup for d6
    dmin = 1
    dmax = 2
    
    #chose which card to flip
    
    listf = [1,2,3];
    count = 0
    

    while ( sum(card) < 4) :
        n1  = 0.75
        n2  = 1
        n3  = 0.5
        n4  = 0.25
        
        count = count + 1 
        x = random.randint(dmin,dmax) 
        y = random.randint(dmin,dmax) 
        z = x+y 
        
        

        options = [x,y,z]
      #  print(options)
        
        p1 = (prob[(x-1)])
        p2 = (prob[(y-1)])
        p3 = (prob[(z-1)])
        
        listf[0] = p1
        listf[1] = p2
        listf[2] = p3
        
        
            ##this picks which card is best to flip
        tester = listf.index(min(listf))
        
        yeet = options[tester] -1
#        print(GG)
        
        
        if card[(yeet)] == 0:
          
            card[(yeet)] = 1
            
        else:
           
            listf[listf.index(min(listf))] = 1.1;
            
            yeet = options[listf.index(min(listf))] -1; 
                
            if card[(yeet)] == 0:
                     
                card[(yeet)] = 1
                     
            else:
                listf[listf.index(min(listf))] = 1.1;
                yeet = options[listf.index(min(listf))] -1; 
                
                if card[(yeet)] == 1:
                    card[(yeet)] = 0
                else:
                    card[(yeet)] = 1
                
    countList.append(count)
  
    play = play+1

    
    
    
    
    
    
    
    
#print(countList)#    


fc = sum(countList)

fclen = len(countList)

ANS = fc/fclen
print(ANS)















