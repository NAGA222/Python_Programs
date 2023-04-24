

class Solution:
    def sieveOfEratosthenes(self, N):
        p=2
        prime=[True for i in range(N+1)]

        while(p*p<=N):
            if(prime[p]==True):
                for i in range(p*p,N+1,p):
                    prime[i]=False
            p+=1
        res=[]
        for i in range(2,N+1):
            if(prime[i]==True):
                res.append(i)

        return res


if __name__ == '__main__':

    T=int(input())
    for i in range(T):
        N=int(input())
        s=Solution()
        p=s.sieveOfEratosthenes(N)
        for i in p:
            print(i, end=" ")
