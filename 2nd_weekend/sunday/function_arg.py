def foo(x, y, *args, **kwargs):
    print(x, y, sep=' | ')
    print(args)
    print(kwargs)

foo(1, 2, 20, 30, first_name='Adam', age=100)