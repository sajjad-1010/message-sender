# import ilb
import pyautogui as pt 
import time 

#app name
print(''' 
=============
easy messager
=============
\n''')
input('***Press Anything to ENTER***\n')

#send message function
def send_M():
    
    #variable to get the delimiter
    limit = int(input('import limit:')) 
    
    #variable to get the message
    message = input('enter message:')
    
    i = 0 

    #time sleep for user to go in the messanger and click the text box
    time.sleep(3)

    #while for message to send
    while i < limit:
        
        #calling the ilb
        pt.typewrite(message)
        
        #sleep time for writing the message
        time.sleep(1)
        
        #press enter
        pt.press('enter')
    
        i+=1
    
    #calling a (again) function for start the app again
    again()

#again function
def again():
    
    cal_a = input(''' 
    do you wants to try again?
    enter (Y) for yes enter (N) for no:''')
    
    if cal_a.upper() == 'Y':
        send_M()
    
    elif cal_a.upper() == 'N':
        print('\n***Have great day***\n')
    
    else:
        again()
        
send_M()
input("Press Enter to continue..")  