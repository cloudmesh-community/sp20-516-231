# cloudmesh commands
```
# create the vm
$ cms vm boot
# ssh into it from two terminals (one to start the server, another to run commands)
$ cms vm ssh 231-bjkegerr-19
# from within the vm:
$ git clone git@github.com:cloudmesh-community/sp20-516-231.git
$ cd sp20-516-231/week6-lab
# start the server
$ python server.py
# submit curl requests
$ curl -X GET "http://localhost:8080/cloudmesh/cache?level=l2" -H "accept: application/json"
$ curl -X GET "http://localhost:8080/cloudmesh/cache?level=l3" -H "accept: application/json"
$ curl -X GET "http://localhost:8080/cloudmesh/cache?level" -H "accept: application/json"
$ curl -X GET "http://localhost:8080/cloudmesh/cache?cache" -H "accept: application/json"
```
# web service outputs
![web service outputs](https://github.com/cloudmesh-community/sp20-516-231/blob/master/week6-lab/web_service_cropped.png)

# python code
## cpu.py
```python
import platform
import re
import subprocess

from flask import jsonify

from cpuinfo import get_cpu_info

def get_processor_name() -> str:
    """
    The name of the processor
    :return: the name of the processor
    """
    #if platform.system() == "Windows":
    #    p = platform.processor()
    #elif platform.system() == "Darwin":
    #    command = "/usr/sbin/sysctl -n machdep.cpu.brand_string"
    #    p = subprocess.check_output(command, shell=True).strip().decode()
    #elif platform.system() == "Linux":
    #    command = "cat /proc/cpuinfo"
    #    all_info = subprocess.check_output(command, shell=True).strip().decode()
    #    for line in all_info.split("\n"):
    #        if "model name" in line:
    #            p = re.sub(".*model name.*:", "", line, 1)
    #else:
    #    p = "cannot find cpuinfo"
    
    i = get_cpu_info()
    p = i['brand']

    pinfo = {"model": p}

    return jsonify(pinfo)

def get_cache_size(level: str='') -> str:
    """
    The cache size of the processor
    :return: the cache size
    """

    i = get_cpu_info()
    l2 = i['l2_cache_size']
    l3 = i['l3_cache_size']
    if level == 'l2':
        cinfo = {level: l2}
    elif level == 'l3':
        cinfo = {level: l3}
    else:
        cinfo = {
                 'caches': {
                   'l3': l3,
                   'l2': l2
                   }
                 }
    return jsonify(cinfo)
```
## cpu.yaml
```yaml
openapi: 3.0.2
info:
  title: cpuinfo
  description: A simple service to get cpuinfo as an example of using OpenAPI 3.0
  license:
    name: Apache 2.0
  version: 0.0.1

servers:
  - url: http://localhost:8080/cloudmesh

paths:
  /cpu:
    get:
      summary: Returns cpu information of the hosting server
      operationId: cpu.get_processor_name
      responses:
        '200':
          description: cpu info
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/cpu"
  /cache:
     get:
       summary: Returns cpu cache size
       operationId: cpu.get_cache_size
       parameters:
         - in: query
           name: level
           description: l2 or l3
           schema:
             type: "string"
       responses:
         '200':
            description: cache size
            content:
              application/json:
                schema:
                  type: "object"
                  additionalProperties: true

components:
  schemas:
    cpu:
      type: "object"
      required:
        - "model"
      properties:
        model:
          type: "string"
```

## server.py
``` python
from flask import jsonify
import connexion

app = connexion.App(__name__, specification_dir="./")

app.add_api("cpu.yaml")

@app.route("/")
def home():
    msg = {"msg": "It's working!"}
    return jsonify(msg)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
```
