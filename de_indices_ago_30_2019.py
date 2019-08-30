# -*- coding: utf-8 -*-
"""Untitled19.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GJX5dkJyfGSsaoN6uwBLFKrMJpEgnwN_
"""

import numpy as np

def de(MAX,MIN, mut, crossp, popsize, its,fobj,X,SOMA,TOTAL,QUANT):
    
  
  Num=len(MAX)
  
  XOLD=X
  X=np.zeros((popsize,Num)) 
  INDICE=np.zeros(QUANT) 
    
  for i in range(popsize):
    for j in range(Num):
        X[i,j]=np.copy(XOLD[i,j])
  
  
  
  bounds=[(0,0)] * Num
  dimensions = len(bounds)  
  
  for i in range(Num):
    bounds[i]=(MIN[i], MAX[i])

  fitness = np.asarray([fobj(ind) for ind in X])
  best_idx = np.argmin(fitness)
  best = X[best_idx]
  

  
  for i in range(its):
    if(SOMA>TOTAL):
      soma_ind=0
      break
    else:
      soma_ind=SOMA
    for j in range(popsize):
      if(SOMA>TOTAL):
        soma_ind=0
        break
      else:
        soma_ind=SOMA
      SOMA=SOMA+1
      
      idxs = [idx for idx in range(popsize) if idx != j]
      a, b, c = X[np.random.choice(idxs, 3, replace = False)]
      mutant = a + mut * (b - c)

      for k in range(Num):
        if(mutant[k]>MAX[k]):
          mutant[k]=MAX[k]
        if(mutant[k]<MIN[k]):
          mutant[k]=MIN[k]
          
      cross_points = np.random.rand(dimensions) < crossp
      if not np.any(cross_points):
        cross_points[np.random.randint(0, dimensions)] = True

      trial = np.where(cross_points, mutant, X[j,:])


      f = fobj(trial)
      if f < fitness[j]:
        fitness[j] = f
        X[j,:] = trial
        if f < fitness[best_idx]:
          best_idx = j
          best = trial

    fitness = np.asarray([fobj(ind) for ind in X])

  fitness = np.asarray([fobj(ind) for ind in X])
  best_idx = np.argmin(fitness)
  best = X[best_idx]
  fobj_best = fitness[best_idx]

  
  y=fitness

  BEST=best
  FOBEST=fobj_best
  XY= np.c_[X,y] #concatena x e y em 2 colunas            
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir da last col(Y) for all row
  x=XYsorted[:,0:Num]
  XY=XYsorted
  BEST_XY =np.append(BEST,FOBEST)
  
  for i in range(popsize):
    for j in range(Num):
        XOLD[i,j]=np.copy(X[i,j])
  
  soma=0
  for j in range(Num):
    for i in range(popsize):
        Xj=np.mean(X[:,j])
        soma=soma+(X[i,j]-Xj)**2
  DI=(soma/popsize)**0.5
  
  # DI Indice:  Radka Polakova, Josef Tvrdik, Petr Bujok 
  # Differential evolution with adaptative mechanism of population size according to current diversity
  
        
        
  INDICE[0]=DI
  INDICE[1]=soma_ind # este indice vai ser modificado externamente
  INDICE[2]=30    

        
  return XOLD,BEST,FOBEST,XY,BEST_XY,SOMA,INDICE
