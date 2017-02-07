def fizz_buzz(args):
  if (args <= 0):
    return "Ensure the number is greater than zero"
  else:
    if args % 3 == 0 & args % 5 == 0:
      return "FizzBuzz"
    elif args % 5 == 0:
      return "Buzz"
    elif args % 3 == 0:
      return "Fizz"
    else:
      return args
