
# coding: utf-8

# In[ ]:

import numpy as np

def FringeAmplitude(Hs,B,dec):
    FA = []
    lam = (3*10**8)/(10.7*10**9)
    for i in range(0,len(Hs)):
        Q = (np.cos(dec)*B/lam)
        F = np.cos(2*np.pi*Q*np.sin(Hs[i]))#+B*np.sin(2*p.pi*Q*np.sin(Hs[i])), A = 1
        FA.append(F)
    return np.array(FA)

def BestFitBaseline(Hs,Data,GuessMin,GuessMax,inc):
    Guesses = np.arange(GuessMin,GuessMax,inc)
    S=[]
    for j in range (0, len(Guesses)):
        FAmps = FringeAmplitude(Hs,Guesses[j])
        Square = 0
        for i in range(0,len(FAmps)):
            Square+=(Data[j]-FAmps[j])**2
        S.append(Square)
            

