# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 15:22:26 2018

@author: v-beshi
"""
import new_player

def buy_player(team,player,cost,new_player):
    team['Finance']=team['Finance']-cost
    team['players'].append(new_player.loc[player])
    new_player=new_player.drop([player])
    return 