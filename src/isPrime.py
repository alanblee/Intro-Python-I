# write a function that checks if a number is prime
# a prime number is an int that only has exactly 2 positive divisors
# 1 is not prime only divisible by itself
# 2 is prime, 3 is prime both divisible by itself and 1
# 4 is not prime, divisible by 2, itself and 1


# const isPrime = (num) => {
#   if(num <= 1) {
#     return false
#   }else if(num <= 3) {
#     return true
#   }else if(num % 2 === 0 || num % 3 === 0) {
#     return false
#   }

#   //handles every other number if its not caught by the first block of conditional
#   for(let i = 2; i < num; i++) {
#     if(num % i === 0) {
#       return false
#     }
#     return true
#   }
# } written in js first


def isPrime(num):
    # check if num is less than or equal to 1,
    if num <= 1:
        return f"{False}, {num} is not a prime number"
    elif num <= 3:
        return f"{True}, {num} is a prime number"
    elif num % 2 == 0 or num % 3 == 0:
        return f"{False}, {num} is not a prime number"

    for i in range(2, num, 1):
        if num % i == 0:
            return f"{False}, {num} is not a prime number"
        else:
            return f"{True}, {num} is a prime number"


print(isPrime(5))  # should return true
print(isPrime(1))  # should return false
print(isPrime(2))  # should return true
print(isPrime(3))  # should return true
print(isPrime(4))  # should return false
print(isPrime(9))  # should return false
print(isPrime(11))  # should return true
print(isPrime(49))  # should return false
print(isPrime(62))  # should return false
print(isPrime(83))  # should return true
