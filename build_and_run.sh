# creating a network between the two containers
docker network create server-classifier-network

#building and running the main server
cd server_side
docker build -t main_server__v2.0 .
docker run -d -p 8003:8001 --network server-classifier-network --name cls_server_container__v2.0 cls_server__v2.0
cd ..

# building and running the cls server
cd classifier_server
docker build -t cls_server__v2.0 .
docker run -d -p 8002:8000 --network server-classifier-network --name main_server_container__v2.0 main_server__v2.0
cd ..

