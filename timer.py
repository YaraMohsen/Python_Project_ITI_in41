
import tkinter as tk
import re

#generate the output init.c file
def GenerateCode():
    modes()
    Intr()
    Prescalar()
    oc0()

 #To determine the modes on OC0 depend on the mode of the timer
def ManageModeOptions(*args):
    mode = options.get()
    
    if mode == 'PWM_FAST' or mode == 'PWM_Phase':
        DutyInput.grid(row=20,column=1)
        DutyInput.insert(tk.END, "Enter your valu here : ")
       
        om =tk.OptionMenu(Timer_Window, Duty, *Duty_cycle.values())
        om.grid(row=20,column=60)
        
    if   mode == 'Normal' :
            oc0_pin_dict={1:'Toggle', 2: 'Clear',3:'Set'}
    elif mode == 'Output Compare' :
            oc0_pin_dict={1:'Toggle', 2: 'Clear',3:'Set'}
    elif mode == 'PWM_FAST' :
            oc0_pin_dict={1:'Non-Inverted (FAST)', 2: 'Inverted (FAST)'}
    elif mode == 'PWM_Phase' :
            oc0_pin_dict={1:'CLEAR when Up Counting', 2: 'SET when Up Counting'}
   
    om4 = tk.OptionMenu(Timer_Window, options4, *oc0_pin_dict.values())
    om4.grid(row=240,column=60)




Timer_Window = tk.Tk()               #create new window
Timer_Window.geometry("500x200")     # Size of the window  
Timer_Window.title("Timer Drivers")  # title 
 
 
# create the dictionary of all menu options
Modes_dict       = {1: 'Normal', 2: 'Output Compare', 3: 'PWM_FAST',4:'PWM_Phase'}  #mode options
INTR_enable_dict = {1:'Enable', 2: 'Disable'}                                       #intr options
PreScalar_dict   = {1:'1', 2: '8',3: '64',4: '256',5: '1024'}                       #prescalar options
oc0_pin_dict     = {1: 'option'}                                                    #when oc0 appear 
Duty_cycle       = {1:'25%',2:'50%',3:'75%',4:'100%',5:'Other'}                     #Duty cycle options
 
options     = tk.StringVar(Timer_Window) 
options2    = tk.StringVar(Timer_Window) 
options3    = tk.StringVar(Timer_Window) 
options4    = tk.StringVar(Timer_Window) 
PWM_options = tk.StringVar(Timer_Window) 
Duty        = tk.StringVar(Timer_Window)


#default values of each OptionMenu 
options.set('Modes')
options2.set('E OR D') 
options3.set('PreScalar options') 
options4.set('options') 
PWM_options.set('PWM_pin_mode') 
Duty.set('Duty Cycle') 
 
 
#text create 
DutyInput = tk.Text(Timer_Window, height=1, width=30) 

#GUI of timer mode(text & option menu)
T1 = tk.Text(Timer_Window, height=1, width=30) 
T1.grid(row=2,column=1) 
T1.insert(tk.END, "choose The Mode:\n") 
 
menu1 = tk.OptionMenu(Timer_Window, options, *Modes_dict.values(),command=ManageModeOptions) 
menu1.grid(row=2,column=60) 
 
 
#GUI of intr (text & option menu)
T2 = tk.Text(Timer_Window, height=1, width=30) 
T2.grid(row=60,column=1) 
T2.insert(tk.END, "Interrupt :\n") 
 
menu2 = tk.OptionMenu(Timer_Window, options2, *INTR_enable_dict.values()) 
menu2.grid(row=60,column=60) 
 
#GUI of prescalar(text & option menu)
T3 = tk.Text(Timer_Window, height=1, width=30) 
T3.grid(row=120,column=1) 
T3.insert(tk.END, "choose The Prescalar :\n") 
 
menu3 = tk.OptionMenu(Timer_Window, options3, *PreScalar_dict.values()) 
menu3.grid(row=120,column=60) 
 
#GUI of oc0text & option menu)
T4 = tk.Text(Timer_Window, height=1, width=30) 
T4.grid(row=240,column=1) 
T4.insert(tk.END, "OC0 On Match: :\n") 
 
 
menu4 = tk.OptionMenu(Timer_Window, options4, *oc0_pin_dict.values()) 
menu4.grid(row=240,column=60) 

#GUI of generate button
B = tk.Button(Timer_Window, text ="Generate",command=GenerateCode) 
B.grid(row=300 , column= 120) 
 
 
#user enter the duty cycle out of our range
def getTextInput(): 
    result = DutyInput.get(1.23, tk.END+"-1c") 
    result = int(result) 
    duty   = (result*255)/100 
    return (int(duty)) 

#inzialize the duty cycle
def Duty_fun(*args): 
    D = Duty.get() 
    file3 = open("Init.c","a+") 
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
    elif D == 'Other': 
        val=getTextInput() 
        print(val) 
        file3.write("// Duty cycle manually % \n") 
        file3.write("OCR0=") 
        file3.write(str(val)) 
        file3.write(";\n") 
    file3.close() 
 
 
 
#display the chossen timer mode
def modes(*args):   
    x = options.get() 
     
    file3 = open("Init.c","w+") 
    file3.write("#incude \"Timer.h\" \n") 
    file3.write("void Timer_Init (void) \n { \n") 
 
    if   x == 'Normal' : 
        file3.write("//Norml Mode  \n\n") 
        file3.write("CLEAR_BIT(TCCR0,WGM00);\nCLEAR_BIT(TCCR0,WGM01);\n\n") 
        file3.close() 
         
 
    elif x == 'Output Compare' : 
        file3.write("//Output Compare mode  \n\n") 
        file3.write("CLEAR_BIT(TCCR0,WGM00);\nSET_BIT(TCCR0,WGM01);\n\n") 
        file3.close() 
         
    elif x == 'PWM_FAST' : 
        file3.write("//PWM FAST Mode  \n\n") 
        file3.write("SET_BIT(TCCR0,WGM00);\nSET_BIT(TCCR0,WGM01);\n\n") 
        file3.close() 
        Duty_fun() 
 
    elif x == 'PWM_Phase' : 
        file3.write("//PWM Phase mode  \n\n") 
        file3.write("CLEAR_BIT(TCCR0,WGM00);\nSET_BIT(TCCR0,WGM01);\n\n") 
        file3.close() 
        Duty_fun() 
 
         
     
#display the intr availability 
def Intr(*args): 
    m     = options.get() 
    intr  = options2.get() 
    file3 = open("Init.c","a+") 
 
    if intr == 'Enable': 
        file3.write("//Interrupt Enabled   \n\n") 
        if m == 'Normal' : 
            file3.write("SET_BIT(TIMSK,TOIE0); \n") 
             
        else:  
            file3.write("SET_BIT(TIMSK,OCIE0); \n") 
    
    else: 
            file3.write("//Interrupt Disabled   \n\n") 
     
    file3.close() 
     

#display the choosen prescalar
def Prescalar (*args): 
    Pre   = options3.get() 
    file3 = open("Init.c","a+") 
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
         
#display the choosen output on oc0  
def oc0 (*args): 
    oc    = options4.get() 
    mode  = options.get() 
    file3 = open("Init.c","a+") 
    if mode == 'Normal' or mode == 'Output Compare' or mode == 'PWM_FAST' or mode == 'PWM_Phase' : 
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
     
         
     
 
 
Timer_Window.mainloop()