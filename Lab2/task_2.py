n = int(input())
if abs(n)>= 10000:
    print("Invalid Data")
else:
    print(f'The next number for the number {n} is {n+1}.')
    print(f'The previous number for the number {n} is {n-1}.')    