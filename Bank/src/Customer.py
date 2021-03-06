import grpc
import bank_pb2
import bank_pb2_grpc
import json
import sys

PORT = 50053

class Customer:
    def __init__(self, id, events=None):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.stub = None

    def createStub(self):
      self.stub = bank_pb2_grpc.BankingStub(grpc.insecure_channel('localhost:'+str(PORT + self.id)))
      return self.stub

    def executeEvents(self):
      output = {}
      interfaces = []
      stub = self.createStub()
      for event in self.events:
        output['id'] = self.id
        if str(event["interface"]) == "query":
          response = stub.Query(bank_pb2.BalanceRequest(branchid=self.id))
          interfaces.append(f"{{ 'interface': 'query', 'result': '{response.status}', 'money': {response.ammount} }}")
        elif str(event["interface"]) == "withdraw":
          response = stub.Withdraw(bank_pb2.WithdrawRequest(branchid=self.id, ammount = event["money"]))
          interfaces.append(f"{{ 'interface': 'withdraw', 'result': '{response.status}' }}")
        elif str(event["interface"]) == "deposit":
          response = stub.Deposit(bank_pb2.DepositRequest(branchid=self.id, ammount = event["money"]))
          interfaces.append(f"{{ 'interface': 'deposit', 'result': '{response.status}' }}")
        else:
          interfaces.append("Unkown event")
      output['recv'] = interfaces
      return output
  
if __name__ == '__main__':
  
  with open(sys.argv[1], 'r') as file:
    data = json.load(file)
  for item in data:
    output = {}
    interfaces = []
    if str(item["type"]) == "customer":
      customer = Customer(id=int(item["id"]),events=item["events"])
      print(customer.executeEvents())

