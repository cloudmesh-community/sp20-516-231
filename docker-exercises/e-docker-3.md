# docker communication
```
$ MONGO_USER=`cms config value cloudmesh.data.mongo.MONGO_USERNAME | tail -n1`
$ MONGO_PW=`cms config value cloudmesh.data.mongo.MONGO_PASSWORD | tail -n1`
$ sudo docker network create mongo-net
$ sudo docker run -d --network mongo-net -e MONGO_INITDB_ROOT_USERNAME=${MONGO_USER} -e MONGO_INITDB_ROOT_PASSWORD=${MONGO_PW} --name mongo-auth bk-mongo-1:v1
$ sudo docker build -t bk-cms-mongo-user:v1 -f ./e-docker-3.Dockerfile --build-arg mongo_user=$MONGO_USER --build-arg mongo_pw=$MONGO_PW .
# the new container will automatically authenticate and connect to mongo-auth using the supplied build arguments
$ sudo docker run --rm -it --network mongo-net bk-cms-mongo-user:v1
# now you can run mongo commands to your heart's content
```

1. the dockerfile needs to have a mongo installation and needs to know the username and password to authenticate with the mongo host container

2. we outcommented the mongodb related tasks in the dockerfile so that it doesn't try to create its own database when it builds

3. need to set up a docker bridge network so they can communicate

4. docker compose could help so we don't have to execute multiple run commands and repeat the variables used to set up authentication

5. cloudmesh.yaml contains passwords that shouldn't be made available

6. anyone on dockerhub could inspect private files like cloudmesh.yaml and break into any cloud accounts that have username and password information in them

