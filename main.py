#!/usr/bin/env python3
"""Currently runs just the Modbus server command. The server will wait until a Modbus packet is received, then close.
When it closes, the return code indicates that the server is done and a DIS PDU packet is automatically sent using the
DIS PDU sender.

The current implementation automatically kills the Modbus receiver server, but could be changed to stay active after
processing the Modbus packet.

While main.py handles the Modbus receiver and DIS PDU sender, the DIS PDU reciever should be started separately in order
to see the packet output.

Order of Operations
1. Start dis_pdu_receiver.py
2. Start main.py
3. Run modbus_sender.py
4. Confirm that debug logs are generated in main.py window, then enter data for DIS PDU sender
5. Confirm that DIS PDU receiver output packet information.
6. Verify that main.py exited correctly.
7. The dis_pdu_receiver.py process will have to be killed manually via Ctl-C
"""
import socket

from dis_pdu_sender import send_dis_pdu
from modbus_receiver import run_modbus_server


HOST = "localhost"
PORT = 5020

if __name__ == "__main__":
    while run_modbus_server():
        pass
    else:
        send_dis_pdu()
