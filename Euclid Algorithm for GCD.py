
# gcd(m,n) = gcd(n,m mod n)

def gcd (m, n):
    if m<=0 or n<=0:
        print("Given unsupported values!")
        return -2
    r =-1
    
    while int (n) != 0:
        r = int (m) % n             # Remainder
        m=n                 # Assign value of m to n
        n=r                 # Assign remainder to  n
    return m        

m = int(input("Enter m: "))
n = int(input("Enter n: "))
print(f"The greatest common divisor of {m} and {n} is : {gcd(m,n)}")


