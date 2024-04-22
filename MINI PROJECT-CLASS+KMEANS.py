from math import sqrt
from random import randint
import pprint
import copy
class Point:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        
    def __eq__(self,other):
        if isinstance(other,Point):
            t=(self.x==other.x) & (self.y==other.y) & (self.z==other.z)
            return t
        return False

    def __repr__ (self):
        return f"( {self.x}, {self.y}, {self.z})"

        
def error_ent(n:int):
    """
    this function raise a error if the number of the method is invalid"
    """
    if n>2:
        raise ValueError

def distance_calculation(p1, p2, t:int)->float:
    """
    this function clculates the distance between two points with the wanted method(manhatan or Euclidean)
    """
    if t==1:
        distance=(abs(p1.x-p2.x)+abs(p1.y-p2.y)+abs(p1.z-p2.z))
    elif t==2:
        distance=sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2+(p1.z-p2.z)**2)
    return distance

def k_means (points:list,centers:list,t:int)->list:
    """
    this function cluster points around the centers 
    """
    clustering= [ {f"center{i+1}": center , "points":[]} for i,center in enumerate(centers)]
    for pointt in points:
        min_dis=distance_calculation(pointt,centers[0],t)
        for center in centers:
            if distance_calculation(pointt,center,t)<=min_dis:
                min_dis=distance_calculation(pointt,center,t)
                pos=centers.index(center)
        clustering[pos]["points"].append(pointt)
    #pprint.pprint(clustering)
    return clustering

def new_center(clustering):
    """
    this function calcules  new center of the points in a cluster according to average of Geometric coordinates
    """
    #newcenter=[]
    newcenter2=[]
    for i in range(0,k):
        xp,yp,zp=0,0,0
        """
        xt,yt,zt=0,0,0
        xt=sum(pointt.x for pointt in len(clustering[i]["points"]))
        yt=sum(pointt.y for pointt in len(clustering[i]["points"])) 
        zt=sum(pointt.z for pointt in len(clustering[i]["points"])) 
        print(xt , yt, zt)
        """
        for pointt in clustering[i]["points"]:
            xp=xp+pointt.x
            yp=yp+pointt.y
            zp=zp+pointt.z
        if len(clustering[i]["points"])!=0:
            newcenter2.append(Point(xp/len(clustering[i]["points"]),
                             yp/len(clustering[i]["points"]),
                             zp/len(clustering[i]["points"])))
        else:
            newcenter2.append(Point(0,0,0))   
    return newcenter2

def read_points(file_path):

    with open (file_path) as f:
        l=f.readlines()
    lp=[i.replace("(","") for i in l]
    l=[i.replace(")","") for i in lp]
    i=0
    points=[]
    invaliddata=0
    while i<len(l):
         try:
            points.append(Point(*map(float,l[i].strip().split(","))))
            i=i+1
         except:
             invaliddata=invaliddata+1
             i=i+1    
    return points,invaliddata
       
    
k=int(input("Please enter a k as the number of the clusters: "))
method= int(input("Please enter the distance method \n1)Manhatan \n2)Euclidean\nEnrer number: "))
while True:
    try:
        error_ent(method)
        break
    except:
        method= int(input("Please enter the distance method \n1)manhatan \n2)euclidus\nEnrer number: "))
points,invaliddata=read_points("C:\\Users\\Maedeh\\Desktop\\tamrin py\\points.txt")
print(f"\n{invaliddata} number of the points were invalid, so they could not be used in clustering \n")
print("points:", points)
centers=[Point(randint(-10,10),randint(-10,10),randint(-10,10)) for _ in range (k)]
print("\nRandom centers:",centers,"\n")
clustering=k_means(points,centers,method)
#pprint.pprint(clustering)
newcenter=new_center(clustering)
#counter=1
#print("\nnewcenters:", newcenter)
if newcenter==centers:
    print("yes")

while centers!=newcenter:
   centers=copy.deepcopy(newcenter)
   clustering=k_means(points,newcenter,method)
   newcenter=new_center(clustering)
    #counter=counter+1
#print(counter)  

print("This is the recomanded cluster: \n") 
pprint.pprint (clustering)

