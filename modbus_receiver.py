#!/usr/bin/env python3
import logging

from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
from pymodbus.server.sync import StartTcpServer


def run_modbus_server(mb_host="localhost", mb_port=5020):
    FORMAT = ('%(asctime)-15s %(threadName)-15s'
              ' %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
    logging.basicConfig(format=FORMAT)
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [17] * 100),
        co=ModbusSequentialDataBlock(0, [17] * 100),
        hr=ModbusSequentialDataBlock(0, [17] * 100),
        ir=ModbusSequentialDataBlock(0, [17] * 100))
    context = ModbusServerContext(slaves=store, single=True)
    StartTcpServer(context, address=(mb_host, mb_port))


if __name__ == "__main__":
    run_modbus_server()
