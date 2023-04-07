# https://practice.geeksforgeeks.org/problems/print-the-pattern-set-1/1

def printPat(n):
    if (n==1):
        print("1 $")
    elif (n==2):
        print("2 2 1 1 $2 1 $")
    else:
        res=""
        for i in range(n):
            for j in range(n,0,-1):
                """for z in range(n-i):
                    print(j,end=" ")"""
                res+=(n-i)*(str(j)+" ")
            res+="$"
        print(res)

if __name__ == '__main__':
    t=int(int(input()))
    for i in range(t):
        printPat(int(input()))
