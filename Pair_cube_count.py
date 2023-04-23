#https://practice.geeksforgeeks.org/problems/pair-cube-count4132/1

import math
class Solution:
    def pairCubeCount(self, N):
        c=0 
        a=N**(1/3)
        if(a>int(a)):
            print(int(a))
            for i in range(1,int(a)+1):
                for j in range(1,int(a)+1):
                    if(math.pow(i,3)+math.pow(j,3)==N):
                        print(i,j)
                        c+=1
        elif(a==int(a)):
            c+=1
        return c



if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        s=Solution()
        print(s.pairCubeCount(N))
    