import PySimpleGUI as sg

file = open("IIC.c","w+")

file.write('#include "IIC.h"\n#include "BIT_MATH.h"\n#include "DIO_reg.h"\n#include "STD_TYPES.h"\n#include <avr/io.h> \n ')
file.write('\n/*Define bit rate*/\n')


#display prescaler

def prescaler(*args):
 
  file2 = open("IIC.c","a+")
  if pre =='1':
      file2.write("\n\n//prescaler = 1 \n\n")
      file2.write("#define BITRATE(TWSR)   (D_CPU/SCL_CLK)-16)/2*pow(4,TWSR &=(~((0 << TWPS1) | (0 << TWPS0)))));")
      
  elif pre =='4':
      file2.write("\n\n//prescaler = 4 \n\n")
      file2.write("#define BITRATE(TWSR)   (D_CPU/SCL_CLK)-16)/2*pow(4,TWSR &=(~((0 << TWPS1) | (1 << TWPS0)))));")
      
  elif pre =='16':
      file2.write("\n\n//prescaler = 16 \n\n")
      file2.write("#define BITRATE(TWSR)   (D_CPU/SCL_CLK)-16)/2*pow(4,TWSR &=(~((1 << TWPS1) | (0 << TWPS0)))));")
      
  elif pre =='64':
      file2.write("\n\n//prescaler = 64 \n\n")
      file2.write("#define BITRATE(TWSR)   (D_CPU/SCL_CLK)-16)/2*pow(4,TWSR &=(~((1 << TWPS1) | (1 << TWPS0)))));")
      
file.close()

#interrupt
def INTERRUPT(*args):
 
  file3 = open("IIC.c","a+")
  if interrupt =='enable':
      file3.write("\n\n//enable interrupt  \n\n")
      file3.write("SET_BIT(TWCR,TWINT);\n")
      file3.write("SET_BIT(TWCR,TWIE);\n")
      
  else:
      file3.write("Interrupt Disapled")
      
file.close()


#Initialization
file = open("IIC.c","a+")
file.write("\n/*I2C Initialize function*/\n")
file.write("\nvoid I2C_Init(void)\n{\n")
file.write("//TWI intialization\n//Bit Rate: 100000 KHz\n")
file.write(" TWBR = BITRATE(TWSR=0X00); /*Get bit rate register value by formula*/\n //Two Wire Bus Slave Address: 0x1\n")
file.write(" TWAR = 0X02;\n // Generate Acknowledgment pulse: on/n // TWI Interrupt off\n")
file.write(" TWCR = 0X44;\n TWSR = 0X00;\n ")

#I2C_Start
file.write("\n\nvoid TWIStart(void)\n{\n //send start Condition\n TWCR = (1 << TWINT) | (1 << TWSTA) | (1 << TWEN);\n\n// wait for TWINT flag set in TWCR Register\n while (!(TWCR & (1 << TWINT)));\n}")

#I2C_Write
file.write("\n\nvoid TWIWrite(unsigned char data)\n{\n // put data on TWI Register\n TWDR = data;\n // send data")
file.write("\n TWCR = (1 << TWINT) | (1 << TWEN);\n // wait for TWINT flag set in TWCR Register\n while (!(TWCR & (1 << TWINT)));\n}") 


#I2C_Read
def Read(*args):
 
    file3 = open("IIC.c","a+")
    if Read_Data == 'enable':
        file3.write("unsigned char TWI_Read(unsigned char isLast)\n{\n if(isLast == 0)        //if want to read only one byte\n")
        file3.write("  TWCR = (1 << TWINT) | (1 << TWEN) | (1 << TWEA);\n else\n  TWCR = (1 << TWINT) | (1 << TWEN);\n while((TWCR & (1 << TWINT)) == 0;\n return TWDR;\n}")
    else:
        file4.write("Read_Data_Disapled")
file.close()

#I2C_ReadACK
def Acknowledge(*args):
 
  file3 = open("IIC.c","a+")
  if READ_Acknowledge =='enable':
        file3.write("\n\nunsigned char TWIReadACK(void)\n{\n")
        file3.write("\n TWCR = (1 << TWINT) | (1 << TWEN) |(1 << TWEA);//enable ACK\n // wait for TWINT flag set in TWCR Register\n while (!(TWCR & (1 << TWINT)));\n}") 
  else:
      file3.write("Acknowledge Disapled")
file.close()
  
      
#I2C_ReadNACK
def NAcknowledge(*args):
  
  file3 = open("IIC.c","a+")
  if READ_NAcknowledge =='enable':
        file3.write("\n\nunsigned char TWIReadNACK(void)\n{\n")
        file3.write("\n TWCR = (1 << TWINT) | (1 << TWEN);\n // wait for TWINT flag set in TWCR Register\n while (!(TWCR & (1 << TWINT)));\n// Read Data\n return TWDR;\n}") 

  else:
      file3.write("NAcknowledge Disapled")
file.close()
      

#Get_status
file = open("IIC.c","a+")
file.write("\n\nunsigned char TWIGetStatus(void)\n{\n")
file.write("unsigned char Status;\n Status = TWSR & 0xF8;\n return Status;\n}")

#I2C_Stop
file.write("\n\nvoid TWIStop(void)\n{\n //send stop condition")
file.write("\n TWCR = (1 << TWINT) | (1 << TWEN) | (1 << TWEN) | (1 << TWSTO);\n")

file.close()

##----------------------------------------------------------- GUI Interface --------------------------------------------------------------------------------

E_Interrupt_layout = [

        [sg.Text("Interrupt on Match     "),
         sg.Combo(values=['Enable'], default_value="", size=(8, 1), key='_optionsEnable_')],
]

D_Interrupt_layout = [

        [sg.Text("Interrupt on Match     "),
         sg.Combo(values=['Disaple'], default_value="", size=(8, 1), key='_optionsDisaple_')],
]

E_Read_NACK_layout = [

        [sg.Text("NAcknowledgment on Match     "),
         sg.Combo(values=['Disaple'], default_value="", size=(8, 1), key='_optionsDisaple_')],
]

D_Read_NACK_layout = [

        [sg.Text("NAcknowledgment on Match     "),
         sg.Combo(values=['Disaple'], default_value="", size=(8, 1), key='_optionsDisaple_')],
]

E_Read_ACK_layout = [

        [sg.Text("Acknowledgment on Match     "),
         sg.Combo(values=['Disaple'], default_value="", size=(8, 1), key='_optionsDisaple_')],
]

D_Read_ACK_layout = [

        [sg.Text("Acknowledgment on Match     "),
         sg.Combo(values=['Disaple'], default_value="", size=(8, 1), key='_optionsDisaple_')],
]


I2C_Choice_List_Column = [
    
    [sg.Text('I2C Initialization')],
    [sg.Text("Pick the parameters for I2C ")],
     [sg.Text("Interrupt               "),
         sg.Combo(values=['Enable', 'Disable'], default_value="", size=(8, 1), key='_Interrupt_')],
        [sg.Text("Prescaler             "),
         sg.Combo(values=['1', '4', '16', '64'], default_value="", size=(8, 1), key='_Prescaler_')],
    
    
    
     [sg.Button(button_text="Generate Code", key="_generate_I2C_", enable_events=True)]
    
    ]
    
    code_viewer_column = [
    [sg.Multiline("Your code will be previewed here \nand a file will be created in your directory", font='any 10',
                  justification="center",  size=(70, 15), key="-CODE_I2C-")],
]

    