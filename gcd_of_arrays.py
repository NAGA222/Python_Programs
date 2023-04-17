#https://practice.geeksforgeeks.org/problems/gcd-of-array0614/1
import math
class Solution:

    def gcd(self,n,arr):
        a=arr[0]
        for i in range(1,n,1):
            r=math.gcd(a,arr[i])
            a=r
        return a

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        s=Solution()
        print(s.gcd(n,arr))