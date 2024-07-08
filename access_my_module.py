# import the entire module
import mymodule

mymodule.greet("Alice")

# import specific items from the module
from mymodule import MathOperations
sum= MathOperations.add(5, 3)
sub= MathOperations.subtract(5, 3)
print(sum)
print(sub)