var1 = 5


def some_func():
    # var2 is in the local namespace
    var2 = 6

    def some_inner_func():
        # var3 is in the nested local
        # namespace
        var3 = 7

# var 1 is global name space
