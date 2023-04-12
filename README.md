# Closest-Pair

In this problem, a set of n points are given on the 2D plane. In this problem, we have to find the pair of points, whose distance is minimum.


## Our solution to this problem 

Given a set of points in a plane, p = {(x0, y0),(x1, y1), . . . ,(xn−1, yn−1)}, consider the problem of determining the closest pair of points

Clearly the naive idea of computing the n(n−1)/2 distances and finding the minimum gives an O(n^2) algorithm. Here is an improvement using divide and conquer.

As a pre-processing step, the input array is sorted according to x coordinates.
1. Find a value x such that half the points have xi<= x and half have xi> x (roughly; you may partition about the median
on their x coordinates to do this). On this basis split into two groups L and R.
2. Recursively compute the closest pair in L and in R. Let these pairs be pL, q L ∈ L and pR, qR∈ R, with distances dL and
dR respectively. Let the smaller of these two distances be d.
3. It remains to be seen if there is a point in L and a point in R that are less than d distance apart from each other.
4. Now, go through this sorted list, and for each point, compare its distance to the seven subsequent points in the list
(why?). Let pM, qM be the closest pair found this way.
5. The answer is one of the three pairs {pL, qL}, {pR, qR} and {pM, qM}, whichever is closest.
