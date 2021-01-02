
# Juan Carlos Juárez

def fizzBuzz(number):
  nums= []
  for i in range (1,number+1):
    if(i%3==0 and i%5==0):
      nums.append("FizzBuzz")
    elif(i%3==0):
      nums.append("Fizz")
    elif(i%5==0):
      nums.append("Buzz")
    else:
      nums.append(i)
  return nums

print("FizzBuzz Code")
number= int(input())
numa=fizzBuzz(number)
print(numa)


