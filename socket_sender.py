import socket
import sys

from io import BytesIO

from opendis.DataOutputStream import DataOutputStream
from opendis.dis7 import EntityStatePdu
from opendis.RangeCoordinates import GPS

HOST, PORT = "192.168.1.8", 502
data_in = " ".join(sys.argv[1:])

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send():
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
    send()
