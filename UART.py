import PySimpleGUI as sg


##--------------------------- Functionality INTERFACE--------------------------------


# BudRate Function
def BUDRATE(baudrate):
    if baudrate in (1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200):
        ubrrl = int(((8000000) / (16 * baudrate)) - 1)
        return ubrrl
    else:
        ubrrl = int(((8000000) / (16 * 9600)) - 1)
        return ubrrl


# Stop Bit Function
def StopBits(number_of_stop_bits):
    if number_of_stop_bits == "1":
        return "|(0<<USBS)"
    elif number_of_stop_bits == "2":
        return "|(1<<USBS)"


# No_of Data bits Functions
def Data_Bits(data_bits):
    if data_bits == "5":
        return "|(0<<UCSZ0)"
    elif data_bits == "6":
        return "|(1<<UCSZ0)"
    elif data_bits == "7":
        return "|(2<<UCSZ0)"
    elif data_bits == "8":
        return "|(3<<UCSZ0)"


# Parity Function
def Parit_Bit(parity_bit):
    if parity_bit == "NONE":
        return "|(0<<UPM0)|(0<<UPM1);"
    elif parity_bit == "ODD":
        return "|(1<<UPM0)|(1<<UPM1);"
    elif parity_bit == "EVEN":
        return "|(0<<UPM0)|(1<<UPM1);"


def UART_write_file(baud_rate, parity, stop, data):
    file = open("UART.c", "w+")

    # includes
    file.write('#include <avr/io.h>\n#include "STD_type.h"\n#include "BIT_MATH.h"\n\nvoid uart_init()\n{\n')

    # Init_func_Budrate
    file.write(
        '\n\t/* Set baud rate */\n\tUBRRL=%d;\n\n\t/* Enable receiver and transmitter */\n\tUCSRB = (1<<RXEN)|(1<<TXEN);\n\n\t'
        '/* Set frame format: 8data, 2stop bit */\n\tUCSRC = (1<<URSEL)%s' % (baud_rate, stop))

    # Init_func_Parity & Dats
    file.write('%s%s\n}\n\n' % (data, parity))

    # Uart Send
    file.write(
        'void transmit_uart(uint8 data)\n{\n\n\t/* Wait for empty transmit buffer */\n\twhile (!(UCSRA & (1<<UDRE)));\n\n\t'
        '/* Put data into buffer, sends the data */\n\tUDR=data;\n}\n\n')

    # Uart Recieve
    file.write('uint8 receive_uart()\n{\n\n\t/* Wait for data to be received */\n\twhile ( !(UCSRA & (1<<RXC)));\n\n\t'
               '/* Get and return received data from buffer */\n\treturn UDR;\n}\n')

    file.close()


##--------------------------- GUI INTERFACE--------------------------------

UART_Choice_List_Column = [

    [sg.Text('UART Initialization')],
    [sg.Text("Pick the parameters for UART ")],
    [sg.Text("Baud rate   "),
     sg.Input(default_text ="", size=(10, 1), key='_BAUDRATE_')],
    [sg.Text("Parity bits  "),
     sg.Combo(values=["NONE", "ODD", "EVEN"], default_value="", size=(8, 1), key='_Parity_')],
    [sg.Text("Stop bits    "),
     sg.Combo(values=["1", "2"], default_value="", size=(8, 1), key='_Stop_')],
    [sg.Text("Data bits    "),
     sg.Combo(values=["5", "6", "7", "8"], default_value="", size=(8, 1), key='_Data_')],

    [sg.Button(button_text="Generate Code", key="_generate_UART_", enable_events=True)]

]

code_viewer_column = [
    [sg.Multiline("Your code will be previewed here \nand a file will be created in your directory", font='any 10',
                  justification="center", size=(70, 15), key="-CODE_UART-")],
]