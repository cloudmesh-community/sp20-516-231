# sp20-516-231 E.Cloudmesh.Common.5

from cloudmesh.common.StopWatch import StopWatch
from time import sleep

print('cubing every number from 0 to 4,999,999...')
StopWatch.start('cubes')
#sleep(1)
for i in range(5000000):
    x=i**3
StopWatch.stop('cubes')
print(StopWatch.get('cubes'))
