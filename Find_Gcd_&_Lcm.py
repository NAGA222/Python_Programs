#https://practice.geeksforgeeks.org/problems/lcm-and-gcd4516/1

import math
class Solution:
    def lcmAndGcd(self, A , B):
        # code here
        l=[]
        gcd1= math.gcd(A,B)
        lcm1=(A*B)//(math.gcd(A,B))
        l.append(lcm1)
        l.append(gcd1)
        
        return l

if __name__ == '__main__':
    T= int(input())
    for i in range(T):
        A,B=map(int,input().strip().split())
        s=Solution()
        l=s.lcmAndGcd(A,B)
        print(l[0],l[1])