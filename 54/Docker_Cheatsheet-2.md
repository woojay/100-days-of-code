### Networking ###

#### Port ####
docker container run -p 80:80 ... # Port Out:In (80:80)
  docker container port ...

# Create new virtual network for each app
# "Batteries included, but removable"
# Use host IP (--net=host)


#### IP Address ####
docker container inspect --format '{{ .NetworkSettings.IPAaddress }}' webhost

docker network ls
docker network inspect
docker network create --driver
  docker run -d --name my_nginx --network my_net nginx
docker network [ connect | disconnect ]
  docker network [ connect | disconnect ] my_net {container}


#### DNS ####
IP should not be relied on for networking

Container name works as network aliases w/ auto DNS resolution

Default bridge does not have this feature unless --link is used, but only in custom network

docker run --rm -it centos:7 bash
docker run --rm -it ubuntu:14.04 bash

docker network create my_net
docker container run -d --network my_net --name net1 --net-alias search elasticsearch:2
docker container run -d --network my_net --name net2 --net-alias search elasticsearch:2
docker container run --rm --network my_net alpine nslookup search


