# sp20-516-231 E.Cloudmesh.Common.2

from cloudmesh.common.dotdict import dotdict

# dotdict example
my_dict={
        'first': 'Brian',
        'middle': 'Joseph',
        'last': 'Kegerreis'
        }
my_dotdict=dotdict(my_dict)
try:
    print(my_dict.first)
except:
    print("my_dict.first doesn't work")
    print("try using dotdict instead")
print(my_dotdict.first)
print(my_dotdict.middle)
print(my_dotdict.last)
