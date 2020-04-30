import datetime
import time
from datetime import date

from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket, TTransport

from thriftDemo.service.hello import HelloService


class HelloServiceHandler:
    def ping(self, msg):
        result = str(datetime.time) + msg
        print("receive %s" % msg)
        return result


if __name__ == '__main__':
    handler = HelloServiceHandler()
    processor = HelloService.Processor(handler)
    transport = TSocket.TServerSocket("localhost", 12580)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(processor,transport,tfactory,pfactory)
    print("thrift server start !")
    server.serve()
