"""Print the largest possible number numerically that can be 
generated using at max that many number of matchsticks which 
was used to generate N.
https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/seven-segment-display-nov-easy-e7f87ce0/
"""
t = int(input())
for _ in range(t):
    n = list(map(int, input().strip()))
    seg=0
    out=''
    for d in n:
        if d==1:  seg+=2
        elif d==7:  seg+=3
        elif d==4:  seg+=4
        elif d==2 or d==3 or d==5:  seg+=5
        elif d==0 or d==6 or d==9:    seg+=6
        elif d==8:  seg+=7
    if seg%2==0:
        while seg!=0:
            out += '1'
            seg-=2
    else:
        seg-=3
        out+='7'
        while seg!=0:
            out+='1'
            seg-=2
    print(out)