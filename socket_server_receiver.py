#!/usr/bin/env python3

import socketserver

from opendis.RangeCoordinates import GPS
from opendis.PduFactory import createPdu

gps = GPS()


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


if __name__ == "__main__":
    HOST, PORT = "localhost", 3001
    with socketserver.UDPServer((HOST, PORT), UDPServer) as server:
        print(f"Created UDP socket {PORT}")
        server.serve_forever()
