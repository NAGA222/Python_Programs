#https://practice.geeksforgeeks.org/problems/print-the-kth-digit3520/1

import math
class Solution:
    def kthDigit(self, A, B, K):
        res=pow(A,B)
        c=0
        while res>0:
            c=c+1
            r=res%10
            if c==K:
                return r
            res=res//10
        return

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        A,B,K=map(int,input().strip().split())
        s=Solution()
        print(s.kthDigit(A,B,K))
    