# gRPC-Distributed-Bank

## Prerequisites
Python 3.5 or higher
pip version 9.0.1 or higher

## Setting Up
$ python3 -m pip install virtualenv
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ python -m pip install --upgrade pip
$ pip install grpcio grpcio-tools



python -m grpc_tools.protoc -I./proto --python_out=./generated --grpc_python_out=./generated ./proto/*.proto

docker build -t gprc-python .
docker run  -p 50053:50053 -e BRANCH_ID=1 -d  gprc-python
