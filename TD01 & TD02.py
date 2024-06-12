"""
TD01 & TD02 de Marc Rougagnou
Atelier - Data science - 2024
Groupe DS4
"""
# %% zone exo1
def Exo1():
    time = 6.892
    dist =  19.7
    vitesse = dist/time
    print("vitesse = ", vitesse)
    print("new vitesse = %.2f" %vitesse)

#%% zone exo2

def Exo2a(a, b):
    if a > b :
        mini, maxi = b,a
    else:
        mini, maxi = a,b
    print(maxi,"is the maximum")
    print(mini, "is the minimum")
    return    

def Exo2b(a, b):
    mini, maxi = b,a
    if maxi < mini:
        mini, maxi = maxi, mini
    print(maxi,"is the maximum")
    print(mini, "is the minimum")
    return

def Exo2c(a, b):
    maxi = a if a > b else b
    mini = a if a < b else b
    print(maxi, " is the maximum")
    print(mini, " is the minimum")
    return

#%% zone exo3

def volBoite(x1=None,x2 = None,x3 = None):
    if x1==None and x2 == None and x3 == None:
        return -1
        
    if x2 == None and x3 == None:
        res=x1*x1*x1
        print("%.3f"%res)
        return res
    
    if x2 != None and x3 == None and x1!=None:
        res = x1*x1*x2
        print("%.2f"%res)
        return
    
    if x1 != None and x2 != None and x3 != None:
        res = x1*x2*x3
        print("%.2f"%res)
        return
    
#%% zone exo4
def eleMax(liste, debut = None, fin = None):
    maxi=None
    if debut == None and fin == None:
        if len(liste)>0:
            maxi=liste[0]
            for i in range (len(liste)):
                if liste[i]>maxi:
                    maxi=liste[i]
        else:
            print("no list")

    if debut != None and fin == None:
        if debut>0 and debut<=len(liste):
            maxi=liste[debut]
            for i in range(debut,len(liste)):
                if liste[i]>maxi:
                    maxi=liste[i]
        else:
            print("out of range")
    
    if fin != None and debut ==None:
        if fin >0 and fin <=len(liste):
            maxi=liste[0]
            for i in range(0, fin):
                if liste[i]>maxi:
                    maxi=liste[i]
        else:
            print("out of range")
            
    if debut != None and fin != None:
        if debut>0 and debut<len(liste)+1 and fin<=len(liste)+1 and debut<fin:
            maxi=liste[debut]
            for i in range (debut, fin):
                if liste[i]>maxi:
                    maxi=liste[i]
        else:
            print("out of range")
    return maxi

#%% zone exo 5
def combT1andT2(t1, t2):
    tab=[]
    for i in range (len(t1)):
        tab.append(t2[i])
        tab.append(t1[i])
    return tab

#%% zone exo 6

def inverse(s):
    res=""
    for i in range(len(s)-1,-1,-1):
        res=res+s[i]
    return res

