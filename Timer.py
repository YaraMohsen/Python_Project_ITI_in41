import PySimpleGUI as sg

##--------------------------- Functionality INTERFACE--------------------------------


# inzialize the duty cycle
def Duty_fun(D):

    file3 = open("Timer.c" ,"a+")
    file3.write("\n//Duty cycle\n")
    if   D == '25%':
        file3.write("// Duty cycle 25% \n")
        file3.write("OCR0=63;\n")
    elif D == '50%':
        file3.write("// Duty cycle 50% \n")
        file3.write("OCR0=127;\n")
    elif D == '75%':
        file3.write("// Duty cycle 75% \n")
        file3.write("OCR0=191;\n")
    elif D == '100%':
        file3.write("// Duty cycle 100% \n")
        file3.write("OCR0=255;\n")
    else:
        val = D
        print(val)
        file3.write("// Duty cycle manually % \n")
        file3.write("OCR0=")
        file3.write(str(val))
        file3.write(";\n")
    file3.close()


# display the chossen timer mode
def modes(x):

    file3 = open("Timer.c" ,"w+")
    file3.write("#incude \"Timer.h\" \n")
    file3.write("void Timer_Init (void) \n { \n")

    if x == 'Normal':
        file3.write("//Norml Mode  \n\n")
        file3.write("CLEAR_BIT(TCCR0,WGM00);\nCLEAR_BIT(TCCR0,WGM01);\n\n")
        file3.close()
        return 'Nor'


    elif x == 'Output_compare':
        file3.write("//Output Compare mode  \n\n")
        file3.write("CLEAR_BIT(TCCR0,WGM00);\nSET_BIT(TCCR0,WGM01);\n\n")
        file3.close()
        return 'OC'

    elif x == 'PWM_fast':
        file3.write("//PWM FAST Mode  \n\n")
        file3.write("SET_BIT(TCCR0,WGM00);\nSET_BIT(TCCR0,WGM01);\n\n")
        file3.close()
        return 'fast'

    elif x == 'PWM_phase':
        file3.write("//PWM Phase mode  \n\n")
        file3.write("CLEAR_BIT(TCCR0,WGM00);\nSET_BIT(TCCR0,WGM01);\n\n")
        file3.close()
        return 'phase'


# display the intr availability
def Intr(m, intr):

    file3 = open("Timer.c" ,"a+")

    if intr == 'Enable':
        file3.write("//Interrupt Enabled   \n\n")
        if m == 'Normal' :
            file3.write("SET_BIT(TIMSK,TOIE0); \n")

        else:
            file3.write("SET_BIT(TIMSK,OCIE0); \n")

    else:
        file3.write("//Interrupt Disabled   \n\n")

    file3.close()


# display the choosen prescalar
def Prescalar(Pre):

    file3 = open("Timer.c" ,"a+")
    if   Pre == '1':
        file3.write("\n\n//prescalar = 1  \n\n")
        file3.write("SET_BIT(TCCR0,CS00); \n")
    elif Pre == '8':
        file3.write("\n\n//prescalar = 8  \n\n")
        file3.write("SET_BIT(TCCR0,CS01); \n")
    elif Pre == '64':
        file3.write("\n\n//prescalar = 64  \n\n")
        file3.write("SET_BIT(TCCR0,CS00); \n")
        file3.write("SET_BIT(TCCR0,CS01); \n")
    elif Pre == '256':
        file3.write("\n\n//prescalar = 256  \n\n")
        file3.write("SET_BIT(TCCR0,CS02); \n")
    elif Pre == '1024':
        file3.write("\n\n//prescalar = 1024  \n\n")
        file3.write("SET_BIT(TCCR0,CS00); \n")
        file3.write("SET_BIT(TCCR0,CS02); \n")

    file3.close()


