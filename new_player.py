# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 20:34:46 2018

@author: v-beshi
"""

import pandas as pd
import random as rd
import numpy as np

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
columns=['name','pot','shot','str','spe','dri','pas','head','tac','mind','GK']
pot=[1]+[2]*2+[3]*2+[4]*3+[5]*5+[6]*4+[7]*3+[8]*2+[9]*2+[10]*1
beta=range(10)

def create_new(num): 
    free=[]
    if num==1:
        free_name='{0}{1}{2}{3}'.format(rd.sample(alpha,1)[0],rd.sample(alpha,1)[0],rd.sample(beta,1)[0],rd.sample(beta,1)[0])
        free_pot=rd.sample(pot,1)[0]
        free_shot=rd.sample(pot,1)[0]
        free_str=rd.sample(pot,1)[0]
        free_spe=rd.sample(pot,1)[0]
        free_dri=rd.sample(pot,1)[0]
        free_pas=rd.sample(pot,1)[0]
        free_head=rd.sample(pot,1)[0]
        free_tac=rd.sample(pot,1)[0]
        free_mind=rd.sample(pot,1)[0]
        free_GK=rd.sample(pot,1)[0]
        free_man=[free_name,free_pot,free_shot,free_str,free_spe,free_dri,free_pas,free_head,free_tac,free_mind,free_GK]
        player_list=pd.DataFrame([free_man],columns=columns)
    else:
        for i in range(num):
            
            free_name='{0}{1}{2}{3}'.format(rd.sample(alpha,1)[0],rd.sample(alpha,1)[0],rd.sample(beta,1)[0],rd.sample(beta,1)[0])
            free_pot=rd.sample(pot,1)[0]
            free_shot=rd.sample(pot,1)[0]
            free_str=rd.sample(pot,1)[0]
            free_spe=rd.sample(pot,1)[0]
            free_dri=rd.sample(pot,1)[0]
            free_pas=rd.sample(pot,1)[0]
            free_head=rd.sample(pot,1)[0]
            free_tac=rd.sample(pot,1)[0]
            free_mind=rd.sample(pot,1)[0]
            free_GK=rd.sample(pot,1)[0]
            free_mann=[free_name,free_pot,free_shot,free_str,free_spe,free_dri,free_pas,free_head,free_tac,free_mind,free_GK]
            free.append(free_mann)
        player_list=pd.DataFrame(free,columns=columns)
    player_list['Total']=player_list['pot']+player_list['shot']+player_list['str']+player_list['spe']+player_list['dri']+player_list['pas']+player_list['head']+player_list['tac']+player_list['mind']+player_list['GK']
    return player_list
        
            
    
