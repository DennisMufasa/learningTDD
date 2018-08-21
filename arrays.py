# a function that reverses array items
def reversal(x):
    if isinstance(x, list):
        x.reverse()
        return x
