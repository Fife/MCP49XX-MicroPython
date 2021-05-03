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

If everything is working correctly, a value near 32768 will print out on the terminal. Replacing "1.65" to "3.33"  in the writeVolt function should yield a value near 65536.

Note that this number may not be exact for a few reasons (It should be very close though):

1. If you are using a MCP4901, there are only 8 bits of signal resolution. This limits the precision of the output reading because the ADC input resolution is 12-bits, which get scaled up to a 16 bit result in micropython. Rounding errors across multiple scaling functions can happen.      
2. Since there is only 1 ADC onboard the pi Pico, but multiple channels, the ADC scans each pin regardless of whether or not the inpts are connected, and the noise on those unused pins will affect the reading accuracy slightly. To reduce this noise, connect the unused ADC pins on the pi Pico to ground. 
3. It is recommended by the MCP49XX manufacturer that bypass capacitor(s) are used across voltage supply (+, - rails). This is optional, but doing so reduces the noise on the DAC output pin. 
