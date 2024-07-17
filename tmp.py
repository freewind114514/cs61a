from doctest  import testmod
from pathlib import Path
def f(x):
    print(__name__)
    return [1,2,3]
f(1)
if __name__ == '__main__':
    testmod()
    