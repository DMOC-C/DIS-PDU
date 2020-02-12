#!/usr/bin/env python3
import logging

from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.server.sync import StartTcpServer, ModbusTcpServer

from dis_pdu_sender import send_dis_pdu


def run_modbus_server(mb_host="localhost", mb_port=5020):
    log_format = ('%(asctime)-15s %(threadName)-15s'
                  ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
    logging.basicConfig(format=log_format)
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17] * 100),
        co=ModbusSequentialDataBlock(0, [17] * 100),
        hr=ModbusSequentialDataBlock(0, [17] * 100),
        ir=ModbusSequentialDataBlock(0, [17] * 100))
    context = ModbusServerContext(slaves=store, single=True)
    print("Starting Modbus server")
    # StartTcpServer(context, address=(mb_host, mb_port))
    server = ModbusTcpServer(context, address=(mb_host, mb_port))
    while server.handle_request():  # Wait for Modbus packet
        pass
    else:  # As soon as Modbus packet received and processed, kill Modbus server and exit
        return 0


if __name__ == "__main__":
    run_modbus_server()
