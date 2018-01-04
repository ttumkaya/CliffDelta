
# coding: utf-8

# In[36]:


import numpy as np

# Pass two "LISTS" to the function to calculate the difference in Cliff's delta.
def cliffDelta(x,y):
    lenx = len(x)
    leny = len(y)
    
    ## generate a matrix full of zeros
    matrix = np.zeros((lenx,leny))
    
    ## compare the two lists and put either 1 or -1 to the matrix (if they are equal, there is already a zero in the matrix) 
    for i in range(lenx):
        for j in range(leny):
            if x[i] > y[j]:
                matrix[i,j] = 1
            elif x[i] < y[j]:
                matrix[i,j] = -1
    
    ## get the avarage of the dominance matrix
    delta = matrix.mean()    
    return delta,matrix
    


# In[39]:


a = [10,10,20,20,20,30,30,30,40,50]
b = [10,20,30,40,40,50]


# In[40]:


delta, matrix = cliffDelta(a,b)
delta

