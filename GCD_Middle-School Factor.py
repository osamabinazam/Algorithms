# This algorithm find prime fectors of both numbers first 
# after that it calculates the product of common factors

def prime_factors (number):
    i=2                    
    factors_list= []
    while i*i <=number:
        if number%i ==0:
            number //=i
            factors_list.append(i)   
        else:
            i+=1
    
    if number>1:
        factors_list.append(number)
    return factors_list

def gcd(m,n):
    prime_factors_of_m = prime_factors(m)
    prime_factors_of_n = prime_factors(n)

    #finding common elements
    common_factors = []
    for factor in prime_factors_of_m:
        if factor in prime_factors_of_n:
            common_factors.append(factor)
            prime_factors_of_n.remove(factor)

    # calculating the product of common factors
    gcd =1
    for factor in common_factors:
        gcd *=factor
    return gcd


if __name__ == "__main__":
    m = int(input("Enter m: "))
    n = int(input("Enter n: "))
    print(f"The greatest common divisor of {m} and {n} is : {gcd(m,n)}")

