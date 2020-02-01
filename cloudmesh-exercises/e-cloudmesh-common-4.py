# sp20-516-231 E.Cloudmesh.Common.4

from cloudmesh.common.Shell import Shell

print("`ls *py`")
result=Shell.ls('*py')
print(result)
print("`grep import *py`")
result=Shell.execute('grep',['import','*py'])
print(result)
