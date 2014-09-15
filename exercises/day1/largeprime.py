
def is_prime(num):
    for j in range(2,num):
        if (num % j) == 0:
            return False
    return True

num=1000
004

while True:
  if is_prime(num):
    print 'Prime Number greater than 1000 003: ', num
    break
  num = num + 1

