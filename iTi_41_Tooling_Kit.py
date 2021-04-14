import PySimpleGUI as sg
import DIO
import SPI
import UART
import Timer

"""
    a python tool for making embedded software engineers' life easier.

    This tool allows you to generate your peripherals code dynamically, so you would not waste time 
    on looking things up in data sheets.
    
    This tool contain 4 peripherals so far which are ( DIO, Timers, UART, SPI), we plan to add more
    but maybe in future releases.

"""

# ----------- Create the main menu and 4 layouts for each peripheral -----------
MainMenu_layout = [
        [sg.Image(filename="iti.png", pad=(65, 0))],
        [sg.Text('Pick the peripheral you want to generate', font='any 12')],
]

DIO_layout = [
    [
        sg.Column(DIO.DIO_Choice_List_Column),
        sg.VSeperator(),
        sg.Column(DIO.code_viewer_column)
    ]
]


Timer_layout = [
    [
        sg.Column(Timer.Timer_Choice_List_Column),
        sg.VSeperator(),
        sg.Column(Timer.code_viewer_column)
    ]
]

UART_layout = [
    [
        sg.Column(UART.UART_Choice_List_Column),
        sg.VSeperator(),
        sg.Column(UART.code_viewer_column)
    ]
]

SPI_layout = [
    [
        sg.Column(SPI.SPI_Choice_List_Column),
        sg.VSeperator(),
        sg.Column(SPI.code_viewer_column)
    ]
]

# ----------- Create actual layout using Columns and a row of Buttons
layout = [[sg.Column(MainMenu_layout, key='-MainMenuTab-'), sg.Column(DIO_layout, visible=False, key='-DIOTab-'),
           sg.Column(Timer_layout, visible=False, key='-TimerTab-'), sg.Column(UART_layout, visible=False, key='-UARTTab-'),
           sg.Column(SPI_layout, visible=False, key='-SPITab-')],
          [sg.Button('DIO', size=(6, 1), pad=(10, 0)), sg.Button('Timer', size=(6, 1)), sg.Button('UART', size=(6, 1)),
           sg.Button('SPI', size=(6, 1))]]

window = sg.Window('iTi-41 tooling kit', layout)

layout = 'MainMenu'  # The currently visible layout
Timer_mode_layout = 'Normal'
while True:
    event, values = window.read(timeout=700)
    #print(event, values)

    if event in (None, 'Exit'):
        break


    if event in ['DIO', 'Timer', 'UART', 'SPI']:
        window[f'-{layout}Tab-'].update(visible=False)
        layout = event
        window[f'-{layout}Tab-'].update(visible=True)
        window.move(250, 227)

    elif event in ['Normal', 'Output_compare', 'PWM_fast', 'PWM_phase']:
        window[f'-{Timer_mode_layout}-'].update(visible=False)
        Timer_mode_layout = event
        print(Timer_mode_layout)
        window[f'-{Timer_mode_layout}-'].update(visible=True)
        window['_Tmode_'].update(value="Current mode: {}".format(Timer_mode_layout))

    ## DIO EVENTS AND BUTTONS ##

    if event == "_SavePort_":
        bits = [values["_BIT0_"], values["_BIT1_"], values["_BIT2_"], values["_BIT3_"], values["_BIT4_"],
                values["_BIT5_"], values["_BIT6_"], values["_BIT7_"]]

        DIO.Set_Ports(bits, values["_PORT_"])
        window['port_saved'].update(value="PORT SAVED")

    if event == "_generate_DIO_":
        DIO.write_file()
        file = open("DIO_Init.c", "r")
        data = file.read()
        window['-CODE_DIO-'].update(value=data, justification="left")

    if event == "_generate_SPI_":
        SPI.select_themode(values["_MS_"])
        SPI.select_spimodes(values["_MODE_"], values["_MS_"])
        SPI.select_clockrate(values["_CLK_"])

        file = open("spi.c", "r")
        data = file.read()
        window['-CODE_SPI-'].update(value=data, justification="left")

    if event == "_generate_UART_":
        BR = UART.BUDRATE(int(values["_BAUDRATE_"]))
        PARITY = UART.Parit_Bit(values["_Parity_"])
        STOP = UART.StopBits(values["_Stop_"])
        DATA = UART.Data_Bits(values["_Data_"])

        UART.UART_write_file(BR, PARITY, STOP, DATA)
        file = open("UART.c", "r")
        data = file.read()
        window['-CODE_UART-'].update(value=data, justification="left")

    if event == "_generate_Timer_":
        ret = Timer.modes(Timer_mode_layout)

        Timer.Intr(Timer_mode_layout, values["_Interrupt_"])
        Timer.Prescalar(values["_Prescaler_"])

        if ret == 'Nor':
            Timer.oc0(Timer_mode_layout, values["_optionsNor_"])
        if ret == 'OC':
            Timer.oc0(Timer_mode_layout, values["_optionsOC_"])
        if ret == 'fast':
            Timer.Duty_fun(values["_DC_fast_"])
            Timer.oc0(Timer_mode_layout, values["_options_PWMF_"])
        if ret == 'phase':
            Timer.oc0(Timer_mode_layout, values["_options_PWMP_"])
            Timer.Duty_fun(values["_DC_phase_"])

        file = open("Timer.c", "r")
        data = file.read()
        window['-CODE_Timer-'].update(value=data, justification="left")

    if event == '__TIMEOUT__':
        window['port_saved'].update(value="")

window.close()