#%% zone exo 7
def mafonction(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
"""
la fonction réalise un tri à bulle sur la liste donnée en entrée
les nombres sont mis dans l'ordre croissant donc si on met en entré [1,5,3,4] il ressort [1,3,4,5]
"""
#%% zone exo 8

def Exo8(start):
    for i in range (start, 0, -1):
        print(i,end= " ")
    print("Go!")
    
#%% zone exo 9

def palindrome(s):
    res=""
    for i in range(len(s)-1,-1,-1):
        res=res+s[i]
    if res==s:
        return (s," is palindrome")
    else:
        return (s," is not palindrome")

#%% zone exo 10

def Exo10(liste):
    l1, l2, l3 = [], [], []
    
    for i in range(len(liste)):
        l1.append(liste[i])
    for i in range(len(liste)-1,-1,-1):
        l1.append(liste[i])
    
    for i in range(3):
        l2.append(liste[0])
    
    for i in range(len(liste)):
        if liste[i]%3==0:
            l3.append(liste[i])
            
    return "liste l1:", l1," liste l2:", l2, " liste l3:", l3

#%% zone exo 11

def Exo11(x):
    if x%2==0:
        return x," pair"
    else :
        return x, " impair"

#%% zone exo 12

def acronyme(string):
    res=""
    for elem in string.split(" "):
        res+=elem[0]
    return res.upper()

#%% zone exo 13

def count_let(chaine, c):
    count=0
    for i in range(len(chaine)):
        if (chaine[i]==c):
            count+=1
    print("You will then display ",c," apparaît ",count," fois dans ",chaine)
    return None
            
#%% zone Exo 14

def vowel_count(chaine):
    count=0
    for i in range(len(chaine)):
        if chaine[i] in 'aeiouAOIEUyY':
            count+=1 
    return count

#%% zone Exo 15

def create():
   my_dict={"pi":3.14,"mot":"mot","nombre":42,"lsite":[1,2,3]}
   return my_dict

#%% zone exo 16

def exo16(string, my_dict):
    if string in my_dict.keys():
        return string," vaut ",my_dict[string]," dans my_dict"
    else:
        return string," n'est pas une cle de ",my_dict

#%% zone exo17

def exo17(dico):
    dico["hello"]="world"
    dico["nombre"]=0 
    del(dico["pi"])
    return dico

#%% zone exo18

def exo18(values):
    s1={1,2,3}
    s2=set("hello World")
    s3,s4=set(),set()
    for i in range(len(values)):
        s3.add(values[i])
    for i in range(5,15):
        s4.add(i)
    return s1,s2,s3,s4

# %% zone du main
if __name__ == '__main__' :
#Exo0()
    
    #Exo 1
    Exo1()
    
    #Exo 2
    a=int(input("premier nombre: "))
    b=int(input("deuxieme nombre: "))
    Exo2a(a,b)
    Exo2b(a,b)
    Exo2c(a,b)
    
    #Exo 3
    volBoite(5.2)
    volBoite(5.2, 3)
    volBoite(5.2, 3, 7.4)
    
    #Exo 4
    serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
    print(eleMax(serie))
    print(eleMax(serie, 2, 5))
    print(eleMax(serie, 2))
    print(eleMax(serie, fin =3, debut =1))
    print(eleMax(serie, fin = 3))
    
    #Exo 5
    t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre',
    'Décembre']
    print(combT1andT2(t1,t2))
    
    #Exo 6
    print(inverse("zorglub"))
    
    #Exo 7
    arr=[1,5,3,4]
    mafonction(arr)
    print(arr)
    
    #Exo 8
    start=8
    Exo8(start)
    
    #Exo 9
    s="ava"
    print(palindrome(s))

    #Exo 10
    l=[0,1,2,3,4, 9, 6]
    print(Exo10(l))
    
    #Exo 11
    print(Exo11(1))
    
    #Exo 12
    string=input("Acronyme: ")
    print(acronyme(string))
    
    #Exo 13
    chaine="Hi people"
    c='w'
    count_let(chaine,c)
    
    #Exo 14
    chaine="AEOoi2nde"
    print(vowel_count(chaine))
    
    #Exo 15
    print(create())
    
    #Exo 16
    print(exo16("p",create()))
    
    #Exo 17
    print(exo17(create()))
    
    #Exo18
    values=[10,20,30,40,10,2,40]
    print(exo18(values))
    

#%% Zone début du TD02
"""
TD02
"""
#%% zone exo1

def convert(ch):
    my_list= [int(ch.split(" ")[i]) for i in range(len(ch.split(" ")))]
    return my_list
    
def convert_map(ch):
    return list(map(int, ch.split(" ")))

#%% zone exo2

def tuple_map(test,values1,values2):
    result=tuple(map((lambda x: values2[test.index(x)] if x%2==0 else values1[test.index(x)]),test))
    return result

#%% zone exo3

def pow2_map(N):
    my_list=list(map(lambda x: pow(2,x),range(N)))
    #ou my_list = [pow(2,i) for i in range(n)]
    return my_list

#%% zone exo4

def carre_map(numbers):
    my_list=[x*x for x in numbers if x<0]
    return my_list

#%% zone exo5

def filt(n,x):
    my_list=[i for i in range(n) if i%x!=0]
    return my_list

#%% zone exo6

def full_inverse(sentence):
    revert=" "
    revert = revert.join([elem[::-1] for elem in sentence.split(" ")])
    return revert

#%% zone exo7

def lower_let(sent):
    res=" "
    res=res.join([elem for elem in sent.split(" ") if all(ord(char)<=122 and ord(char)>=97 for char in elem)])
    return res

#%% zone exo8

def same_world(s1,s2):
    res=" "
    ans_s1=" "
    ans_s2=" "
    s1=s1.split(" ")
    s2=s2.split(" ")
    res=set(s1) & set(s2)
    ans_s1=ans_s1.join([elem.upper() if elem in res else elem.lower() for elem in s1])    
    ans_s2=ans_s2.join([elem.upper() if elem in res else elem.lower() for elem in s2])    
    print(ans_s1)
    print(ans_s2)
    return

#%% zone exo 9

def revert_dict(dico):
    rev_dico={val: key for key,val in dico.items()}
    return rev_dico

#%% zone exo 10

def take_coresp(dico, coresp):
    result={}
    for key, val in dico.items():
        for key_c, val_c in coresp.items():
            if val==key_c:
                result[key]=val_c
    return result

#%% zone Exo11

