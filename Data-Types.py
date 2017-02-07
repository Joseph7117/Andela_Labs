def data_type(args):
    if type(args) == str:
        return len(args)

    elif type(args) == None:
        print("no value")

    elif type(args) == bool:
        return args

    elif type(args) == int:
        if args < 100:
            print("less than 100")
        elif args > 100:
            print("more than 100")
        else:
            print("equal to 100")
    elif type(args) == list:
        return args[:3] or None