#https://practice.geeksforgeeks.org/problems/series-gp4646/1

import math
class Solution:
	def Nth_term(self, a, r, n):
		mod= 1000000007
		return math.floor(a*(pow(r,(n-1),mod))) % mod

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        a,r,n=input().split()
        a,r,n=int(a),int(r),int(n)
        s=Solution()
        res=s.Nth_term(a,r,n)
        print(res)