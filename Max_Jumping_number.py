#https://practice.geeksforgeeks.org/problems/jumping-numbers3805/1

class Solution:
    def jumpingNums(self, X):
        # code here 
        for i in range(X,1,-1):
            s=str(i)
            k=s[0]
            c=1
            for j in range(1,len(s),1):
                if(abs(int(k)-int(s[j])) == 1):
                    k=s[j]
                    c=c+1
                else:
                    break
            if(c==len(s)):
                return i

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        k=int(input())
        s=Solution()
        print(s.jumpingNums(k))


"""
#User function Template for python3

#User function Template for python3



class Solution:
    def jumpingNums(self, X):
        lst=[1,2,3,4,5,6,7,8,9]
        ans=0
        while lst:
            num=lst.pop()
            if num>X:
                continue
            ans=max(num,ans)
            l=num%10
            if l!=0:
                lst.append(num*10+(l-1))
            if l!=9:
                lst.append(num*10+(l+1))
        return ans
"""


    