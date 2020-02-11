#!/usr/bin/env python3
from dis_pdu_sender import send_dis_pdu
from modbus_receiver import run_modbus_server

# Capture Modbus packet
run_modbus_server()

# Generate DIS PDU packet
send_dis_pdu()
