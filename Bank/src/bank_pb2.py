# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bank.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='bank.proto',
  package='banking',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nbank.proto\x12\x07\x62\x61nking\")\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"4\n\x0fWithdrawRequest\x12\x10\n\x08\x62ranchid\x18\x01 \x01(\x05\x12\x0f\n\x07\x61mmount\x18\x02 \x01(\x05\"3\n\x0e\x44\x65positRequest\x12\x10\n\x08\x62ranchid\x18\x01 \x01(\x05\x12\x0f\n\x07\x61mmount\x18\x02 \x01(\x05\"\"\n\x0e\x42\x61lanceRequest\x12\x10\n\x08\x62ranchid\x18\x01 \x01(\x05\"2\n\x0f\x42\x61lanceResponse\x12\x0f\n\x07\x61mmount\x18\x01 \x01(\x05\x12\x0e\n\x06status\x18\x02 \x01(\t\"\x1c\n\x08\x42ranchID\x12\x10\n\x08\x62ranchid\x18\x01 \x01(\x05\"&\n\x11ProcessIDResponse\x12\x11\n\tprocessid\x18\x01 \x01(\x05\"\x0c\n\nWichBranch2\xfd\x03\n\x07\x42\x61nking\x12\x35\n\x07\x44\x65posit\x12\x17.banking.DepositRequest\x1a\x0f.banking.Status\"\x00\x12\x37\n\x08Withdraw\x12\x18.banking.WithdrawRequest\x1a\x0f.banking.Status\"\x00\x12?\n\x11Propogate_Deposit\x12\x17.banking.DepositRequest\x1a\x0f.banking.Status\"\x00\x12\x41\n\x12Propogate_Withdraw\x12\x18.banking.WithdrawRequest\x1a\x0f.banking.Status\"\x00\x12<\n\x05Query\x12\x17.banking.BalanceRequest\x1a\x18.banking.BalanceResponse\"\x00\x12<\n\tProcessID\x12\x11.banking.BranchID\x1a\x1a.banking.ProcessIDResponse\"\x00\x12?\n\x11Propagate_Deposit\x12\x17.banking.DepositRequest\x1a\x0f.banking.Status\"\x00\x12\x41\n\x12Propagate_Withdraw\x12\x18.banking.WithdrawRequest\x1a\x0f.banking.Status\"\x00\x62\x06proto3'
)




_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='banking.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='banking.Status.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='banking.Status.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=64,
)


_WITHDRAWREQUEST = _descriptor.Descriptor(
  name='WithdrawRequest',
  full_name='banking.WithdrawRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='branchid', full_name='banking.WithdrawRequest.branchid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ammount', full_name='banking.WithdrawRequest.ammount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=66,
  serialized_end=118,
)


_DEPOSITREQUEST = _descriptor.Descriptor(
  name='DepositRequest',
  full_name='banking.DepositRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='branchid', full_name='banking.DepositRequest.branchid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ammount', full_name='banking.DepositRequest.ammount', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=171,
)


_BALANCEREQUEST = _descriptor.Descriptor(
  name='BalanceRequest',
  full_name='banking.BalanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='branchid', full_name='banking.BalanceRequest.branchid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=207,
)


_BALANCERESPONSE = _descriptor.Descriptor(
  name='BalanceResponse',
  full_name='banking.BalanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ammount', full_name='banking.BalanceResponse.ammount', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='banking.BalanceResponse.status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=259,
)


_BRANCHID = _descriptor.Descriptor(
  name='BranchID',
  full_name='banking.BranchID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='branchid', full_name='banking.BranchID.branchid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=261,
  serialized_end=289,
)


_PROCESSIDRESPONSE = _descriptor.Descriptor(
  name='ProcessIDResponse',
  full_name='banking.ProcessIDResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='processid', full_name='banking.ProcessIDResponse.processid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=329,
)


_WICHBRANCH = _descriptor.Descriptor(
  name='WichBranch',
  full_name='banking.WichBranch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=343,
)

DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['WithdrawRequest'] = _WITHDRAWREQUEST
DESCRIPTOR.message_types_by_name['DepositRequest'] = _DEPOSITREQUEST
DESCRIPTOR.message_types_by_name['BalanceRequest'] = _BALANCEREQUEST
DESCRIPTOR.message_types_by_name['BalanceResponse'] = _BALANCERESPONSE
DESCRIPTOR.message_types_by_name['BranchID'] = _BRANCHID
DESCRIPTOR.message_types_by_name['ProcessIDResponse'] = _PROCESSIDRESPONSE
DESCRIPTOR.message_types_by_name['WichBranch'] = _WICHBRANCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:banking.Status)
  })
_sym_db.RegisterMessage(Status)

WithdrawRequest = _reflection.GeneratedProtocolMessageType('WithdrawRequest', (_message.Message,), {
  'DESCRIPTOR' : _WITHDRAWREQUEST,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:banking.WithdrawRequest)
  })
_sym_db.RegisterMessage(WithdrawRequest)

DepositRequest = _reflection.GeneratedProtocolMessageType('DepositRequest', (_message.Message,), {
  'DESCRIPTOR' : _DEPOSITREQUEST,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:banking.DepositRequest)
  })
_sym_db.RegisterMessage(DepositRequest)

BalanceRequest = _reflection.GeneratedProtocolMessageType('BalanceRequest', (_message.Message,), {
  'DESCRIPTOR' : _BALANCEREQUEST,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:banking.BalanceRequest)
  })
_sym_db.RegisterMessage(BalanceRequest)

BalanceResponse = _reflection.GeneratedProtocolMessageType('BalanceResponse', (_message.Message,), {
  'DESCRIPTOR' : _BALANCERESPONSE,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:banking.BalanceResponse)
  })
_sym_db.RegisterMessage(BalanceResponse)

BranchID = _reflection.GeneratedProtocolMessageType('BranchID', (_message.Message,), {
  'DESCRIPTOR' : _BRANCHID,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:banking.BranchID)
  })
_sym_db.RegisterMessage(BranchID)

ProcessIDResponse = _reflection.GeneratedProtocolMessageType('ProcessIDResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROCESSIDRESPONSE,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:banking.ProcessIDResponse)
  })
_sym_db.RegisterMessage(ProcessIDResponse)

WichBranch = _reflection.GeneratedProtocolMessageType('WichBranch', (_message.Message,), {
  'DESCRIPTOR' : _WICHBRANCH,
  '__module__' : 'bank_pb2'
  # @@protoc_insertion_point(class_scope:banking.WichBranch)
  })
_sym_db.RegisterMessage(WichBranch)



_BANKING = _descriptor.ServiceDescriptor(
  name='Banking',
  full_name='banking.Banking',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=346,
  serialized_end=855,
  methods=[
  _descriptor.MethodDescriptor(
    name='Deposit',
    full_name='banking.Banking.Deposit',
    index=0,
    containing_service=None,
    input_type=_DEPOSITREQUEST,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Withdraw',
    full_name='banking.Banking.Withdraw',
    index=1,
    containing_service=None,
    input_type=_WITHDRAWREQUEST,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Propogate_Deposit',
    full_name='banking.Banking.Propogate_Deposit',
    index=2,
    containing_service=None,
    input_type=_DEPOSITREQUEST,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Propogate_Withdraw',
    full_name='banking.Banking.Propogate_Withdraw',
    index=3,
    containing_service=None,
    input_type=_WITHDRAWREQUEST,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Query',
    full_name='banking.Banking.Query',
    index=4,
    containing_service=None,
    input_type=_BALANCEREQUEST,
    output_type=_BALANCERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ProcessID',
    full_name='banking.Banking.ProcessID',
    index=5,
    containing_service=None,
    input_type=_BRANCHID,
    output_type=_PROCESSIDRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Propagate_Deposit',
    full_name='banking.Banking.Propagate_Deposit',
    index=6,
    containing_service=None,
    input_type=_DEPOSITREQUEST,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Propagate_Withdraw',
    full_name='banking.Banking.Propagate_Withdraw',
    index=7,
    containing_service=None,
    input_type=_WITHDRAWREQUEST,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BANKING)

DESCRIPTOR.services_by_name['Banking'] = _BANKING

# @@protoc_insertion_point(module_scope)
