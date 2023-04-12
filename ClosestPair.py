#I have given a line by line explanation and understanding of my code in my pdf of the assignment 

import copy

#A class to represent a Point in 2D plane

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
#dist function to find the distance between two points

def dist(p1, p2):
    return ((p1.x - p2.x) * (p1.x - p2.x) +(p1.y - p2.y) * (p1.y - p2.y))**0.5
 
#assert: A Brute Force method to return the smallest distance between two points in P[] of size n

def bf(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if dist(P[i], P[j]) < min_val:
                min_val = dist(P[i], P[j])
 
    return min_val
 
# assert: A function to find the distance between the closest points of strip of given size. All points in strip[] are sorted according to y coordinate. 

def stripClosest(strip, size, d):
     
    #assert: Initialize the minimum distance as d
    min_val = d
 
    
    #INV: Pick all points one by one and try the next points till the difference between y coordinates is smaller than d.

    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y - strip[i].y) < min_val:
            min_val = dist(strip[i], strip[j])
            j += 1
 
    return min_val
 
#INV: A recursive function to find the smallest distance. The array P contains all points sorted according to x coordinate

def closestUtil(P, Q, n):

    #assert: If there are <= 3 points, then use brute force

    if n <= 3:
        return bf(P, n)
 
    #Find the middle point

    mid = n // 2
    midPoint = P[mid]
 
    #keep a copy of left and right subarrays/ sections that we've made

    Pl = P[:mid]
    Pr = P[mid:]
 
    #Consider the vertical line passing through the middle point calculate smallest distance dl and dr
  
    dl = closestUtil(Pl, Q, mid)
    dr = closestUtil(Pr, Q, n - mid)  

    #Find the smaller of two distances

    d = min(dl, dr)
 
    #assert: Build an array strip[] that contains points close (closer than d) to the line passing through the middle point
    #INV: 

    stripP = []
    stripQ = []
    lr = Pl + Pr

    #To put it in the most simple words, so far in this code atleast the function of abs is just to return a positive value
    #Same case as min(), we could just have an if else statement
    #if lr[i].x - midPoint.x <0:    create_a_new_variable_to_check_condition_with= (lr[i].x - midPoint.x)* (-1)
    #else:  we'd move to the next line. 
    for i in range(n):
        if abs(lr[i].x - midPoint.x) < d:
            stripP.append(lr[i])
        if abs(Q[i].x - midPoint.x) < d:
            stripQ.append(Q[i])
 
#In python lambda is a keyword used to define anonymous functions. It can be specified directly, Inline in (for example here) the sorted function
#We are "pre-sorting", now we have used an inbuilt function but what we can use is a merge sort algorithm and define a .sort() function. 
#I have specified all defined function which are in this code inbuilt functions and given explanations in my written pdf. 

    stripP.sort(key = lambda point: point.y) 
    min_a = min(d, stripClosest(stripP, len(stripP), d))
    min_b = min(d, stripClosest(stripQ, len(stripQ), d))
     
     
    # Return the minimum of d and self.closest distance is strip[]
    #We are using an inbuilt function here but we could actually not do that and not even define a new min
    #This is because we are just comparing two varibles
    #So we could have if min_a<min_b:   return min_a else:  return min_b (an if else statement)
    #we could do this for all comparisons where we use min.

    return min(min_a,min_b)
 
# The main function that finds the smallest distance.
# performs the initial sorting and makes the initial invocation (the execution of a program or function) of the recursive function.

#Deepcopy: It constructs a new compound object. As in objects that contain other objects. 
#It then recursively inserts these copies into the variable that we .deepcopy to. 
#It basically inserts into it what was found in the original

def closest(P, n):
    P.sort(key = lambda point: point.x)
    Q = copy.deepcopy(P)
    Q.sort(key = lambda point: point.y)   
 
    # Use recursive function closestUtil() to find the smallest distance

    return closestUtil(P, Q, n)
 
# Driver code

P = [Point(4, 23), Point(21, 32), Point(4, 5), Point(7, 9), Point(42, 10), Point(37, 2)]
n = len(P)
print(closest(P, n))