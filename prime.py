
def is_prime(number: int) -> bool:
    """
    Check if number is prime.
    Parameters: number - to check if prime
    Returns: True if prime, False otherwise
    """

    if number == 2:
        # 2 is the only even prime number
        return True

    if number < 2 or number % 2 == 0:
        # 0, 1, negative numbers and even numbers are not prime
        return False
    
    for i in range(3, int(number ** 0.5) + 1, 2):
        # If number is divisible by any number from 3 to sqrt(number),
        # (skip even numbers as they are not prime)
        # it is not prime
        if number % i == 0:
            return False
    
    return True

def get_factors(number: int) -> list:
    """
    Get factors of a number.
    Parameters: number to factorize
    Returns: List of factors of number
    """

    factors = []
    for i in range(1, (number // 2) + 1):
        # If number is divisible by i, then i is a factor of number
        # Only check till number // 2
        if number % i == 0:
            factors.append(i)
    
    return factors

def check_prime(number: int) -> None:
    """
    Check if number is prime.
    Parameters: number - to check if prime or output factors
    Returns: None
    """

    if is_prime(number):
        print("Prime!")
    else:
        factors = get_factors(number)
        print("Factors:", factors)

def generate_primes_in_range(start: int, end: int) -> list:
    """
    Generate prime numbers in a range.
    Parameters:
        start - beginning of range
        end - end of range
    Returns: List of prime numbers in the range
    """

    primes = []

    for i in range(start, end + 1):
        if is_prime(i):
            primes.append(i)
    
    return primes

if __name__ == "__main__":
    
    while True:
        try:
            print(" ------ ")
            print("Options: \
              \n To check for prime number: 1 \
              \n To generate prime numbers in a range: 2 \
              \n To exit: 3")

            option = int(input("Enter Option: "))

            if option == 1:
                input_number = int(input("Enter a Number: "))
                check_prime(input_number)
            elif option == 2:
                start = int(input("Enter start of range: "))
                end = int(input("Enter end of range: "))
                print("Primes: ", generate_primes_in_range(start, end))
            elif option == 3:
                print("Exiting...")
                break
            else:
                print("**Invalid Option. Try again.")
                continue
        except ValueError:
            print("Invalid input.")