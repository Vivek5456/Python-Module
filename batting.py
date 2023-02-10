#This is a batting module to compute runs of players based on certain rules
"""
1. 2 runs scored  - 1 pts.
2. Half century   - 5 pts.
3. Full century   - 10 pts.
4. Strike rate of 80-100 - 2 pts.
5. Strike rate  > 100 - 4 pts.
6. Fours          - 1 pts.
7. Sixes          -2 pts.
"""

#Function for two runs
def tworuns(a):
    r_2=a//2
    
    return r_2
    
    
#Function for half century
def halfcentury(a):
    if((a-50)>0):
        r_50=5
    else:
        r_50=0
        
    return r_50
    
    
#Function for full century
def fullcentury(a):
    if((a-100)>0):
        r_100=10
    else:
        r_100=0
        
    return r_100


#Function for strike rate 
def strikerate(runs,ball):
    rst=(runs/ball)*100
    if(rst>80 and rst<100):
        r_st=2
    elif(rst>100):
        r_st=4
    else:
        r_st=0
        
    return r_st


#Function for fours 
def fours(fr):
    r_4=1*fr
    
    return r_4
    

#Function for sixes
def sixes(sx):
    r_6=2*sx
    
    return r_6