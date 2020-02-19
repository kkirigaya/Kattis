h,m = map(int, input().split())

mins = (24+h) * 60 + m
mins -= 45
mins %= 24*60
print(mins//60, mins%60)
