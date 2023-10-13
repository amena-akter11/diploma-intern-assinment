def sum(first,second):
  print(f" The summetion result is {first} + {second} = {first+ second}")


def subtraction(first, second):
  return f"The subtraction result is {first - second}" 
result = subtraction(20, 5)

def multiplication(first, second, third, fourth):
  return f" The multiplication result is {first * second * third * fourth}"
multiply_inside_the_method = multiplication(2, 4, 6, 12)


sum(13, 11)
print(result)
print(multiply_inside_the_method)



def division(first, second):

  divide = (first / second)
  print(f"Division result is {divide}")

  modulus = (first % second)
  if modulus != 0:
    print(f"Modulus result is {modulus}")

  else:
    return

division(15,2)


