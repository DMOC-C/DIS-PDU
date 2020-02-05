#!/usr/bin/env python3
import logging
import socketserver

from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.server.sync import StartTcpServer

from opendis.PduFactory import createPdu


class UDPServer(socketserver.BaseRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        self.data = None
        self.lla = None
        self.location = None

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        self.recv(data)

    def recv(self, data):
        self.data = data
        a_pdu = createPdu(self.data)
        print(f"Received Pdu type {a_pdu.pduType}, {len(self.data)} bytes")

        if a_pdu.pduType == 1:
            print(f"PDU data: {bin(a_pdu.entityAppearance)}")


def run_modbus_server():
    FORMAT = ('%(asctime)-15s %(threadName)-15s'
              ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
    logging.basicConfig(format=FORMAT)
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    mb_host = "localhost"
    mb_port = 5020
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17] * 100),
        co=ModbusSequentialDataBlock(0, [17] * 100),
        hr=ModbusSequentialDataBlock(0, [17] * 100),
        ir=ModbusSequentialDataBlock(0, [17] * 100))
    context = ModbusServerContext(slaves=store, single=True)
    StartTcpServer(context, address=(mb_host, mb_port))


def run_dis_server():
    dis_host = "localhost"
    dis_port = 3001
    with socketserver.UDPServer((dis_host, dis_port), UDPServer) as server:
        print(f"Created UDP socket {dis_port}")
        server.serve_forever()


if __name__ == "__main__":
    run_dis_server()
    # run_modbus_server()

