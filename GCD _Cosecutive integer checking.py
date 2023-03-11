
# Steps:
#   1: Assign min(m,n) to t
#   2: if m%t is equal to zero then go to step 3, otherwise step 4
#   3: if n%t is equal to zero then return the answer, otherwise go to step 4
#   4: Decrase t by one and go to step 2

def gcd (m,n):
    t = min(m,n)
    while t>=0:
        if m%t==0 and n%t==0:
            return t
        else :
            t=t-1

m = int(input("Enter m: "))
n = int(input("Enter n: "))
print(f"The greatest common divisor of {m} and {n} is : {gcd(m,n)}")