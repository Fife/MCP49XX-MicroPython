from MCP49XX import MCP

C_SELECT = 9 #Chip Select Pin. This goes low when we write data to the MCP49XX Bus

myMCP = MCP("MCP4901", C_SELECT) #Creation of an MCP object instance MCP(ChipName, ChipSelectPin)

myMCP.writeVolt(1.65) #Writing a voltage value to the MCP49XX

value = machine.ADC(26) #Ouput of MCP49XX is tied to input ADC(0) to get a test reading

reading = value.read_u16() #Read output of the MCPXX

print(reading)
