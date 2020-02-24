import typing
from pprint import pprint
from copy import deepcopy, copy
from cloudmesh.common.util import readfile
import textwrap

def echo(word:str, n:int, toupper:bool=False) -> str:
    """
    Repeat a given word some number of times.

    :param word: word to repeat
    :type word: str
    :param n: number of repeats
    :type n: int
    :param toupper: return in all caps?
    :type toupper: bool
    :return: result
    :return type: str
    """
    res=word*n
    if (toupper):
        res=res.upper()
    return res

func = echo

print (func.__annotations__)

template = """
openapi: 3.0.0
info:
  title: {title}
  description: {description}
  version: {version}
servers:
  - url: http://localhost/cloudmesh/{title}
    description: Optional server description, e.g. Main (production) server
paths:
  /{name}:
    get:
      description: {description}
      parameters:
{parameters}
      responses:
{responses}
"""

# backslashes at the start of f-strings gets rid of newline pad
# then use rstrip to get rid of any trailing newline pads

def generate_parameter(name, _type, description):
    spec = textwrap.dedent(f"""\
        - in: query
          name: {name}
          description: {description}
          schema:
            type: {_type}
    """)
    return spec

def generate_response(code:str, return_type, description):
    spec = textwrap.dedent(f"""\
      '{code}':
        description: {description}
        content:
          text/plain:
            schema:
              type: {return_type}
        """)
    return spec

def generate_openapi(f, write=True):
    description = f.__doc__.strip().split("\n")[0]
    try:
        version = open('../VERSION','r').read()
    except FileNotFoundError:
        version='test'
    title = f.__name__
    parameters=''
    responses=''
    for parameter, _type in func.__annotations__.items():
        if _type == int:
            _type = 'integer'
        elif _type == float:
            _type = 'float'
        elif _type == bool:
            _type = 'boolean'
        elif _type == str:
            _type = 'string'
        else:
            _type = 'unknown'
        if parameter == 'return':
            responses=generate_response('200', _type, 'not yet available, check function docstring',)
        else:
            parameters = parameters + generate_parameter(parameter, _type, 'not yet available, check function docstring')
    parameters = textwrap.indent(parameters,' '*8).rstrip()
    responses = textwrap.indent(responses,' '*8)
    spec = template.format(
        title = title,
        name = f.__name__,
        description = description,
        version = version,
        parameters = parameters,
        responses = responses
    )
    if write:
        with open(f"{title}.yaml",'w') as fh:
            fh.write(spec)
    return spec

#def generate_openapi(f, write=True):
#    description = f.__doc__.strip().split("\n")[0]
#    version = open('../VERSION','r').read()
#    title = f.__name__
#
#    spec = template.format(
#        title = title,
#        name = f.__name__,
#        description = description,
#        version = version
#    )
#
#    if write:
#        version = open(f"{title}.yaml", 'w').write(spec)
#
#    return spec

spec = generate_openapi(func)


print(spec)

#for parameter, _type in  func.__annotations__.items():
#    if parameter == "return":
#        break
#    print (parameter, _type)
#    if _type == int:
#        _type = 'integer'
#    elif _type == bool:
#        _type = 'boolean'
#    elif _type == float:
#        _type = 'float'
#    elif _type == str:
#        _type = 'string'
#    else:
#        _type = 'unkown'
#
#    spec = generate_parameter(parameter, _type, "not yet available, you can read it from docstring")
#    print(spec)


