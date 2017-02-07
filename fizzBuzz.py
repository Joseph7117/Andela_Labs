def fizz_buzz(args):
  args = abs(args)
  if args % 3 == 0 :
    if args % 5 == 0:
      return "FizzBuzz"
    return "Fizz"
  elif args % 5 == 0:
    return "Buzz"
  else:
    return args
