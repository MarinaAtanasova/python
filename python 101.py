for c in range(0, 48):
    for b in range(1,c):
        for a in range(1,b):
            if a*a+b*b == c*c:
                print('{:5d},{:5d},{:5d}'.format(a,b,c), (a+b+c))