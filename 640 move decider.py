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





def move_decider (d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12):
    
    c12_out = c12|d12
    c11_out = c11|d11
    c10_out = c10|d10
    c9_out = c9|d9
    c8_out = c8|d8
    c7_out = c7|d7
    
    c6_out = ~(c6|(((d1)&(~c1))|((d2)&(~c2))|((d3)&(~c3))|((d4)&(~c4))|((d5)&(~c5))|((d7)&(~c7))|((d8)&(~c8))|((d9)&(~c9))|((d10)&(~c10))|((d11)&(~c11))|((d12)&(~c12))))
    
    
    c5_out = False
    c4_out = False
    c3_out = False
    c2_out = False
    c1_out = False
    
    
    
    
    
    return(c1_out , c2_out , c3_out , c4_out , c5_out , c6_out , c7_out , c8_out , c9_out ,c10_out , c11_out , c12_out)
    
    
    
    
    
    
    
    
    
    
#d1 = True
#d2 = True
#d3 = True
#d4 = True
#d5 = True
d6 = True
#d7 = True
d8 = True
d9 = True
d10 = True
d11 = True
d12 = True

    


print(move_decider(d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12))