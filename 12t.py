x = int(input("Enter seconds: "))
D = x//86400
H = (x//3600) - (D*24)
M = (x//60) - (x//3600 * 60)
S = x % 60
print(f"Converted time in D:HH:MM:SS format : {D}:{H}:{M}:{S}")