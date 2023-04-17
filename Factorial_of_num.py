#https://practice.geeksforgeeks.org/problems/factorial5739/1

import math
class Solution:
    def factorial(self,N):
        res=1
        for i in range(2,N+1):
            res=res*i

        return res
        #return math.factorial(N)

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        s=Solution()
        print(s.factorial(N))
