import pyvisa

# rm = ResourceManager()
rm = pyvisa.ResourceManager()
print(rm.list_resources())
hp = rm.open_resource('GPIB0::3::INSTR')

# print(my_instrument.read())
ident_string = hp.query('*IDN?')
print(rm.list_resources)

# hp.read_termination = '\n'
# hp.write_termination = '\n'

# hp.write('*TST?')
# data = hp.read_raw()

# print(data)

# interval_in_ms = 500
# number_of_readings = 10
# hp.write("status:measurement:enable 512; *sre 1")
# hp.write("sample:count %d" % number_of_readings)
# hp.write("trigger:source bus")
# hp.write("trigger:delay %f" % (interval_in_ms / 1000.0))
# hp.write("trace:points %d" % number_of_readings)
# hp.write("trace:feed sense1; trace:feed:control next")

# hp.write("initiate")
# hp.assert_trigger()
# hp.wait_for_srq()

# print(hp.query('FETC:SCAL:VOLT[:DC]:ACDC?'))


# print(type(ident_string))
# print(f"<{ident_string}>")
# if ident_string != "HEWLETT-PACKARD,6632B,0,A.00.09\n":
#     raise IOError(f"Invalid IDENT string: {ident_string}")