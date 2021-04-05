
# coding: utf-8

# In[1]:
################################################
# AI Assignment 2
# Rakesh Rawat MT17046
# compairison between MIN MAX and ALPHA BETA for 
# Tic-Tac-Toe game 
################################################

from copy import deepcopy
import time


# In[2]:


f = {1:(0,0) , 2:(0,1) , 3:(0,2) , 4:(1,0) , 5:(1,1) , 6:(1,2) , 7:(2,0) , 8:(2,1) , 9:(2,2)}


# In[3]:


def neighbors(grid,ch):
    m = len(grid[0])
    
    sol = []
    
    for i in range(0,m):
        for j in range(0,m):
            if grid[i][j]>=1 and grid[i][j]<=9:
                s = deepcopy(grid)
                s[i][j] = ch
                sol.append(s)
                
    return sol


# In[4]:


def display(grid):
    print " ____________"
    for i in [0,1,2]:
            print "| "+str(grid[i][0])+" | "+str(grid[i][1])+" | "+str(grid[i][2])+" |"
            print " ___________"
        
    print " "


# In[5]:


def win(grid,ch):
    
    reward = 0
    if ch=='X':
        reward = 1
    else:
        reward = -1
        
    # diagonal
    if grid[0][0]==ch and grid[1][1]==ch and grid[2][2]==ch:
        return reward
    if grid[0][2]==ch and grid[1][1]==ch and grid[2][0]==ch:
        return reward
    
    #  horizontal
    
    if grid[0][0]==ch and grid[0][1]==ch and grid[0][2]==ch:
        return reward
    if grid[1][0]==ch and grid[1][1]==ch and grid[1][2]==ch:
        return reward
    if grid[2][0]==ch and grid[2][1]==ch and grid[2][2]==ch:
        return reward
    
    #  vertical
    
    if grid[0][0]==ch and grid[1][0]==ch and grid[2][0]==ch:
        return reward
    if grid[0][1]==ch and grid[1][1]==ch and grid[2][1]==ch:
        return reward
    if grid[0][2]==ch and grid[1][2]==ch and grid[2][2]==ch:
        return reward
    
    return 0


# In[6]:


def MIN(grid):
    
    global nodes_expanded
    nodes_expanded+=1
    
    if win(grid,'X'):
        return 1,grid,"win-x"
    utility = 1e9
    s = None
    nodes = neighbors(grid,'O')
    
    if len(nodes)==0:
        return 0,grid,"draw"
    
    for state in nodes:
        
        res,_,l = MAX(state)
        if utility > res:
            utility = res
            s = state
        
    return utility,s,None


# In[7]:


def MAX_prune(grid,alpha,beta):
    
    global nodes_expanded
    nodes_expanded+=1
    
    if win(grid,'O'):
        return -1,grid,"win-o"
    utility = -1e9
    s = None
    nodes = neighbors(grid,'X')
    if len(nodes)==0:
        return 0,grid,"draw"
    for state in nodes:
        
        res,_,l = MIN_prune(state,alpha,beta)
        if utility < res :
            utility = res
            s = state
        if utility>=beta:
            return utility,s,None
        alpha = max(alpha,utility)
        
    return utility,s,None


# In[8]:


def MIN_prune(grid,alpha,beta):
    
    global nodes_expanded
    nodes_expanded+=1
    
    if win(grid,'X'):
        return 1,grid,"win-x"
    utility = 1e9
    s = None
    nodes = neighbors(grid,'O')
    
    if len(nodes)==0:
        return 0,grid,"draw"
    
    for state in nodes:
        
        res,_,l = MAX_prune(state,alpha,beta)
        if utility > res:
            utility = res
            s = state
        if utility<=alpha:
            return utility,s,None
        beta = min(beta,utility)
            
        
    return utility,s,None


# In[9]:


def MAX(grid):
    
    global nodes_expanded
    nodes_expanded+=1
    
    if win(grid,'O'):
        return -1,grid,"win-o"
    utility = -1e9
    s = None
    nodes = neighbors(grid,'X')
    if len(nodes)==0:
        return 0,grid,"draw"
    for state in nodes:
        
        res,_,l = MIN(state)
        if utility < res :
            utility = res
            s = state
        
    return utility,s,None


# In[10]:


nodes_expanded = None

def game():  
    grid = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
    global f,nodes_expanded
    while True:
        
        display(grid)
        option = int(raw_input())
        
        i = f[option]
        grid[i[0]][i[1]] = 'X'
        
        nodes_expanded = 0
        start_time = time.time()
        _,grid,res = MIN_prune(grid,-1e9,1e9)
        #_,grid,res = MIN(grid)
        
        print "Time : "+str(time.time()-start_time)
        print "Nodes Expanded : "+str(nodes_expanded)
        print "\n"
        
        if res=='win-x':
            display(grid)
            print "X wins"
            break
        if res==0 or res=="draw":
            display(grid)
            print "draw"
            break
        if res=='win-o' or win(grid,'O')==-1:
            display(grid)
            print "O wins"
            break

        
game()    

