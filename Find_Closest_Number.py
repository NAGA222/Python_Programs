#https://practice.geeksforgeeks.org/problems/closest-number5728/1

class Solution:
    def ClosestNumber(self, N , M):
        return round(N/float(M))*M

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N,M=map(int,input().strip().split(" "))
        s=Solution()
        print(s.ClosestNumber(N,M))