# MCP49XX-MicroPython
A library to use the MCP49XX series DAC with MicroPython and a pi Pico for embedded systems learning environments. 
This is essentially a wrapper class that abstracts some of the interfacing with the specific SPI implementation of the MCP family of chips.  This allows a user to simply import the library and write direct voltage values in a simple, understandable syntax. 

# Testing the library 
Use the following code to test the library on a pi Pico. Setup the circuit According to the following pins:

MCP4901 Example:

MCP4901 Pin 1 --> RPi Pico 3V3 OUT (Pin 37)

MCP4901 Pin 2 --> GPIO Pin 9

MCP4901 Pin 3 --> GPIO Pin 6

MCP4901 Pin 4 --> GPIO Pin 7

MCP4901 Pin 5 --> Ground

MCP4901 Pin 6 --> Rpi Pico 3v3 OUT (Pin 37)

MCP4901 Pin 7 --> Ground

MCP4901 Pin 8 --> Rpi Pico GPIO Pin 26 (ADC(0))

Run the code as seein in [example.py](https://github.com/GermanWaffles/MCP49XX-MicroPython/blob/main/example.py)

```python
from MCP49XX import MCP

C_SELECT = 9 #Chip Select Pin. This goes low when we write data to the MCP49XX Bus

myMCP = MCP("MCP4901", C_SELECT) #Creation of an MCP object instance MCP(ChipName, ChipSelectPin)

myMCP.writeVolt(1.65) #Writing a voltage value to the MCP49XX

value = machine.ADC(26) #Ouput of MCP49XX is tied to input ADC(0) to get a test reading

reading = value.read_u16() #Read output of the MCPXX

print(reading)
```
