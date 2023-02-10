# This is a bowling module to calculate the bowlscore of players using certain rules :
"""
1. Each wicket   - 10
2. Three wickets - 5
3. Five or more  wickets  - 10
4. Economy rate b/w 3.5 & 4.5 - 4
5. Economy rate b/w 2 & 3.5 -7
6. Economy rate less than 2 -10
"""


#Function for each wicket 
def wicket(a):
    b_w=a*10
    if((a-3)>0):
        b_w+=5
    if(a-5>10):
        b_w+=10
        
    return b_w
    
    
#Function for economy rate 
def economy(runs,overs):
    b_ec=0
    econ=runs/overs
    if(econ>=3.5 and econ<4.5):
        b_ec+=4
    elif(econ>=2 and econ<3.5):
        b_ec+=7
    elif(econ<2):
        b_ec+=10
    else:
        b_ec+=0
    
    return b_ec
    
