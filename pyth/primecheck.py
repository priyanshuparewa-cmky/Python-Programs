original_list = [3, 7, 2, 8, 1, 6, 5, 10, 12, 13, 17, 19]


prime_list = []

# Iterate through each number in the original list
for num in original_list:
    if num > 1:  # Only check numbers greater than 1
        is_prime = True  # Assume the number is prime
        
        # Check for factors from 2 to the square root of num
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:  # Found a divisor, so it's not prime
                is_prime = False
                break  # No need to check further
        
        if is_prime:  
            prime_list.append(num)

prime_sum = 0
for prime in prime_list:
    prime_sum += prime

print("Original List:", original_list)
print("List of Prime Numbers:", prime_list)
print("Sum of Prime Numbers:", prime_sum)
