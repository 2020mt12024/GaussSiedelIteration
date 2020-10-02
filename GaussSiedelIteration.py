# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:05:10 2020

@author: SSMOHANTA
"""
import numpy as np

def GSIteration(A,b,s,epsilon,N):
    n=A.shape[0]
    x = np.ones(n)
    t = np.ones(n)
    print("A:")
    print(A)
    print("b:")
    print(b)
    print("s:")
    print(s)
    for m in range(0, N):
        for j in range(0, 3):
            bef = 0
            aft = 0            
            for k in range(0, j):
                bef += A[j,k]*x[k]
            for k in range(j+1, n):
                aft += A[j,k]*t[k]
            x[j] = (1.0/A[j,j])*(b[j] - bef - aft)   
        print("Iteratiion: " + str(m+1))    
        print("x: ")
        print(x)
        print("t: ")
        print(t)
        if(max(abs(x-t)) < epsilon):
            print("Converged after " + str(m+1) +" Iteration")
            return x
        t[:] = x        
    return x

