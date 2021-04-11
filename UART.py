import tkinter as tk
from tkinter import ttk
import math

window = tk.Tk()
window.title("GUI UART Tx/Rx Interface")
window.focus_set()
frame_COMinf = tk.Frame(window)
frame_COMinf.grid(row = 1, column = 1)

#BudRate Function
def BUDRATE(budrate):
    if budrate in (1200,2400,4800,9600,19200,38400,57600,115200):
        ubrrl=int(((8000000)/(16*budrate))-1)
        return ubrrl
    else :
        ubrrl=int(((8000000)/(16*9600))-1)
        return ubrrl



#Stop Bit Function 
def StopBits(number_of_stop_bits):
    if number_of_stop_bits=="1":
        return "|(0<<USBS)"
    elif number_of_stop_bits=="2":
        return "|(1<<USBS)"

#No_of Data bits Functions    
def Data_Bits(data_bits):
    if data_bits=="5":
        return "|(0<<UCSZ0)"
    elif data_bits=="6":
        return "|(1<<UCSZ0)"
    elif data_bits=="7":
        return "|(2<<UCSZ0)"
    elif data_bits=="8":
        return "|(3<<UCSZ0)"

#Parity Function 
def Parit_Bit(parity_bit):
    
    if parity_bit=="NONE":
        return "|(0<<UPM0)|(0<<UPM1);"
    elif parity_bit=="ODD":
        return "|(1<<UPM0)|(1<<UPM1);"
    elif parity_bit=="EVEN":
        return "|(0<<UPM0)|(1<<UPM1);"



#File generation
def Generate():
    
    strParity = Parity.get()

    strStopbits = Stopbits.get()
    strDatabits = Databits.get()
    strBaudrate=  Baudrate.get()
    
    file=open("UART.c","w+")
    
    #includes
    file.write('#include <avr/io.h>\n#include "STD_type.h"\n#include "BIT_MATH.h"\n\nvoid uart_init()\n{\n')
    #Init_func_Budrate
    file.write('\n\t/* Set baud rate */\n\tUBRRL=%d;\n\n\t/* Enable receiver and transmitter */\n\tUCSRB = (1<<RXEN)|(1<<TXEN);\n\n\t/* Set frame format: 8data, 2stop bit */\n\tUCSRC = (1<<URSEL)%s' %(BUDRATE(strBaudrate),StopBits(strStopbits)))
    #Init_func_Parity & Dats
    file.write('%s%s\n}\n\n' %(Data_Bits(strDatabits),Parit_Bit(strParity)))
    #Uart Send
    file.write('void transmit_uart(uint8 data)\n{\n\n\t/* Wait for empty transmit buffer */\n\twhile (!(UCSRA & (1<<UDRE)));\n\n\t/* Put data into buffer, sends the data */\n\tUDR=data;\n}\n\n')
    #Uart Recieve
    file.write('uint8 receive_uart()\n{\n\n\t/* Wait for data to be received */\n\twhile ( !(UCSRA & (1<<RXC)));\n\n\t/* Get and return received data from buffer */\n\treturn UDR;\n}\n')
    file.close()



        
        

        
##For Baudrate
labelBaudrate = tk.Label(frame_COMinf,text="Baudrate: ")
Baudrate = tk.IntVar(value = 9600)
ertryBaudrate = tk.Entry(frame_COMinf, textvariable = Baudrate)
labelBaudrate.grid(row = 1, column = 1, padx = 5, pady = 3)
ertryBaudrate.grid(row = 1, column = 2, padx = 5, pady = 3)
        
##For Parity
labelParity = tk.Label(frame_COMinf,text="Parity: ")
Parity = tk.StringVar(value="NONE")
comboParity = ttk.Combobox(frame_COMinf, width = 17, textvariable=Parity)
comboParity["values"] = ("NONE","ODD","EVEN")
comboParity["state"] = "readonly"
labelParity.grid(row = 1, column = 3, padx = 5, pady = 3)
comboParity.grid(row = 1, column = 4, padx = 5, pady = 3)
        
##For StopBits
labelStopbits = tk.Label(frame_COMinf,text="Stopbits: ")
Stopbits = tk.StringVar(value ="1")
comboStopbits = ttk.Combobox(frame_COMinf, width = 17, textvariable=Stopbits)
comboStopbits["values"] = ("1","2")
comboStopbits["state"] = "readonly"
labelStopbits.grid(row = 2, column = 1, padx = 5, pady = 3)
comboStopbits.grid(row = 2, column = 2, padx = 5, pady = 3)
        
##For Databits
labelDatabits = tk.Label(frame_COMinf,text="Databits: ")
Databits = tk.StringVar(value ="5")
comboDatabits = ttk.Combobox(frame_COMinf, width = 17, textvariable=Databits)
comboDatabits["values"] = ("5","6","7","8")
comboDatabits["state"] = "readonly"
labelDatabits.grid(row = 2, column = 3, padx = 5, pady = 3)
comboDatabits.grid(row = 2, column = 4, padx = 5, pady = 3)



buttonSS = tk.Button(frame_COMinf, text = "Generate", width=8,command = Generate)
buttonSS.grid(row = 3, column = 4, padx = 5, pady = 3, sticky = tk.E)

window.mainloop()