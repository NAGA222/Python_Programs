#https://practice.geeksforgeeks.org/problems/pairs-of-prime-number2612/1

class Solution:
    def prime_pairs(self,N):
        pairs=[]
        p=2
        prime=[True for i in range(N+1)]
        while(p*p<=N):
            if(prime[p]==True):
                for i in range(p*p,N+1,p):
                    prime[i]=False

            p+=1
        prime1=[]
        for i in range(2,N+1):
            if(prime[i]):
                prime1.append(i)
        res=[]
        for i in range(len(prime1)):
            for j in range(len(prime1)):
                if(prime1[i]*prime1[j]<=N):
                    res.append(prime1[i])
                    res.append(prime1[j])
        
        return res

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        s=Solution()
        res=s.prime_pairs(N)
        for i in res:
            print(i, end=" ")
