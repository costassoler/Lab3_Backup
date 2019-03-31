
# coding: utf-8

# In[1]:


import numpy as np

def Filter (Freq, Sig, Bounds):
    '''
    This lets you create multiple pass filters. Each entry in bounds 
    represents a window of frequencies you'd like to let through.
    #######################################################################
    Arguments:
    Freq = your frequencies array
    Sig = your signal array
    Bounds = an nx1 matrix, where each entry is a 2-element array. The first entry 
    and the second entry in those arrays represent the lower bound and upper bound (respectively)
    of your window
    Returns: Your filtered spectrum'''
    
    FILT = np.zeros((len(Sig)))
    for n in range (0,len(Bounds)):
        for i in range (0,len(Sig)):
            if (Freq[i]>Bounds[n][0]) and (Freq[i]<Bounds[n][1]):
                FILT[i] = Sig[i]
    return FILT
        

