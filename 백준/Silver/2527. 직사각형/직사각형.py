for _ in range(4):
    x1,y1,x2,y2,p1,q1,p2,q2 = map(int, input().split())
    if x2 < p1 or p2 < x1 or y2 < q1 or q2 < y1:
        ans = 'd'
    elif (x2, y2)==(p1,q1) or (x2, y1)==(p1,q2) or (x1,y1)==(p2,q2) or (x1,y2)==(p2,q1):
        ans = 'c'
    elif (y2==q1 and x1<p2 and p1<x2) or (x2==p1 and q1<y2 and y1<q2) or (y1==q2 and p1<x2 and x1<p2) or (x1==p2 and q1<y2 and y1<q2):
        ans = 'b'
    else:
        ans = 'a'
    print(ans)