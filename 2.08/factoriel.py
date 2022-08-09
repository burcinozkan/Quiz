def sum_divisors(n):
  sum = 0
  i=1
  while i<n:
      if n%i==0:
          sum += i

      i+=1
  return sum



print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18