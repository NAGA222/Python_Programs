# https://practice.geeksforgeeks.org/problems/prime-number2314/1

class Solution:
    def prime(self, N):
        c=0
        j=int(N**(1/2))
        for i in range(2,j+1):
            if(N%i==0):
                c+=1
        if(c==0 and N!=1):
            return 1
        else:
            return 0

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        s=Solution()
        print(s.prime(N))