# display the choosen output on oc0
def oc0(mode, oc):

    file3 = open("Timer.c", "a+")
    if mode == 'Normal' or mode == 'Output_compare' or mode == 'PWM_fast' or mode == 'PWM_phase' :
        if oc == 'Toggle' :
            file3.write("\n\n//TOGGLE OC0  \n\n")
            file3.write("SET_BIT(TCCR0,COM00); \n")
            file3.write("CLEAR_BIT(TCCR0,COM01); \n")
        elif oc == 'Clear' :
            file3.write("\n\n//CLEAR OC0  \n\n")
            file3.write("SET_BIT(TCCR0,COM01); \n")
            file3.write("CLEAR_BIT(TCCR0,COM00); \n")
        elif oc == 'Set' :
            file3.write("\n\n//SET OC0  \n\n")
            file3.write("SET_BIT(TCCR0,COM01); \n")
            file3.write("SET_BIT(TCCR0,COM00); \n")
        elif oc == 'Non-Inverted (FAST)':
            file3.write("//Non-Inverted (FAST)\n")
            file3.write("SET_BIT(TCCR0,COM01);\nCLEAR_BIT(TCCR0,COM00);\n")
        elif oc == 'Inverted (FAST)':
            file3.write("//Inverted (FAST)\n")
            file3.write("SET_BIT(TCCR0,COM01);\nSET_BIT(TCCR0,COM00);\n")
        elif oc== 'CLEAR when Up Counting':
            file3.write("//CLEAR On Compare Match when Up Counting\n")
            file3.write("SET_BIT(TCCR0,COM01);\nCLEAR_BIT(TCCR0,COM00);\n")
        elif oc == 'SET when Up Counting':
            file3.write("//SET On Compare Match when Up Counting\n")
            file3.write("SET_BIT(TCCR0,COM01);\nSET_BIT(TCCR0,COM00);\n")
    file3.write(" \n  }")
    file3.close()

##--------------------------- GUI INTERFACE--------------------------------




Normal_layout = [

        [sg.Text("OC0 on Match     "),
         sg.Combo(values=['Toggle', 'Clear', 'Set'], default_value="", size=(8, 1), key='_optionsNor_')],
]

OC_layout = [

    [sg.Text("OC0 on Match     "),
     sg.Combo(values=['Toggle', 'Clear', 'Set'], default_value="", size=(8, 1), key='_optionsOC_')],
]


PWM_fast_layout = [

        [sg.Text("Duty cycle          "),
         sg.Combo(values=['25%', '50%', '75%', '100%'], default_value="", size=(8, 1), key='_DC_fast_')],

        [sg.Text("OC0 on Match     "),
         sg.Combo(values=['Non-Inverted (FAST)', 'Inverted (FAST)'], default_value="", key='_options_PWMF_')],
]


PWM_phase_layout = [

        [sg.Text("Duty cycle          "),
         sg.Combo(values=['25%', '50%', '75%', '100%'], default_value="", size=(8, 1), key='_DC_phase_')],

        [sg.Text("OC0 on Match     "),
         sg.Combo(values=['CLEAR when Up Counting', 'SET when Up Counting'], default_value="", key='_options_PWMP_')],
]

Timer_Choice_List_Column = [

    [sg.Text('Timer Initialization')],
    [sg.Text("Pick the parameters for Timer ")],
    [sg.Text("Timer Mode:   ")],
    [sg.Button('Normal',), sg.Button('Output_compare'), sg.Button('PWM_fast'), sg.Button('PWM_phase')],

    [sg.Text("Current mode:{}".format("normal"), key='_Tmode_',size=(30,1))],
    [sg.Text("Interrupt               "),
         sg.Combo(values=['Enable', 'Disable'], default_value="", size=(8, 1), key='_Interrupt_')],
        [sg.Text("Prescaler             "),
         sg.Combo(values=['1', '8', '64', '256', '1024'], default_value="", size=(8, 1), key='_Prescaler_')],

    [sg.Column(Normal_layout, key='-Normal-'),sg.Column(OC_layout,  visible=False, key='-Output_compare-'),
     sg.Column(PWM_fast_layout, visible=False, key='-PWM_fast-'), sg.Column(PWM_phase_layout, visible=False, key='-PWM_phase-')],



    [sg.Button(button_text="Generate Code", key="_generate_Timer_", enable_events=True)]

]

code_viewer_column = [
    [sg.Multiline("Your code will be previewed here \nand a file will be created in your directory", font='any 10',
                  justification="center",  size=(70, 15), key="-CODE_Timer-")],
]
