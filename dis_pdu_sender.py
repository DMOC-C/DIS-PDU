import socket
import sys
from io import BytesIO

from opendis.DataOutputStream import DataOutputStream
from opendis.dis7 import EntityStatePdu

data_in = " ".join(sys.argv[1:])

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_dis(host, port):
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

    udp_socket.sendto(data, (host, port))
    print(f"Sent {len(data)} DIS PDU bytes")


def send_dis_pdu():
    dis_ip = input("What is the IP address of the DIS PDU receiver? ")
    if not dis_ip:
        dis_ip = "localhost"
    dis_port = input("What is the port of the DIS PDU receiver? ")
    if not dis_port:
        dis_port = 3001
    send_dis(dis_ip, dis_port)


if __name__ == "__main__":
    send_dis_pdu()
