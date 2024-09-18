import pyfirmata
import time
from time import sleep
comport='COM8'

board=pyfirmata.Arduino(comport)

right_motor_forward=board.get_pin('d:7:o')
left_motor_forward=board.get_pin('d:6:o')

led_1=board.get_pin('d:13:o')
led_2=board.get_pin('d:2:o')
catch=board.get_pin('d:5:o')
# do_not_catch=board.get_pin('d:4:o')

# led_2=board.get_pin('d:8:o')
# led_4=board.get_pin('d:6:o')
from pyfirmata import INPUT, OUTPUT, PWM
board.digital[10].mode = PWM

value=0.05

# def led(total):
def led(total,obj_direction_x):

    if(total=='bottle' or total=='cup'):

        if (obj_direction_x=='catch'): # remember you have to add conditional position here 
            catch.write(1)
            left_motor_forward.write(0)
            right_motor_forward.write(0)
            # do_not_catch.write(0)
            sleep(value)
            # sleep(1)
        elif (obj_direction_x=='right'):

            right_motor_forward.write(1)
            left_motor_forward.write(0)
            led_1.write(1)
            led_2.write(0)
            # do_not_catch.write(1)
            catch.write(0)
            # #time.sleep(2.0)
            # board.digital[10].write(2.2)
            sleep(value)

        elif (obj_direction_x=='left'):
            right_motor_forward.write(0)
            left_motor_forward.write(1)
            # do_not_catch.write(1)
            catch.write(0)
            led_1.write(0)
            led_2.write(1)
            # board.digital[10].write(2.2)
            sleep(value)
        elif (obj_direction_x=='forward'):
            right_motor_forward.write(1)
            left_motor_forward.write(1) 
            # do_not_catch.write(1)
            catch.write(0)
            led_1.write(1)
            led_2.write(1)           
            # board.digital[10].write(2.3)
            sleep(value)


        elif (obj_direction_x=='none'):
            right_motor_forward.write(0)
            left_motor_forward.write(0)
            # do_not_catch.write(0)
            catch.write(0)
            led_1.write(0)
            led_2.write(0)
            # board.digital[10].write(.0)


        else:
            obj_direction_x=='none'
            right_motor_forward.write(0)
            left_motor_forward.write(0)
            # do_not_catch.write(0)
            catch.write(0)
            led_1.write(0)
            led_2.write(0)
            # board.digital[10].write(0.0)

    else:
        total=='ab'
        obj_direction_x=='none'
        right_motor_forward.write(0)
        left_motor_forward.write(0)
        # do_not_catch.write(0)
        catch.write(0)
        led_1.write(0)
        led_2.write(0)

def nothing(total):
    if(total!='bottle'):
        right_motor_forward.write(0)
        left_motor_forward.write(0)
        # do_not_catch.write(0)
        catch.write(0)
        led_1.write(0)
        led_2.write(0)


