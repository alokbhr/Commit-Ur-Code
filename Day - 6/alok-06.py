for i in range(int(input())):
     P, a, b, c, x, y = map(int, input().split())
     p_one_anar = x*a+b
     p_one_rocket = y*a+c
     print(max(p_one_anar,p_one_rocket))
