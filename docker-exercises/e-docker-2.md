# mongo container with authorization
```
$ MONGO_USER=`cms config value cloudmesh.data.mongo.MONGO_USERNAME | tail -n1`
$ MONGO_PW=`cms config value cloudmesh.data.mongo.MONGO_PASSWORD | tail -n1`
$ echo $MONGO_USER
# admin
$ echo $MONGO_PW
# sp516Insecure
$ sudo docker run -d -p 27019:27017 -e MONGO_INITDB_ROOT_USERNAME=${MONGO_USER} -e MONGO_INITDB_ROOT_PASSWORD=${MONGO_PW} --name mongo2 bk-mongo-1:v1
# write some commands to execute in the container
$ echo -e 'use admin\nshow users' > script.js
$ mongo --port 27019 -u ${MONGO_USER} -p ${MONGO_PW} < script.js
#MongoDB shell version v4.0.10
#connecting to: mongodb://127.0.0.1:27019/?gssapiServiceName=mongodb
#Implicit session: session { "id" : UUID("6bd8524f-8d7f-485c-b2c8-2d402f83ccf8") }
#MongoDB server version: 4.2.6
#WARNING: shell and server versions do not match
#switched to db admin
#{
#	"_id" : "admin.admin",
#	"userId" : UUID("e0be1487-03a9-4a78-b1b9-0589a010d6a4"),
#	"user" : "admin",
#	"db" : "admin",
#	"roles" : [
#		{
#			"role" : "root",
#			"db" : "admin"
#		}
#	],
#	"mechanisms" : [
#		"SCRAM-SHA-1",
#		"SCRAM-SHA-256"
#	]
#}
#bye
```
