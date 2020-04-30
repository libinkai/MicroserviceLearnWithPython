from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport

from thriftDemo.service.hello import HelloService

if __name__ == '__main__':
    server = TSocket.TSocket("localhost", 12580)
    transport = TTransport.TBufferedTransport(server)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = HelloService.Client(protocol)
    transport.open()
    pong = client.ping("hello, world!")
    print("pong %s" % pong)
    transport.close()
