#https://practice.geeksforgeeks.org/problems/sum-of-all-prime-numbers-between-1-and-n4404/1

class Solution:
    def primesum(self,N):
        sum=0
        p=2
        prime=[True for i in range(N+1)]
        while(p*p<=N):
            if(prime[p]==True):
                for i in range(p*p,N+1,p):
                    prime[i]=False
            p+=1
        
        for i in range(2,N+1):
            if(prime[i]==True):
                sum+=i
                
        return sum

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        s=Solution()
        print(s.primesum(N))