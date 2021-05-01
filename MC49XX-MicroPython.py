#Dependacies: 
    #machine
    #ubitString
    #micropython-types
    #micropython-copy
    
# A Class that is a "digital instance" of the MCP49XX DAC. This is essentially 
# a wrapper class that abstracts some of the interfacing away from the user so that
# people new to microcontrollers can get an easily available and well-documented DAC
# and communicate with it using python file/REPL.

#Setup Information:
    #Number of don't care bits (Resolution of data bits)
        #12-bit, 10-bit, 8-bit
    #Interface Pins (outputs of micro controller): 
        #SCK- Serial Clock - Default Pin: 6
        #CS- Chip Select - Default Pin: N/A (Must be defined)
        #SDI- Serial Data Input - Default Pin: N/A (Must be defined)
        #LDAC Latch DAC Input - Default Pin: N/A(Must be defined) 
    #VRef - 3.3V-5V (3.3V Default)

#Controls/Methods: 
    #Write to the DAC 
    #Buffered/Unbuffered Mode
    #Output Gain Selecetion (x1, x2)
    #Shutdown Control

#Desired interface example:

#myObg = MCP() - Minimal Instantiation with all defaults
#myObj = MCP(BITS, CS_PIN, SDI_PIN, LDAC, VREF, GAIN, BUFFER_MODE)  - Instantiates instance of chip with all params in constructor
#myObj.write(1.26) - Wrting values
#myObj.setGain(2) - Setting Gain
#myObj.setBuffer(True)- Setting Buffer
#myObj.shutDown(True)- Shutdown Control
#myObj.setLDAC(PIN)- Set Latch DAC/Any other interface params

#Implementation TODOS: 
    #Setup Methods
        #SPI superconstructor 
        #Interface pin instantiation
        #Vref 
    #Control Methods 
        #Write to the DAC 
        #Buffered/Unbuffered Mode
        #Output Gain Selecetion (x1, x2)
        #Shutdown Control

#Test load of dependancies
from machine import SPI
from ubitstring import Bits
spi = SPI(0)
print("Hello")


