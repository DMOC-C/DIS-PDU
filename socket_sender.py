import socket
import sys

from io import BytesIO

from opendis.DataOutputStream import DataOutputStream
from opendis.dis7 import EntityStatePdu
from opendis.RangeCoordinates import GPS

HOST, PORT = "localhost", 3001
data_in = " ".join(sys.argv[1:])

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_dis():
    pdu = EntityStatePdu()

    # Entity ID
    pdu.entityID.entityID = 45033
    pdu.entityID.siteID = 17
    pdu.entityID.applicationID = 2

    # Entity Type
    pdu.entityType.entityKind = 1
    pdu.entityType.domain = 1
    pdu.entityType.country = 222
    pdu.entityType.category = 16

    # Entity Appearance
    pdu.entityAppearance = 8388608

    memory_stream = BytesIO()
    output_stream = DataOutputStream(memory_stream)
    pdu.serialize(output_stream)
    data = memory_stream.getvalue()

    udp_socket.sendto(data, (HOST, PORT))
    print(f"Sent {len(data)} bytes")


if __name__ == "__main__":
    from pymodbus.client.sync import ModbusTcpClient as ModbusClient
    from time import sleep

    openplc_ip = input("What is the IP address of the OpenPLC device? ")
    target = openplc_ip
    client = ModbusClient(target)
    client.write_coil(2, True)
    sleep(2)
    send_dis()
