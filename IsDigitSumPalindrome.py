class Solution:
    def isDigitSumPalindrome(self,N):
        
        def palindrome(M):
            P=M
            s1=0
            while M>0:
                r=M%10
                s1=s1*10+r
                M=M//10
            print(s1)
            if(s1==P):
                return 1
            else:
                return 0
        s=0
        while N>0:
            r=N%10
            s=s+r
            N=N//10
        print(s)   
        return palindrome(s)

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n=int(input())
        s=Solution()
        result=s.isDigitSumPalindrome(n)
        print(result)
                