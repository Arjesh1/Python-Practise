def prime_checker(number) :
  divisible_by = []
  for num in range(1, number + 1):
    remainder = number % num
    if remainder == 0:
      divisible_by.append(num)
  if len(divisible_by) == 2:
    return "It is prime number"
  else:
    return "It is not a prime number"

for _ in range (100):
   n = int(input('Number >> '))
   result = prime_checker(number = n)
   print(result)


