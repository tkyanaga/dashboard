import obd

obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.OBD() # auto-connects to USB or RF port

cmd = obd.commands.RPM # select an OBD command (sensor)

response = connection.query(cmd) # send the command, and parse the response

print(response.value) # returns unit-bearing values thanks to Pint

connection.close()