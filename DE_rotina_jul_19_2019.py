# -*- coding: utf-8 -*-
"""DE_variavel_jul_18_2019_rotina.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ogHn_bYqlnCokGuQ6wO3q6o6LoaWZbBq
"""

import numpy as np

'''https://pablormier.github.io/2017/09/05/a-tutorial-on-differential-evolution-with-python/'''

"""def Fun( sol):
  #Schwefel(x):
  x=sol  
  summ=0
  for i in range(len(x)):
    new=x[i]*np.sin((abs(x[i]))**0.5)
    summ=summ+new
    top=(418.9829*len(x)-summ) 
  
  return top;"""

def de(MAX,MIN, mut, crossp, popsize, its,fobj,X):
  
  
  Num=len(MAX)
  bounds=[(0,0)] * Num
  dimensions = len(bounds)  
  
  for i in range(Num):
    bounds[i]=(MIN[i], MAX[i])
  
  #diff = np.fabs(MIN - MAX)
  min_b, max_b = np.asarray(bounds).T
  diff = np.fabs(min_b - max_b)
  
  pop=np.zeros((popsize,Num))

    
  for i in range(popsize):
    for j in range(Num):
      pop[i,j]=(X[i,j]-MIN[j])/(MAX[j]-MIN[j])

  #print(pop[0,:]) 
  pop_denorm = X
  fitness = np.asarray([fobj(ind) for ind in pop_denorm])
  best_idx = np.argmin(fitness)
  best = pop_denorm[best_idx]
  for i in range(its):
    for j in range(popsize):
      
      idxs = [idx for idx in range(popsize) if idx != j]
      a, b, c = pop[np.random.choice(idxs, 3, replace = False)]
      mutant = np.clip(a + mut * (b - c), 0, 1)
      cross_points = np.random.rand(dimensions) < crossp
      if not np.any(cross_points):
        cross_points[np.random.randint(0, dimensions)] = True
      trial = np.where(cross_points, mutant, pop[j])
      trial_denorm = min_b + trial * diff
      #print("=====",trial,"******",trial_denorm )
      f = fobj(trial_denorm)
      if f < fitness[j]:
        fitness[j] = f
        pop[j] = trial
        if f < fitness[best_idx]:
          best_idx = j
          best = trial
          
    pop_denorm = min_b + pop * diff
    fitness = np.asarray([fobj(ind) for ind in pop_denorm])

  fitness = np.asarray([fobj(ind) for ind in pop_denorm])
  best_idx = np.argmin(fitness)
  best = pop_denorm[best_idx]
  fobj_best = fitness[best_idx]

  
  y=fitness
  #xo=pop
  xo = min_b + pop * diff
  #xo=pop_denorm estou em duvidas aqui....
  BEST=best
  FOBEST=fobj_best
  XY= np.c_[xo,y] #concatena x e y em 2 colunas            
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir da last col(Y) for all row
  x=XYsorted[:,0:Num]
  XY=XYsorted
  BEST_XY =np.append(BEST,FOBEST)
  #print(pop_denorm)
  
  return x,BEST,FOBEST,XY,BEST_XY

'''

GlobalParam e Solucao: [4.20971300e+02 4.20968070e+02 4.20967728e+02 3.91941765e-05]
Means of 1 runs: 3.91941764519288e-05
'''

"""MAX=[500,500,500] # MAXIMO DE CADA PARAMETRO
MIN=[-500,-500,-500] # MINIMO DE CADA PARAMETRO
PAR=3
mut=0.8
crossp=0.7
NPAR=100
ITE=100

runtime=1
its=1
runs=ITE

dimensions=len(MAX)

pop = np.random.rand(NPAR, dimensions)
diff=np.zeros(PAR)
for i in range(PAR):
  diff[i] = MAX[i]-MIN[i]
X = MIN + pop * diff
#print(X)

for run in range(runs):
  X,BEST,FOBEST,XY,BEST_XY= de(MAX,MIN, mut, crossp, NPAR, its,Fun,X)
  print("Iteracao[",run+1,"] : GlobalParam e Solucao:", BEST_XY)

print("GlobalParam e Solucao final:", BEST_XY)

mean=np.average(FOBEST)


print("Means of",runtime,"runs:",mean,"\n")"""
