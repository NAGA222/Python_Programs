class Solution:
    def armstrongNumber (ob, n):
        m=n
        s=0
        while n>0:
            r=n%10
            n=n//10
            s=s+pow(r,3)
        if(m==s):
            return "Yes"
        else:
            return "NO"

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n=int(input())
        s=Solution()
        result=s.armstrongNumber(n)
        print(result)