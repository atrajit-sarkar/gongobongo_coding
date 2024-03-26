def is_prime(n):
  if n == 1:
   return False


  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True
p_factors=[]
def p_factorise(n):
  for i in range(2,n+1):
    if n%i==0 and is_prime(i):
      p_factors.append(i)

  return p_factors
n=int(input("Enter the number:"))
print(p_factorise(n))