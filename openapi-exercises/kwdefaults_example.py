def foo(x:int, y:str='hello', *args, z:str='goodbye', pi:float=3.14) -> int:
    return 1

print('__annotations__:')
for parameter, _type in foo.__annotations__.items():
    print('parameter: ' + parameter)
    print('type: ' + str(_type))
print()
print('__kwdefaults__:')
for parameter, default in foo.__kwdefaults__.items():
    print('parameter: ' + parameter)
    print('default: ' + str(default))
print()
print('put them together')
for parameter, _type in foo.__annotations__.items():
    default=None
    print('parameter: ' + parameter)
    print('type: ' + str(_type))
    if parameter in foo.__kwdefaults__.keys():
        default=foo.__kwdefaults__[parameter]
        print('default: ' + str(default))

