def data_type(args):
    if type(args) == str:
        return len(args)

    elif type(args) == bool:
        return args

    elif type(args) == int:
        if args < 100:
          return 'less than 100'
        elif args > 100:
          return 'more than 100'
        else:
          return 'equal to 100'
    elif type(args) == list:
        if len(args) < 3:
          return None
        return args[2]
    else:
      return "no value"
