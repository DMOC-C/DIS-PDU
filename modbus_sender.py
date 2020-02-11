#!/usr/bin/env python3
from pymodbus.client.sync import ModbusTcpClient as ModbusClient


def send_modbus():
    openplc_ip = input("What is the IP address of the OpenPLC device? ")
    if not openplc_ip:
        openplc_ip = "localhost"
    openplc_port = input("What is the port of the OpenPLC device? ")
    if not openplc_port:
        openplc_port = "5020"

    client = ModbusClient(openplc_ip, openplc_port)
    client.write_coil(2, True)
    print("Sent Modbus command")
    client.close()


if __name__ == "__main__":
    send_modbus()
