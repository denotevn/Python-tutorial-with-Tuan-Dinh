from lib2to3.pgen2.token import LESSEQUAL
from time import process_time_ns


is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("The weather is hot")
elif is_cold:
    print("It's cold day")
    print("The weathe is'nt hot")
else:
    print("It's a lovely day")
    print("Enjoy your day")