def find_primes(provided_list):
    prime_numbers = []
    for number in provided_list:
        if prime_number_list(number):
            prime_numbers.append(number)
    print("The prime numbers are ")
    return prime_numbers
    

def prime_number_list(number):
    if number <= 1:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def main():
    expected_list = input("List your numbers separated by -  ")
    new_list = expected_list.split ("-")
    provided_list = []
    for number in new_list:
        provided_list.append(int(number))
    print(find_primes(provided_list))


main()