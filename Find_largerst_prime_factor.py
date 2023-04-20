#https://practice.geeksforgeeks.org/problems/largest-prime-factor2601/1

class Solution:
    def prime(self,k):
            c=0
            for i in range(2,k+1):
                if(k%i==0):
                    c+=1
                if(c>1):
                    break
            if(c==1):
                return 1
            else:
                return 0

    def largestPrimeFactor (self, N):
        res=[]
        for i in range(1,N+1):
            if(N%i==0):
                if(self.prime(i)):
                    res.append(i)
        return max(res)
                

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        s=Solution()
        print(s.largestPrimeFactor(N))


                