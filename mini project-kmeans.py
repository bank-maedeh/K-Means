from math import sqrt
from random import randint
import pprint

def error_ent(n):
    if n>2:
        raise ValueError

POINT=tuple[float,float,float]
def distance_calculation(p1:POINT, p2:POINT, t:int)->float:
    if t==1:
        distance=(abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2]))
    elif t==2:
        distance=sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)
    return distance

def k_means (points:list,centers:list,t:int)->list:
    clustering= [ {f"center {i+1}": center , "points":[]} for i,center in enumerate(centers)]
    for point in points:
        min_dis=distance_calculation(point,centers[0],t)
        for center in centers:
            if distance_calculation(point,center,t)<=min_dis:
                min_dis=distance_calculation(point,center,t)
                pos=centers.index(center)
        clustering[pos]["points"].append(point)
    #pprint.pprint(clustering)
    return clustering

def new_center(clustering):
    newcenter=[]
    newcenter2=[]
    for i in range(0,k):
        xp,yp,zp=0,0,0
        #x,y,z=0,0,0
        #(x,y,z)=zip(*clustering[i]["points"])
        #if len(x)!=0:
        #    newcenter.append((sum(x)/len(x),sum(y)/len(y),sum(z)/len(z)))
        #else:
        #    newcenter.append((0,0,0))  

        for point in clustering[i]["points"]:
            xp=xp+point[0]
            yp=yp+point[1]
            zp=zp+point[2]
        if len(clustering[i]["points"])!=0:
            newcenter2.append((xp/len(clustering[i]["points"]),
                             yp/len(clustering[i]["points"]),
                             zp/len(clustering[i]["points"])))
        else:
            newcenter2.append((0,0,0)) 
    #print("1:",newcenter)
    #print("2:",newcenter2)
    
    return newcenter2



#in the first step the points are generated
"""
points=[(-4, -2, 4), (-4, 4, -7), (-5, 8, 6), (0, 0, 5), (-3, 10, 3), (0, -1, -10),
         (8, 5, 8), (-5, -4, -2), (3, -5, 10), (-8, 5, -7),(0, 10, 5), (0, 10, 13), (1, -10, -10)]
"""
with open ("C:\\Users\\Maedeh\\Desktop\\tamrin py\\py.txt") as f:
    l=f.readlines()

lp=[i.replace("(","") for i in l]
l=[i.replace(")","") for i in lp]
i=0
points=[]
invaliddata=0
while i<len(l):
   try:
      points.append(tuple(map(float,l[i].strip().split(","))))
      i=i+1
   except:
      invaliddata=invaliddata+1
      i+=1
       
    
k=int(input("Please enter a k as the number of the clusters: "))
method= int(input("Please enter the distance method \n1)manhatan \n2)euclidus\nEnrer number: "))
while True:
    try:
        error_ent(method)
        break
    except:
        method= int(input("Please enter the distance method \n1)manhatan \n2)euclidus\nEnrer number: "))
print("points= ",points,"\n")
print(f"{invaliddata} number of the points were invalid, so they can not be used in clustering \n")
centers=[(randint(-10,10),randint(-10,10),randint(-10,10)) for _ in range (k)]
print ("centers=" ,centers,"\n")
clustering=k_means(points,centers,method)
#pprint.pprint(clustering)
newcenter=new_center(clustering)
while centers!=newcenter:
    centers=newcenter.copy()
    clustering=k_means(points,newcenter,method)
    newcenter=new_center(clustering)   
pprint.pprint (clustering)


"""
from math import sqrt
from random import randint
import pprint
POINT=tuple[float,float,float]

def error_ent(n:int):
    """
    this function raise a error if the number of the method is invalid"
    """
    if n>2:
        raise ValueError


def distance_calculation(p1:POINT, p2:POINT, t:int)->float:
    """
    this function clculates the distance between two points with the wanted method(manhatan or Euclidean)
    """
    if t==1:
        distance=(abs(p1[0]-p2[0])+abs(p1[1]-p2[1])+abs(p1[2]-p2[2]))
    elif t==2:
        distance=sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)
    return distance

def k_means (points:list,centers:list,t:int)->list:
    """
    this function cluster points around the centers 
    """
    clustering= [ {f"center {i+1}": center , "points":[]} for i,center in enumerate(centers)]
    for point in points:
        min_dis=distance_calculation(point,centers[0],t)
        for center in centers:
            if distance_calculation(point,center,t)<=min_dis:
                min_dis=distance_calculation(point,center,t)
                pos=centers.index(center)
        clustering[pos]["points"].append(point)
    #pprint.pprint(clustering)
    return clustering

def new_center(clustering):
    """
    this function calcules  new center of the points in a cluster according to average of Geometric coordinates
    """
    newcenter=[]
    newcenter2=[]
    for i in range(0,k):
        xp,yp,zp=0,0,0
        #x,y,z=0,0,0
        #(x,y,z)=zip(*clustering[i]["points"])
        #if len(x)!=0:
        #    newcenter.append((sum(x)/len(x),sum(y)/len(y),sum(z)/len(z)))
        #else:
        #    newcenter.append((0,0,0))  
        for point in clustering[i]["points"]:
            xp=xp+point[0]
            yp=yp+point[1]
            zp=zp+point[2]
        if len(clustering[i]["points"])!=0:
            newcenter2.append((xp/len(clustering[i]["points"]),
                             yp/len(clustering[i]["points"]),
                             zp/len(clustering[i]["points"])))
        else:
            newcenter2.append((0,0,0))   
    return newcenter2

def read_points(file_path):

    with open (file_path) as f:
        l=f.readlines()
    #lp=[i.replace("(","") for i in l]
    #l=[i.replace(")","") for i in lp]
    i=0
    points=[]
    invaliddata=0
    while i<len(l):
         try:
            points.append(tuple(map(float,l[i].strip().split(","))))
            i=i+1
         except:
             invaliddata=invaliddata+1
             i+=1    
    return points,invaliddata
       
    
k=int(input("Please enter a k as the number of the clusters: "))
method= int(input("Please enter the distance method \n1)Manhatan \n2)Euclidean\nEnrer number: "))
while True:
    try:
        error_ent(method)
        break
    except:
        method= int(input("Please enter the distance method \n1)manhatan \n2)euclidus\nEnrer number: "))
points,_=read_points("C:\\Users\\Maedeh\\Desktop\\tamrin py\\points.txt")
print("points= ",points,"\n")
_,invaliddata=read_points("C:\\Users\\Maedeh\\Desktop\\tamrin py\\points.txt")
print(f"{invaliddata} number of the points were invalid, so they can not be used in clustering \n")
centers=[(randint(-10,10),randint(-10,10),randint(-10,10)) for _ in range (k)]
print ("centers=" ,centers,"\n")
clustering=k_means(points,centers,method)
#pprint.pprint(clustering)
newcenter=new_center(clustering)
#counter=1
while centers!=newcenter:
    centers=newcenter.copy()
    clustering=k_means(points,newcenter,method)
    newcenter=new_center(clustering)
    #counter=counter+1
#print(counter)  
print("this is the recomanded cluster: ") 
pprint.pprint (clustering)
"""