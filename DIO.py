import PySimpleGUI as sg

DDRA = "00000000"
DDRB = "00000000"
DDRC = "00000000"
DDRD = "00000000"
my_ports = [DDRA, DDRB, DDRC, DDRD]
port_names = ['DDRA', 'DDRB', 'DDRC', 'DDRD']
data = [None] * 8


def write_file(_path):
    file1 = open(_path, "w+")
    file1.write("void DIO_Init()\n{\n\t")
    file1.write("DDRA = 0b" + my_ports[0])
    file1.write(";\n\t")
    file1.write("DDRB = 0b" + my_ports[1])
    file1.write(";\n\t")
    file1.write("DDRC = 0b" + my_ports[2])
    file1.write(";\n\t")
    file1.write("DDRD = 0b" + my_ports[3])
    file1.write(";\n}")
    file1.close()


def Set_Ports(bits_array, port):
    global my_ports, port_names
    for j in range(8):
        if port == port_names[j]:
            my_ports[j] = ''
            break
    for i in range(8):
        while 1:
            bits_array[i] = bits_array[i].lower()

            if bits_array[i] == "input":
                my_ports[j] = my_ports[j] + '0'
                break
            elif bits_array[i] == "output":
                my_ports[j] = my_ports[j] + '1'
                break
            else:
                print("error, please try again")



DIO_Choice_List_Column = [

    [sg.Text('DIO Initialization')],
    [sg.Text("Pick the PORT to be modified"),
     sg.Combo(values=["DDRA", "DDRB", "DDRC", "DDRD"], default_value="", size=(8, 1), key='_PORT_')],
    [sg.Text("BIT0 : "),
     sg.Combo(values=["INPUT", "OUTPUT"], default_value="", size=(8, 1), key='_BIT0_')],
    [sg.Text("BIT1 : "),
     sg.Combo(values=["INPUT", "OUTPUT"], default_value="", size=(8, 1), key='_BIT1_')],
    [sg.Text("BIT2 : "),
     sg.Combo(values=["INPUT", "OUTPUT"], default_value="", size=(8, 1), key='_BIT2_')],
    [sg.Text("BIT3 : "),
     sg.Combo(values=["INPUT", "OUTPUT"], default_value="", size=(8, 1), key='_BIT3_')],
    [sg.Text("BIT4 : "),
     sg.Combo(values=["INPUT", "OUTPUT"], default_value="", size=(8, 1), key='_BIT4_'),
     sg.Text("", key="port_saved", size=(20, 1), pad=(20, 0))],
    [sg.Text("BIT5 : "),
     sg.Combo(values=["INPUT", "OUTPUT"], default_value="", size=(8, 1), key='_BIT5_')],
    [sg.Text("BIT6 : "),
     sg.Combo(values=["INPUT", "OUTPUT"], default_value="", size=(8, 1), key='_BIT6_')],
    [sg.Text("BIT7 : "),
     sg.Combo(values=["INPUT", "OUTPUT"], default_value="", size=(8, 1), key='_BIT7_')],

    [sg.Button(button_text="Save Port", key="_SavePort_", enable_events=True, pad=(50, 0)),
     sg.Button(button_text="Generate Code", key="_generate_", enable_events=True)]

]

code_viewer_column = [
    [sg.Text("Your code will be generated here",size=(40, 11), key="-CODE-")],
]

