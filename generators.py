# generators return iterable
def i_make_generator():
    yield (1)
    yield (2)
    yield (3)


# i_make_generator() gives us a generator
x = i_make_generator()
print(x)

for iterator in x:
    print(iterator)
