# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:09:48 2018

@author: Rebecca
"""

def load_knapsack(things,knapsack_cap):
    """                          
    Reference: RosettaCode.org - dynamic programming solutions for knapsack problem                        
    """
        
    my_team_number_or_name = "rswood"     
    items_to_pack = []
    load = 0         
    #value = 0           
        
    n = len(things)
    
    knapsack_cap = int(knapsack_cap)
    items = things.keys()
    wt = []
    val = []
    for key in items:
        wt.append(things.get(key)[0])
        val.append(things.get(key)[1])
    
    table = [[0 for w in range(knapsack_cap+1)] for j in range(n+1)]
    
    for j in range(1, n+1):
        a = int(wt[j-1])
        b = int(val[j-1])
        for w in range(1, knapsack_cap+1):
            if a > w:
                table[j][w] = table[j-1][w]
            else:
                table[j][w] = max(table[j-1][w], table[j-1][w-a] + b)

    for j in range(n, 0, -1):
        if table[j][w] != table[j-1][w]:
            item = things.keys()
            wt = []
            val = []
            for key in items:
                wt.append(things.get(key)[0])
                val.append(things.get(key)[1])
            if load + int(wt[j-1]) <= knapsack_cap:
                items_to_pack.append(item[j-1])
                load += int(wt[j-1])
    
    return my_team_number_or_name, items_to_pack  