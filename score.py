import batting as bt
import Bowling as bo

p1={'name' : 'Virat Kohli' , 'role' : 'bat' , 'runs' :112, '4' :10, '6' :0,'balls' :119, 'field' :0}
p2={'name' : 'du Plessis' , 'role' : 'bat' , 'runs' :120, '4' :11, '6' :2,'balls' :112, 'field' :0}
p3={'name' : 'Bhuvneshwar Kumar' , 'role' : 'bowl' , 'wkts' :1, 'overs' :10,'runs' :71, 'field' :1}
p4={'name' : 'Yuzvendra Chahal' , 'role' : 'bowl' , 'wkts' :2, 'overs' :10,'runs' :45, 'field' :0}
p5={'name' : 'Kuldeep Yadav' , 'role' : 'bowl' , 'wkts' :3, 'overs' :10, 'runs' :34,'field' :0}


#Batscore for player P1
for k,v in p1.items():
    if(k=="name"):
       pname=v
       continue
    elif(k=="role"):
        prole=v
        continue
    elif(k=="runs"):
        run=v
        batscore=bt.tworuns(v)+bt.halfcentury(v)+bt.fullcentury(v)
        continue
    elif(k=="4"):
        batscore+=bt.fours(v)
        continue
    elif(k=="6"):
        batscore+=bt.sixes(v)
        continue
    elif(k=="balls"):
        batscore+=bt.strikerate(run,v)
        
d1={"name":pname ,"bowlscore":batscore}
print(d1)

#Batscore of player P2
for k,v in p2.items():
    if(k=="name"):
       pname=v
       continue
    elif(k=="role"):
        prole=v
        continue
    elif(k=="runs"):
        run=v
        batscore=bt.tworuns(v)+bt.halfcentury(v)+bt.fullcentury(v)
        continue
    elif(k=="4"):
        batscore+=bt.fours(v)
        continue
    elif(k=="6"):
        batscore+=bt.sixes(v)
        continue
    elif(k=="balls"):
        batscore+=bt.strikerate(run,v)
        
d2={"name":pname ,"batscore":batscore}
print(d2)


#bowlscore for player p3
for k,v in p3.items():
    if(k=="name"):
       pname=v
       continue
    elif(k=="role"):
        prole=v
        continue
    elif(k=="wkts"):
        bowlscore=bo.wicket(v)
        continue
    elif(k=="overs"):
        over=v
        continue
    elif(k=="runs"):
        bowlscore+=bo.economy(v,over)
        continue
        
d3={"name":pname ,"bowlscore":bowlscore}
print(d3)


#bowlscore of player p4
for k,v in p4.items():
    if(k=="name"):
       pname=v
       continue
    elif(k=="role"):
        prole=v
        continue
    elif(k=="wkts"):
        bowlscore=bo.wicket(v)
        continue
    elif(k=="overs"):
        over=v
        continue
    elif(k=="runs"):
        bowlscore+=bo.economy(v,over)
        continue

d4={"name":pname ,"bowlscore":bowlscore}
print(d4)



#Bowlscore for player p5
for k,v in p5.items():
    if(k=="name"):
       pname=v
       continue
    elif(k=="role"):
        prole=v
        continue
    elif(k=="wkts"):
        bowlscore=bo.wicket(v)
        continue
    elif(k=="overs"):
        over=v
        continue
    elif(k=="runs"):
        bowlscore+=bo.economy(v,over)
        continue
        
        
d5={"name":pname ,"bowlscore":bowlscore}
print(d5)