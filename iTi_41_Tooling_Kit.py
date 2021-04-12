import PySimpleGUI as sg
import DIO

"""
    A python tool for making embedded software engineers' life easier.

    This tool allows you to generate your peripherals code dynamically, so you would not waste time 
    on looking things up in data sheets.
    
    This tool contain 4 peripherals so far which are ( DIO, Timers, UART, SPI), we plan to add more
    but maybe in future releases.

"""

# ----------- Create the main menu and 4 layouts for each peripheral -----------
MainMenu_layout = [[sg.Text('Pick the peripheral you want to generate')]]

DIO_layout = [
    [
        sg.Column(DIO.DIO_Choice_List_Column),
        sg.VSeperator(),
        sg.Column(DIO.code_viewer_column)
    ]
]


Timer_layout = [[sg.Text('This is layout 2')],
                [sg.Input(key='-IN-')],
                [sg.Input(key='-IN2-')]]

UART_layout = [[sg.Text('This is layout 3 - It is all Radio Buttons')],
               *[[sg.R(f'Radio {i}', 1)] for i in range(8)]]

SPI_layout = [[sg.Text('This is layout 3 - It is all Radio Buttons')],
              *[[sg.R(f'Radio {i}', 1)] for i in range(8)]]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(MainMenu_layout, key='-MainMenuTab-'), sg.Column(DIO_layout, visible=False, key='-DIOTab-'),
           sg.Column(Timer_layout, visible=False, key='-TimerTab-'), sg.Column(UART_layout, visible=False, key='-UARTTab-'),
           sg.Column(SPI_layout, visible=False, key='-SPITab-')],
          [sg.Button('DIO',), sg.Button('Timer'), sg.Button('UART'), sg.Button('SPI')]]

window = sg.Window('iTi-41 tooling kit', layout)

layout = 'MainMenu'  # The currently visible layout
while True:
    event, values = window.read(timeout=700)
    print(event, values)
    if event in (None, 'Exit'):
        break
    elif event in ['DIO', 'Timer', 'UART', 'SPI']:
        window[f'-{layout}Tab-'].update(visible=False)
        layout = event
        window[f'-{layout}Tab-'].update(visible=True)


    ## DIO EVENTS AND BUTTONS ##

    if event == "_SavePort_":
        bits = [values["_BIT0_"], values["_BIT1_"], values["_BIT2_"], values["_BIT3_"], values["_BIT4_"],
                values["_BIT5_"], values["_BIT6_"], values["_BIT7_"]]

        DIO.Set_Ports(bits, values["_PORT_"])
        window['port_saved'].update(value="PORT SAVED")

    if event == "_generate_":
        path = "D:/iti/tooling_python/DIO_Init.c"
        DIO.write_file(path)
        file = open(path, "r")
        data = file.read()
        print(data)
        window['-CODE-'].update(value=data)

    if event == '__TIMEOUT__':
        window['port_saved'].update(value="")
window.close()
