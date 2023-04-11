class Solution:
	def binary_to_decimal(self, str):
		c,res=0,0
		str=str[::-1]
		for i in str:
		   res=res+int(i)*pow(2,c)
		   c=c+1
		return res


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        str=input()
        s=Solution()
        print(s.binary_to_decimal(str))



