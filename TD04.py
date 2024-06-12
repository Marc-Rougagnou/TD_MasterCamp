"""
TD04
Marc Rougagnou
Groupe DS4
"""
import random
echec_dim=8

class individu:
    def __init__(self,val=None):
        if val==None:
            self.val=random.sample(range(echec_dim),echec_dim)
        else:
            self.val=val
        self.nbconflict=self.fitness()
        
    def __str__(self):
        res=""
        for i in range(len(self.val)):
            res+=str(self.val[i])+" "
        return res

    def conflict(p1,p2):
        """ retourne True si reine P1 est conflict avec reine P2"""
        if p1[0]==p2[0] or p1[1]==p2[1] or abs(p1[0]-p2[0])==abs(p1[1]-p2[1]):
            return True
        return False
    
    def fitness(self):
        """ savoir le nombre de conflits """
        self.nbconflict=0 
        for i in range(echec_dim):
            for j in range(i+1,echec_dim):
                
                p1=[i,self.val[i]]
                p2=[j,self.val[j]]
                if(individu.conflict(p1,p2)):
                    self.nbconflict+=1
        return self.nbconflict
                
def create_rand_pop(count):
    """ création d'une population de count individus"""
    pop=[]
    for i in range(count):
        pop.append(individu())
    return pop

def ppop(pop):
    """ fct de print de la population """
    for i in range(len(pop)):
        print(pop[i],"conflits: ",pop[i].nbconflict)
    return 

def evaluate(pop):
    return sorted(pop,key= lambda x: x.nbconflict)

def selection(pop,hcount,lcount):
    sous_pop=[]
    for i in range(hcount):
        sous_pop.append(pop[i])
    for i in range(lcount):
        sous_pop.append(pop[len(pop)-1-i])
    return sous_pop

def croisement(ind1,ind2):
    l1=individu()
    l2=individu()
    l1.val=ind1.val[0:len(ind1.val)//2]+ind2.val[len(ind2.val)//2:len(ind2.val)]
    l2.val=ind2.val[0:len(ind2.val)//2]+ind1.val[len(ind1.val)//2:len(ind1.val)]
    return [l1,l2]

def mutation(ind):
    index=random.randint(0,echec_dim-1)
    nb=random.randint(0,echec_dim-1)
    ind.val[index]=nb
    return ind

def algoloopSimple():
    pop=create_rand_pop(25)
    solutiontrouvee=False
    nbriteration=0
    while not solutiontrouvee: 
        print("iteration numéro : ", nbriteration)
        nbriteration+=1
        evaluation=evaluate(pop) 
        if evaluation[0].fitness() == 0: 
            solutiontrouvee=True
        else:
            select=selection(evaluation, 10,4) 
            croises=[]
            for i in range (0, len(select),2 ): 
                croises+=croisement(select [i], select [i+1] )
            mutes=[]
            for i in select: 
                mutes.append(mutation(i))
            newalea=create_rand_pop(5) 
            pop=select [:]+croises[:]+mutes [:]+newalea[:]
    print(evaluation [0])

algoloopSimple()

#%% Partie 2 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

data=np.random.randn(500,3)

fig = plt.figure(figsize=(10,10))
# choose projection 3d for creating a 3d graph
axis = fig.add_subplot(111, projection='3d')
axis.scatter(data[:,0],data[:,1],data[:,2],cmap='plasma')

#question 3
mean_col_0=np.mean(data[:,0],axis=0)#data[:0]--> 1er colonne , 0 --> colonne (si 1--> ligne)
mean_col=np.mean(data,axis=0)
print(mean_col_0," col",mean_col)

#Question 3 (2)
ecart_0=np.std(data[:,0],axis=0)
ecart=np.std(data,axis=0)
print(ecart_0, " ecart ",ecart)

#question 4
print("Avant changement\n",data)
data_copy=data.copy()
def normalisation(data):
    mean_col = np.mean(data, axis = 0)
    std_col = np.std(data, axis = 0)
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = (data[i][j] - mean_col[j]) / std_col[j] 
    return data

datanorm=normalisation(data)
print("Après normalisation\n",datanorm)

#Question 6
def transp(data):
    data=np.transpose(data)
    return data

datatrans=transp(datanorm)
print("transposé \n", data)

#question 7 
data_cov=datatrans.dot(datanorm)/500
print("covariance\n",data_cov)
covariance=np.cov(datatrans)
print("np.cov \n", covariance)

#question 8
val_prop, vec_prop = np.linalg.eig(covariance)
print("val propre\n",val_prop)
print("vec propre\n", vec_prop)

#question 9
indice_trie=np.argsort(val_prop)[::-1]
val_prop=val_prop[indice_trie]
vec_prop=vec_prop[:,indice_trie]
print("val trié\n",val_prop)
print("vec trié\n",vec_prop)

#question 10
pca=vec_prop[:,0:2]
print("pca \n", pca)

#question 11
projecteddata=datanorm.dot(pca)
#print("projectdata\n",projecteddata)

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(figsize=(10,10))
plt.scatter(projecteddata[:,0],projecteddata[:,1],cmap='plasma')


















