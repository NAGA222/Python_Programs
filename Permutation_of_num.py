#https://practice.geeksforgeeks.org/problems/npr4253/1

import math
class Solution:
    def nPr(self, n, r):
        # code here
        nf=math.factorial(n)
        nrf=math.factorial(n-r)
        
        return nf//nrf

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n,r=map(int,input().strip().split())
        s=Solution()
        print(s.nPr(n,r))