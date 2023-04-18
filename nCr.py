#https://practice.geeksforgeeks.org/problems/ncr1019/1

import math
class Solution:
    def nCr(self, n, r):
        if(r<=n):
            num1=math.factorial(n)
            den1=math.factorial(n-r)*math.factorial(r)
        
            return (num1//den1)%1000000007
            
        else:
            return 0

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n,r=map(int,input().strip().split())
        s=Solution()
        print(s.nCr(n,r))