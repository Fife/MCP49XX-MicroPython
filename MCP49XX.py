# A Class that is a "digital instance" of the MCP49XX DAC. This is essentially 
# a wrapper class that abstracts some of the interfacing away from the user so that
# people new to microcontrollers can get an easily available and well-documented DAC
# and communicate with it using python file/REPL.

#Setup Information:
    #Number of don't care bits (Resolution of data bits)
        #12-bit, 10-bit, 8-bit
    #Interface Pins (outputs of micro controller): 
        #SCK- Serial Clock - Pin 6
        #CS- Chip Select - Default Pin: N/A (Must be defined)
        #SDI- Serial Data Input - Pin 4
        #LDAC Latch DAC Input - Default Pin: N/A(Must be defined) 
    #VRef - 3.3V-5V (3.3V Default)

#Implementation TODOS: 
    #VRef Gaurds so users can't change vRef beyond hardware specs 
    #Write value method so user can write direct interger values

#Desired interface example:

#myObj = MCP("MCP4901", 9)
#myObj.write(1.26) - Wrting values
#myObj.setGainFlag(True) - Setting Gain
#myObj.setBufferFlag(True)- Setting Buffer
#myObj.shutdown()- Shutdown Control
#myObj.shutdown()- Shutdown Control
#myObj.setLDAC(PIN)- Set Latch DAC/Any other interface params


from machine import SoftSPI, ADC, Pin

class MCP():
    def __init__(self, name, csPin):
        if (name == "MCP4901"):       
            self.spiInstance = SoftSPI(baudrate=1000000, sck=Pin(6), mosi=Pin(7), miso=Pin(4))
            self.dataBitSize = 8
            self.gain = True
            self.vRef = 3.3
            self.bufferMode = True
            self.isOn = True
            self.chipSelectPin = Pin(csPin, Pin.OUT, Pin.PULL_UP)
            
        elif (name == "MCP4911"):
            self.spiInstance = SoftSPI(baudrate=1000000, sck=Pin(6), mosi=Pin(7), miso=Pin(4))
            self.dataBitSize = 10
            self.gain = True
            self.vRef = 3.33
            self.bufferMode = True
            self.isOn = True
            self.chipSelectPin = Pin(csPin, Pin.OUT, Pin.PULL_UP)
            
        elif (name == "MCP4921"):
            self.spiInstance = SoftSPI(baudrate=1000000, sck=Pin(6), mosi=Pin(7), miso=Pin(4))
            self.dataBitSize = 12
            self.gain = True
            self.vRef = 3.33
            self.bufferMode = True
            self.isOn = True
            self.chipSelectPin = Pin(csPin, Pin.OUT, Pin.PULL_UP)
            
    def __genFrame(self, value):
        tempVal = self.bufferMode*2**14+self.gain*2**13+self.isOn*2**12+(value<<(12-self.dataBitSize))
        return tempVal.to_bytes(2, 'big')
    
    def __voltToValue(self,volt):
        if(volt>self.vRef) : volt = self.vRef
        value = round(volt*(2**self.dataBitSize) /self.vRef)
        if (value == 2**self.dataBitSize): value = value -1
        return value
    
    def writeVolt(self, volt):
        value = self.__voltToValue(volt)
        frame = self.__genFrame(value)
        self.chipSelectPin.low()
        self.spiInstance.write(frame)
        self.chipSelectPin.high()
        #print(frame) #Debug
    
    def shutdown(self):
        self.isOn = False
        
    def restart(self):
        self.isOn = True
        
    def setGainFlag(self, flag):
        self.gain = flag
    
    def setBufferMode(self, flag):
        self.bufferMode = flag
