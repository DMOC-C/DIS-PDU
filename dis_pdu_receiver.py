#!/usr/bin/env python3
import socketserver

from opendis.PduFactory import createPdu


class UDPServer(socketserver.BaseRequestHandler):
    """Create a UDP server for DIS PDU connections"""
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        self.data = None
        self.lla = None
        self.location = None

    def handle(self):
        """Separate the socket connection from the data payload of the packet"""
        data = self.request[0].strip()
        socket = self.request[1]
        self.recv(data)

    def recv(self, data):
        """Reports to the user that a particular PDU type was received, its size, and what the data payload is"""
        self.data = data
        a_pdu = createPdu(self.data)
        print(f"Received PDU type {a_pdu.pduType}, {len(self.data)} bytes")

        if a_pdu.pduType == 1:
            print(f"PDU data: {bin(a_pdu.entityAppearance)}")


def run_dis_server(dis_host="localhost", dis_port=3001):
    """Run UDP server to capture DIS PDU packets.

    This is a very basic server that simply reports that a socket is created, then runs until manually quit.
    """
    with socketserver.UDPServer((dis_host, dis_port), UDPServer) as server:
        print(f"Created UDP socket {dis_port}")
        server.serve_forever()  # Could set it up to timeout


if __name__ == "__main__":
    run_dis_server()

