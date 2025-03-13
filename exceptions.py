T = int(input())
if 0 < T < 10:
    for _ in range(T):
        try:
            a, b = map(int, input().split())
            print(a // b)
        except (ZeroDivisionError, ValueError) as e:
            print("Error Code:", e)

        
    
