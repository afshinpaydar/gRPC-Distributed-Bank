# Simple distributed banking system

## Purpose
This project aims to implement a simple distributed bank system that can either be fault tolerant or highly available using gRPC interface for communication. Written in spring 2021 for CSE 531.

## Architecture design goals
The customers should interact with system as a single coherent system that satisfy these goals:
1.	Access transparency: Customers does not know the implementation details of Branch application.
2.	Support redundancy: Each branch has a replica for other branches
3.	Location transparency: Customers can’t see where the data actually stores
4.	Failure transparency: If a failure happen in the system, customers should not inform about that failure and recovery procedure.
5.	Efficient customer to server and server to server communication


  #### Usage
  ```
$ git clone git@github.com:afshinpaydar/gRPC-Distributed-Bank.git
$ cd gRPC-Distributed-Bank
$ virtualenv -p python3 venv
$ pip install -r requirements.txt

Branch:
$ source venv/bin/activate
$ python Bank/src/Branch.py input.json

Customer:
$ source venv/bin/activate
$ python Bank/src/Customer.py input.json

  ```
  #### Sample Output
  ```
  {'id': 1, 'recv': ["{ 'interface': 'query', 'result': 'success', 'money': 400 }", "{ 'interface': 'withdraw', 'result': 'success' }"]}
  {'id': 2, 'recv': ["{ 'interface': 'deposit', 'result': 'success' }", "{ 'interface': 'query', 'result': 'success', 'money': 570 }"]}
  {'id': 3, 'recv': ["{ 'interface': 'withdraw', 'result': 'success' }", "{ 'interface': 'query', 'result': 'success', 'money': 330 }"]}
  ```
