# sp20-516-231 E.Cloudmesh.Common.1

from cloudmesh.common.util import banner
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.variables import Variables
from math import sqrt

# banner example
banner('here is a banner')

# HEADING example
class HeadingExample():
    
    def __init__(self,x):
        self.x=x
        
    def square_root(self):
        HEADING()
        print(sqrt(self.x))

    def squared(self):
        HEADING()
        print(self.x**2)

my_obj=HeadingExample(4)
my_obj.square_root()
my_obj.squared()

# VERBOSE example
equations = {
        'OnePlusOne': 'Two',
        'TwoPlusTwo': 'Four'
        }
variables=Variables()
variables['verbose']=10
print("variables['verbose'] = 10")
VERBOSE(equations,verbose=11)
print("VERBOSE(equations,verbose=11) didn't print anything")
VERBOSE(equations,verbose=9)
print("VERBOSE(equations,verbose=9) printed something")
