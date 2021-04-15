import PySimpleGUI as sg


##--------------------------- Functionality INTERFACE--------------------------------


def select_themode(x):
    file = open("spi.c", "w+")
    file.write("#include \"spi.h\" \n#include <avr/io.h> \n\n")

    if x == 'MASTER':
        file.write("void SPI_Master_init() \n{ \nSPCR=0x00; \n")
        file.write("//Work in Master Mode \n \n")
        file.write("SPCR|=(1<<MSTR);\nSPCR|=(1<<SPE);\n")

    elif x == 'SLAVE':
        file.write("void SPI_Slave_init() \n{ \nSPCR=0x00; \n")
        file.write("// work on slave mode \n\n")
        file.write("SPCR|=(1<<SPE);\n")
    file.close()


def select_spimodes(x, selected):
    file = open("spi.c", "a+")
    if x == 'MASTER' or x == 'SLAVE':
        if selected == 'MODE 0':
            file.write("// mode0 selected \n ")
        elif selected == 'MODE 1':
            file.write(" // mode1 selected \nSPCR|=(1<<CPHA);\n")
        elif selected == 'MODE 2':
            file.write("// mode2 selected \nSPCR|=(1<<CPOL);\n")
        else:
            file.write("// mode 3 selected \nSPCR|=(1<<CPHA);\nSPCR|=(1<<CPOL);\n")

    file.close()


def select_clockrate(selected2):
    file = open("spi.c", "a+")
    if selected2 == 'FOSC/2':
        file.write("// Prescalar = 2  \nSPSR|=(1<<SPI2X);\n}")
    elif selected2 == 'FOSC/4':
        file.write("// Prescalar = 4  \n}")
    elif selected2 == 'FOSC/8':
        file.write("// Prescalar = 8  \nSPSR|=(1<<SPI2X);\nSPCR|=(1<<SPR0);\n}")
    elif selected2 == 'FOSC/16':
        file.write("// Prescalar = 16  \nSPCR|=(1<<SPR0);\n}")
    elif selected2 == 'FOSC/32':
        file.write("// Prescalar = 32  \nSPSR|=(1<<SPI2X);\nSPCR|=(1<<SPR1);\n}")
    elif selected2 == 'FOSC/64':
        file.write("// Prescalar = 64  \nSPSR|=(1<<SPI2X);\nSPCR|=(1<<SPR0);\nSPCR|=(1<<SPR1);\n}")
    else:
        file.write("//Prescalar = 128 \nSPCR|=(1<<SPR0);\nSPCR|=(1<<SPR1);\n}")

    file.close()


##--------------------------- GUI INTERFACE--------------------------------

SPI_Choice_List_Column = [

    [sg.Text('SPI Initialization')],
    [sg.Text("Pick the parameters for SPI ")],
    [sg.Text("SPI Mode (MASTER/SLAVE)"),
     sg.Combo(values=["MASTER", "SLAVE"], default_value="", size=(8, 1), key='_MS_')],
    [sg.Text("SPI Channel MODE              "),
     sg.Combo(values=["MODE 0", "MODE 1", "MODE 2", "MODE 3"], default_value="", size=(8, 1), key='_MODE_')],
    [sg.Text("Clock Rate                           "),
     sg.Combo(values=["FOSC/2", "FOSC/4", "FOSC/8", "FOSC/16", "FOSC/32", "FOSC/64", "FOSC/128"], default_value="", size=(8, 1), key='_CLK_')],

    [sg.Button(button_text="Generate Code", key="_generate_SPI_", enable_events=True)]

]

code_viewer_column = [
    [sg.Multiline("Your code will be previewed here \nand a file will be created in your directory", font='any 10',
             justification="center", size=(70, 15), key="-CODE_SPI-")],
]