#https://practice.geeksforgeeks.org/problems/series-ap5310\1

class Solution:
    def nthTermOfAP(self,A1,A2,N):
        return (A1+((N-1)*(A2-A1)))

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        A1,A2,N=map(int,input().strip().split(' '))
        s=Solution()
        print(s.nthTermOfAP(A1,A2,N))
        