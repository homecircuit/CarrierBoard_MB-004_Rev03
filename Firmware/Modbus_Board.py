#!/usr/bin/env python3
import minimalmodbus
import serial
import time

instr = minimalmodbus.Instrument('/dev/ttyS0',1)
instr.serial.port='/dev/ttyS0'
instr.serial.baudrate = 9600
instr.serial.bytesize = 8
instr.serial.parity = serial.PARITY_NONE
instr.serial.stopbits = 1
instr.serial.timeout = 2
instr.mode = minimalmodbus.MODE_RTU
#instr.clear_buffers_before_each_transaction = True

instr.address = 5 

try:
    val = instr.read_registers(registeraddress=0, number_of_registers=10, functioncode=3)
    print(val)
except ValueError:
    print("ValueError")
except minimalmodbus.ModbusException:
    print("ModbusException")
except minimalmodbus.NoResponseError:
    print("NoResponseError")
except:
    pass
