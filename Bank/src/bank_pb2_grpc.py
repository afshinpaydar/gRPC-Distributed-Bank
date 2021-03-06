# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import bank_pb2 as bank__pb2


class BankingStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Deposit = channel.unary_unary(
                '/banking.Banking/Deposit',
                request_serializer=bank__pb2.DepositRequest.SerializeToString,
                response_deserializer=bank__pb2.Status.FromString,
                )
        self.Withdraw = channel.unary_unary(
                '/banking.Banking/Withdraw',
                request_serializer=bank__pb2.WithdrawRequest.SerializeToString,
                response_deserializer=bank__pb2.Status.FromString,
                )
        self.Propogate_Deposit = channel.unary_unary(
                '/banking.Banking/Propogate_Deposit',
                request_serializer=bank__pb2.DepositRequest.SerializeToString,
                response_deserializer=bank__pb2.Status.FromString,
                )
        self.Propogate_Withdraw = channel.unary_unary(
                '/banking.Banking/Propogate_Withdraw',
                request_serializer=bank__pb2.WithdrawRequest.SerializeToString,
                response_deserializer=bank__pb2.Status.FromString,
                )
        self.Query = channel.unary_unary(
                '/banking.Banking/Query',
                request_serializer=bank__pb2.BalanceRequest.SerializeToString,
                response_deserializer=bank__pb2.BalanceResponse.FromString,
                )
        self.ProcessID = channel.unary_unary(
                '/banking.Banking/ProcessID',
                request_serializer=bank__pb2.BranchID.SerializeToString,
                response_deserializer=bank__pb2.ProcessIDResponse.FromString,
                )
        self.Propagate_Deposit = channel.unary_unary(
                '/banking.Banking/Propagate_Deposit',
                request_serializer=bank__pb2.DepositRequest.SerializeToString,
                response_deserializer=bank__pb2.Status.FromString,
                )
        self.Propagate_Withdraw = channel.unary_unary(
                '/banking.Banking/Propagate_Withdraw',
                request_serializer=bank__pb2.WithdrawRequest.SerializeToString,
                response_deserializer=bank__pb2.Status.FromString,
                )


class BankingServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Propogate_Deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Propogate_Withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Query(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProcessID(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Propagate_Deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Propagate_Withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BankingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.Deposit,
                    request_deserializer=bank__pb2.DepositRequest.FromString,
                    response_serializer=bank__pb2.Status.SerializeToString,
            ),
            'Withdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.Withdraw,
                    request_deserializer=bank__pb2.WithdrawRequest.FromString,
                    response_serializer=bank__pb2.Status.SerializeToString,
            ),
            'Propogate_Deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.Propogate_Deposit,
                    request_deserializer=bank__pb2.DepositRequest.FromString,
                    response_serializer=bank__pb2.Status.SerializeToString,
            ),
            'Propogate_Withdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.Propogate_Withdraw,
                    request_deserializer=bank__pb2.WithdrawRequest.FromString,
                    response_serializer=bank__pb2.Status.SerializeToString,
            ),
            'Query': grpc.unary_unary_rpc_method_handler(
                    servicer.Query,
                    request_deserializer=bank__pb2.BalanceRequest.FromString,
                    response_serializer=bank__pb2.BalanceResponse.SerializeToString,
            ),
            'ProcessID': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessID,
                    request_deserializer=bank__pb2.BranchID.FromString,
                    response_serializer=bank__pb2.ProcessIDResponse.SerializeToString,
            ),
            'Propagate_Deposit': grpc.unary_unary_rpc_method_handler(
                    servicer.Propagate_Deposit,
                    request_deserializer=bank__pb2.DepositRequest.FromString,
                    response_serializer=bank__pb2.Status.SerializeToString,
            ),
            'Propagate_Withdraw': grpc.unary_unary_rpc_method_handler(
                    servicer.Propagate_Withdraw,
                    request_deserializer=bank__pb2.WithdrawRequest.FromString,
                    response_serializer=bank__pb2.Status.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'banking.Banking', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Banking(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/banking.Banking/Deposit',
            bank__pb2.DepositRequest.SerializeToString,
            bank__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Withdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/banking.Banking/Withdraw',
            bank__pb2.WithdrawRequest.SerializeToString,
            bank__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Propogate_Deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/banking.Banking/Propogate_Deposit',
            bank__pb2.DepositRequest.SerializeToString,
            bank__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Propogate_Withdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/banking.Banking/Propogate_Withdraw',
            bank__pb2.WithdrawRequest.SerializeToString,
            bank__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Query(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/banking.Banking/Query',
            bank__pb2.BalanceRequest.SerializeToString,
            bank__pb2.BalanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProcessID(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/banking.Banking/ProcessID',
            bank__pb2.BranchID.SerializeToString,
            bank__pb2.ProcessIDResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Propagate_Deposit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/banking.Banking/Propagate_Deposit',
            bank__pb2.DepositRequest.SerializeToString,
            bank__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Propagate_Withdraw(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/banking.Banking/Propagate_Withdraw',
            bank__pb2.WithdrawRequest.SerializeToString,
            bank__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
