# starting a mongo container
```
# 27017 is already in use
$ sudo docker run --name mymongo -d -p 27018:27018 bk-mongo-1:v1
# need to find out what host name to use to access the container
$ sudo docker inspect mymongo | grep IPAddress
# 172.17.0.2
$ mongo --host 172.17.0.2
# put some test data in the database
> use test
> db.hello.insert({message:'hello',recipient:'world'})
> exit
# see if it's there on the docker
$ sudo docker exec -it mymongo mongo
> db.hello.find()
# this should print the hello world entry
> exit
```
