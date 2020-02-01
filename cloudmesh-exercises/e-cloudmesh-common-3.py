# sp20-516-231 E.Cloudmesh.Common.3

from cloudmesh.common.FlatDict import FlatDict

aboutme={
        'age': 25,
        'name': {
            'first': 'Brian',
            'middle': 'Joseph',
            'last': 'Kegerreis'
            }
        }
flat=FlatDict(aboutme,sep='_')


print(aboutme['name']['middle'])
print(flat['name_middle'])
