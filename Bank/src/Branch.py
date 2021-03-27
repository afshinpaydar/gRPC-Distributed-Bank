from google.protobuf import message
import grpc
from concurrent import futures
import bank_pb2
import bank_pb2_grpc
import json
import sys
from multiprocessing import Process
import os
import threading
import time


PORT = 50053

class Branch(bank_pb2_grpc.BankingServicer):

    def __init__(self, id, balance, processid):
        # unique ID of the Branch
        self.id = id
        self.processid = processid
        # replica of the Branch's balance
        self.balance = balance
        # the list of process IDs of the branches, this list will update by find_process_ids function
        self.branches = []
        # the list of Client stubs to communicate with the branches
        self.stubList = list()
        # a list of received messages used for debugging purpose
        self.recvMsg = list()

  
    def Query(self,request, context):
      self.recvMsg.append(request)
      try:
        return bank_pb2.BalanceResponse(ammount=self.balance[request.branchid - 1]['balance'], status="success")
      except:
        return bank_pb2.BalanceResponse(ammount=-1, status="failed")
    def Deposit(self,request, context):
      self.recvMsg.append(request)
      try:
        if request.branchid == self.id:
          self.balance[request.branchid - 1]['balance'] += request.ammount
          # We don't use all_response retun value, but we can check it for debug
          responses_other_branches = self.Propagate_Deposit(bank_pb2.DepositRequest(branchid= self.id , ammount = request.ammount))
          return bank_pb2.Status(status="success", message=f"Deposit {request.ammount} in branch {self.balance[request.branchid - 1]['id']}," \
            f" remaining balance: {self.balance[request.branchid - 1]['balance']}")
        else:
          self.balance[request.branchid - 1]['balance'] += request.ammount
          return bank_pb2.Status(status=f"success", message=f"Deposit updated! branch {self.id}")
      except:
        return bank_pb2.Status(status="failed", message=f"Can not withdraw {request.ammount} from branch {self.balance[request.branchid - 1]['id']}")

    def Withdraw(self,request, context):
      self.recvMsg.append(request)
      try:
        if int(self.balance[request.branchid - 1]['balance']) >= request.ammount:
          if request.branchid == self.id:
            self.balance[request.branchid - 1]['balance'] -= request.ammount
            # We don't use all_response retun value, but we can check it for debug
            responses_other_branches = self.Propagate_Withdraw(bank_pb2.WithdrawRequest(branchid= self.id , ammount = request.ammount))
            return bank_pb2.Status(status="success", message=f"Withdraw {request.ammount} from branch {self.balance[request.branchid - 1]['id']}," \
              f" remaining balance: {self.balance[request.branchid - 1]['balance']}") 
          else:
            self.balance[request.branchid - 1]['balance'] -= request.ammount
            return bank_pb2.Status(status=f"success", message=f"Withdraw updated! branch {self.id}")
        else:
          return bank_pb2.Status(status="failed!!!!!", message=f"Can not withdraw {request.ammount} from branch {self.balance[request.branchid - 1]['id']}")
      except:
        return bank_pb2.Status(status="failed", message=f"Can not withdraw {request.ammount} from branch {self.balance[request.branchid - 1]['id']}")

    def Propagate_Deposit(self,request):
      # list of update response from all branches
      all_response = []
      for branch_id in range( 1, len(self.branches) + 1):
        if branch_id != self.id: 
          stub = bank_pb2_grpc.BankingStub(grpc.insecure_channel('localhost:'+str(50053 + branch_id)))
          all_response.append(stub.Deposit(bank_pb2.DepositRequest(branchid=request.branchid, ammount = request.ammount), timeout= 3))
      return all_response

    def Propagate_Withdraw(self,request):
      # list of update response from all branches
      all_response = []
      for branch_id in range( 1, len(self.branches) + 1):
        if branch_id != self.id: 
          stub = bank_pb2_grpc.BankingStub(grpc.insecure_channel('localhost:'+str(50053 + branch_id)))
          all_response.append(stub.Withdraw(bank_pb2.WithdrawRequest(branchid=request.branchid, ammount = request.ammount), timeout= 3))
      return all_response


    def ProcessID(self,request, context):
      return bank_pb2.ProcessIDResponse(processid=self.processid) 

    # Update list of process IDs of the branches for each branch
    def update_process_list(self):
      branch_process = []
      while True:
        try:
          process_file = open("/tmp/process_file.txt", "r")
          lines = process_file.readlines()
          for process in lines:
            if process not in self.branches:
              self.branches.append(process)
          time.sleep(10)
        except:
          pass


def MsgDelivery(branch_id,balance):
  process_id = os.getpid()
  process_file = open("/tmp/process_file.txt", "a+")
  process_file.write(str(process_id)+"\n")
  process_file.close()
  MsgDelivery = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
  branch = Branch(branch_id, balance, process_id)
  update_process_list_thread = threading.Thread(target=branch.update_process_list, args=())
  bank_pb2_grpc.add_BankingServicer_to_server(branch, MsgDelivery)
  MsgDelivery.add_insecure_port('localhost:'+ str(PORT+branch_id))
  MsgDelivery.start()
  print(f"Branch {branch_id} is up and running on port {PORT + branch_id} !!!")
  update_process_list_thread.start()
  MsgDelivery.wait_for_termination()

if __name__ == '__main__':
  balance = []
  with open(sys.argv[1], 'r') as file:
    data = json.load(file)

  for item in data:
    if item["type"] == "branch":
      balance.append({"id":item["id"], "balance":item["balance"]})
  try:
    os.remove("/tmp/process_file.txt")
  except:
    pass
  for item in data:
    processes = []
    if item["type"] == "branch":
      p = Process(target=MsgDelivery, args=(item["id"],balance))
      processes.append(p)
      p.start()
  for proc in processes:
    proc.join()

