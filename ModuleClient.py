# put mymodule.py file in site package
import mymodule                             # import module
from mymodule import myFunction             # import function from module
import mymodule as md
mymodule.myFunction()                       # call function
myFunction()                                # call function directly
md.myFunction()
