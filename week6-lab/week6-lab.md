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
[web service outputs] (
