import obd

obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.Async("dev/ttyUSB0", baudrate="115200", protocol="3", fast=False) # manually set parameters

cmd = obd.commands.RPM # select an OBD command (sensor)

response = connection.query(cmd) # send the command, and parse the response

print(response.value) # returns unit-bearing values thanks to Pint

connection.close()