def sorte(liste,a=None,b=None,c=None,d=None):
    if a!=None:
        liste=sorted(liste)
        return liste
    if b!=None:
        for i in range (len(liste)):
            for j in range(len(liste)):
                if len(liste[i])<len(liste[j]):
                    liste[i], liste[j]=liste[j],liste[i] 
        return liste
    if c!=None:
        for i in range(len(liste)):
            for j in range(len(liste)):
                maxij=max(liste[j])
                maxii=max(liste[i])
                if maxii>maxij:
                    liste[i], liste[j]=liste[j],liste[i] 
        return liste
    if d!=None:
        for i in range(len(liste)):
            for j in range(len(liste)):
                if liste[i][0]<liste[j][0]:
                    liste[i], liste[j]=liste[j],liste[i] 
        print(liste)
        for i in range(len(liste)):
            for j in range(len(liste)):
                if liste[i][1]<liste[j][1]:
                    liste[i], liste[j]=liste[j],liste[i] 
        return liste
    
#%%zone exo 12

def boomerang(ite):
    for i in range(len(ite)):
        yield ite[i]
    for i in range(len(ite)-1,-1,-1):
        yield ite[i]
        
    return
#yield ca fait comme un return mais sans quitter la fonction

#%% zone Partie 2
"""
Partie 2:
"""
#%% Réponses questions

""" 
constructeur -->__init__
variables d'instances --> self.nomClient self.solde self.iban
variables de classes --> cb_count
permis utilisations de print(c2) --> c'est grace à la fonction str
permis test == --> c'est grace a la fo,nction str

"""
#%% class Point3D

class Point3D:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def __str__(self):
        return (f"x: {self.x} y: {self.y} z: {self.z}")
    
    def mod(self):
        return math.sqrt(self.x*self.x+self.y*self.y+self.z*self.z)
        
    def __add__(self,pts2):
        pts=Point3D(self.x+pts2.x,self.y+pts2.y, self.z+pts2.z)
        return pts
    
    def __sub__(self,pts2):
        pts=Point3D(self.x-pts2.x,self.y-pts2.y, self.z-pts2.z)
        return pts
    
    def __eq__(self,pts2):
        if self.x==pts2.x and self.y==pts2.y and self.z==pts2.z:
            return True
        return False
    
class Mass3D(Point3D):
    def __init__(self, x, y, z, m):
        super().__init__(x,y,z)
        self.m=m
    
    def __str__(self):
        #return super().__str__()
        return (f"x: {self.x} y:{self.y} z: {self.z} masse: {self.m}")
    
    def __add__(self, m2):
        self.x+=m2.x
        self.y+=m2.y 
        self.z+=m2.z
        self.m+=m2.m
        return self
    
    def __sub__(self, m2):
        self.x-=m2.x
        self.y-=m2.y 
        self.z-=m2.z
        self.m-=m2.m
        return self
    
    def __eq__(self,m2):
        if int(self.x)==int(m2.x) :
            return True
        return False
    
#%% main TD02
if __name__ == '__main__' :
    import math
    ch="12 13 10 8 20"
    test = [1, 2, 3, 4, 6]
    values1 = ['a', 'b', 'c', 'd', 'e']
    values2 = ['A', 'B', 'C', 'D', 'E']
    numbers=[-1,-2,-3,4,5,10,-5,3]
   
    #Exo 1
    print(convert(ch))
    print(convert_map(ch))
    
    #Exo 2
    print(tuple_map(test,values1,values2))
    
    #Exo 3
    print(pow2_map(4))
    
    #Exo 4
    print(carre_map(numbers))
    
    #Exo 5
    print(filt(10,2))
    
    #Exo 6
    sentence=input("La phrase: ")
    print(full_inverse(sentence))
    
    #Exo 7
    sentence=input("La phrase: ")
    print(lower_let(sentence))
    
    #Exo 8
    s1="Hello kitty"
    s2="Hello world"
    same_world(s1, s2)
    
    #Exo 9
    dico={'b':1, 'a':2, 'd':5}
    print(revert_dict(dico))
    
    #Exo 10
    my_dict = {"a":"b", "b":"c", "c":"a"}
    correspondances = {"a":"A", "b":"B", "c":"C"}
    print(take_coresp(my_dict, correspondances))
    
    #Exo 11
    liste=[5,3,10,4,8,20,2]
    l=["bonjour","tout","le","monde"]
    lis=[ [1,0,5],[1,2,3], [8,5] ]
    li=l=[('Luc',22),('Lea',18),('Alice',23),('Luca',21), ('Max',20) ]
    print(sorte(liste,a=1))
    print(sorte(l,b=1))
    print(sorte(lis,c=1))
    print(sorte(li,d=1))
    
    #Exo 12
    l = [1,2,3]
    for x in boomerang(l):
        print(x)
    
    #Class point3D
    pts=Point3D(1, 2, 3)
    pts1=Point3D(1,0,3)
    print(pts)
    print(pts.mod())
    print(pts+pts)
    print(pts-pts)
    print(pts==pts)
    print(pts==pts1)
    
    #Class Mass3D
    m=Mass3D(1,2,3,5)
    m1=Mass3D(1,2,3,5)
    m2=Mass3D(2,3,4,7)
    print(m==m)
    print(m==m1)
    print(m==m2)
    
    
    
    
    
    
    
    
    
    