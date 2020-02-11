#!/usr/bin/env python3
import socket

from dis_pdu_sender import send_dis_pdu
from modbus_receiver import run_modbus_server


HOST = "localhost"
PORT = 5020

run_modbus_server()

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen()
        conn, addr = sock.accept()
        if conn:
            print("Saw Modbus connection close, sending DIS PDU packet")
