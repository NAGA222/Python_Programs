#https://practice.geeksforgeeks.org/problems/gcd-of-two-numbers3459/1

import math
class Solution:

    def gcd(self,A,B):

        #return math.gcd(A,B)

        if(B==0):
            return A
        else:
            return self.gcd(B,A%B)

if __name__ == '__main__':

    T=int(input())
    for i in range(T):
        A,B=map(int,input().strip().split())
        s=Solution()
        print(s.gcd(A,B))
