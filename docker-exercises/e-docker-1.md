# starting a mongo container
```
# 27017 is already in use
$ sudo docker run -d -p 27018:27017 --name mongo1 bk-mongo-1:v1
$ mongo --port 27018
# put some test data in the database
> use test
> db.hello.insert({message:'hello',recipient:'world'})
> exit
# see if it's there on the container
$ sudo docker exec -it mongo mongo
> db.hello.find()
# this should print the hello world entry
# "_id" : ObjectId("5eae3df7afec4ce11d570c60"), "message" : "hello", "recipient" : "world" }
> exit
```
