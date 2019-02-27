# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:41:28 2019

@author: Eddie
"""
#dice state
d1 = False
d2 =False
d3 =False
d4 =False
d5 =False
d6 =False
d7 =False
d8 =False
d9 =False
d10 =False
d11 =False
d12 =False

#card state
c1 = False
c2 = False
c3 = False
c4 = False
c5 = False
c6 = False
c7 = False
c8 = False
c9 = False
c10 = False
c11 = False
c12 = False




#dice state
#d1 = 0 
#d2 = 0
#d3 = 0
#d4 = 0
#d5 = 0
#d6 = 0
#d7 = 0
#d8 = 0
#d9 = 0
#d10 = 0
#d11 = 0
#d12 = 0
#
##card state
#c1 = 0
#c2 = 0
#c3 = 0
#c4 = 0
#c5 = 0
#c6 = 0
#c7 = 0
#c8 = 0
#c9 = 0
#c10 = 0
#c11 = 0
#c12 = 0





def move_decider (d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12):
    
    
    
    
    #c7:12 next states
    c12_out = c12|d12
    c11_out = c11|d11
    c10_out = c10|d10
    c9_out = c9|d9
    c8_out = c8|d8
    c7_out = c7|d7
    
    
    #c6 next state
    c601 =  (d1)&(not(c1))
    c602 =  (d2)&(not(c2))
    c603 =  (d3)&(not(c3))
    c604 =  (d4)&(not(c4))
    c605 =  (d5)&(not(c5))
    c607 =  (d7)&(not(c7))
    c608 =  (d8)&(not(c8))
    c609 =  (d9)&(not(c9))
    c610 = (d10)&(not(c10))
    c611 = (d11)&(not(c11))
    c612 = (d12)&(not(c12))
    c666 = c601|c602|c603|c604|c605|c607|c608|c609|c610|c611|c612
    c6_out = not(c6|c666)
    
    
    
    
    
 
    #c500 = c601|c602|c603|c604|c607|c608|c609|c610|c611|c612
   # c501 = (not(d5))&(not(c500))&(c5)
  #  c502 = (d5&(not(c500))&(not(c5)))
 #   c503 - c5&d6
#    c504 = d5&c500
    
    
    
    
    c5_out = False
    
    
    
    c4_out = False
    c3_out = False
    c2_out = False
    
    
    
    #c1 next state
    c101 = (d1)&(not(d7))&(not(c1))
    c102 = (d1)&(d7)&(not(c1))&(c7)
    c1_out = c1|c101|c102 
    
    
    
    
    
    return(c1_out , c2_out , c3_out , c4_out , c5_out , c6_out , c7_out , c8_out , c9_out ,c10_out , c11_out , c12_out)
    
    
    
    
    
c6 = True
#d1 = True
#d2 = True
#d3 = True
#d4 = True
#d5 = 1
d6 = True
#d7 = True
#d8 = 1
#d9 = 1
#d10 = True
#d11 = 1
#d12 = True
#c12 = True


#c7 = True


    


print(move_decider(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12))