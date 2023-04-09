#https://practice.geeksforgeeks.org/problems/print-table0303/1

class Solution:
    def getTable(self,N):
        res=[]
        for i in range(1,11,1):
            res.append(N*i)
        return res

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        s=Solution()
        res=s.getTable(N)
        for i in res:
            print(i, end=" ")
        print()
