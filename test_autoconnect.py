import obd

obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.OBD() # auto-connects to USB or RF port

cmd = obd.commands.ODOMETER # select an OBD command (sensor)
print(obd.supports(cmd))

response = connection.query(cmd, force=True) # send the command, and parse the response
print(response.value) # returns unit-bearing values thanks to Pint

connection.close()