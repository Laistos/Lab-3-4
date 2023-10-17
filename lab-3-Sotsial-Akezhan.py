# task 1
try:
   N = int(input())
   i = 1
   while i <= N:
      if i % 2 == 0:
         print(i)
      i += 1
except ValueError:
   print('error')

# #task 2
# try:
#    n = int(input())
#    if n < 0:
#       print("Factorial is not defined for negative numbers.")
#    elif n == 0:
#       print("1")
#    else:
#       factorial = 1
#       i = 1
#       while i <= n:
#          factorial *= i
#          i += 1
#       print(factorial)
# except ValueError:
#    print('error')

# # task 3
# try:
#    while(True):
#       n = int(input())
#       if (n == 42):
#          break
# except ValueError:
#    print('error')

# #task 4
# try:
#    word = str(input())
#    count = word.count('a')
#    print(f"The number of 'a's in the string is: {count}")

# except ValueError:
#    print('error')

# #task 5
# try:
#    num = int(input())
#    sum = 0
#    while (num > 0):
#       digit = num % 10
#       sum += digit
#       num = num // 10
#    print(sum)
# except ValueError:
#    print('error')

# #task 6
# try:
#    fib1 = 0
#    fib2 = 1
#    n = int(input())
#    i = 0
#    while i < n - 2:
#       fib_sum = fib1 + fib2
#       fib1 = fib2
#       fib2 = fib_sum
#       i = i + 1
#    print(fib2)
# except ValueError:
#    print('error')

# #task 7 
# try:
#    word = str(input())
#    reversed_word = word[::-1]
#    print(reversed_word)
# except ValueError:
#    print('error')

# # task 8
# try:
#    sum = 0
#    counter = 0
#    max_inputs = 5
#    while (counter < max_inputs):
#       num = int(input())
#       if num % 2 == 0:
#          counter += 1
#          continue
#       sum += num
#       counter += 1
#    print(sum)
# except ValueError:
#    print('error')

# # task 9
# try:
#    import random
#    random_num = random.randint(1, 100)
#    while(True):
#       guess = int(input())
#       if (guess < random_num):
#          print('Too small!')
#       elif (guess > random_num):
#          print('Too large')
#       else:
#          print('great')
#          break
# except ValueError:
#    print('error')

# # task 10
# try:
#    while(True):
#       palindrome = str(input())
#       if (palindrome == palindrome[::-1]):
#          print('it is a palindrome')
#          break
#       else:
#          print('it is not a palindrome')
# except ValueError:
#    print('error')

# # task 11
# try:
#    num = int(input())
#    pow = int(input())
#    count = 0
#    result = 1
#    while count < pow:
#       result *= num
#       count += 1
#    print(result)
# except ValueError:
#    print('error')

# # task 12
# try:
#    n = int(input())
#    if n <= 1:
#       print("There are no prime numbers in the given range.")
#    else:
#       print("Prime numbers in the range from 1 to", N, "are:")
#       num = 2
#       while num <= n:
#          is_prime = True
#          divisor = 2
#          while divisor * divisor <= num:
#                if num % divisor == 0:
#                   is_prime = False
#                   break
#                divisor += 1
#          if is_prime:
#             print(num, end=" ")
#          num += 1
#       print()
# except ValueError:
#    print('error')

# #task 13
# try:
#    num = int(input())
#    reversed_number = str(num)[::-1]
#    print(reversed_number)
# except ValueError:
#    print('error')

# # task 14
# try:
#    def is_prime(num):
#       if num < 2:
#          return False
#       for i in range(2, int(num**0.5) + 1):
#          if num % i == 0:
#             return False
#       return True

#    def next_prime(num):
#       num += 1
#       while True:
#          if is_prime(num):
#             return num
#          num += 1
   
#    while True:
#       num = int(input())

#       if is_prime(num):
#          print(f"{num} - prime number")
#       else:
#          print(f"{num} not a prime number")
#          next = next_prime(num)
#          print(f"next prime number {next}")

#       choice = input("Do you want to continue? (yes/no): ")
#       if choice.lower() != 'yes':
#          break
# except ValueError:
#    print('error')

# #task 15
# try:
#    word = str(input())
#    shift = int(input())
#    alphabet = "abcdefghijklmnopqrstuvwxyz"
#    encrypted_text = ""
#    for char in word:
#       if char.isalpha():
#          index = (alphabet.index(char) + shift) % 26  
#          new_char = alphabet[index]  
#          encrypted_text += new_char
#    print(encrypted_text)
# except ValueError:
#    print('error')