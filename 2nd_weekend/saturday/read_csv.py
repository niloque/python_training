def read_csv(input_file):

    with open(input_file) as input_file:
        lines = input_file.readlines()
    exctracted = [i.rstrip("\n").split(",") for i in lines]
    return exctracted
    pass
