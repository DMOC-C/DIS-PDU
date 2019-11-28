import socket
import sys

from io import BytesIO

from opendis.DataOutputStream import DataOutputStream
from opendis.dis7 import EntityStatePdu
from opendis.RangeCoordinates import GPS

HOST, PORT = "localhost", 3001
data = " ".join(sys.argv[1:])

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

gps = GPS()


def send():
    pdu = EntityStatePdu()
    pdu.entityID.entityID = 42
    pdu.entityID.siteID = 17
    pdu.entityID.applicationID = 23
    pdu.entityAppearance = 14

    # monterey_location = gps.lla2ecef((36.6, -121.9, 1))  # lat lon altitude of Monterey, CA, USA.
    # pdu.entityLocation.x = monterey_location[0]
    # pdu.entityLocation.y = monterey_location[1]
    # pdu.entityLocation.z = monterey_location[2]

    memory_stream = BytesIO()
    output_stream = DataOutputStream(memory_stream)
    pdu.serialize(output_stream)
    data = memory_stream.getvalue()

    udp_socket.sendto(data, (HOST, PORT))
    print(f"Sent espdu. {len(data)} bytes")


if __name__ == "__main__":
    send()
