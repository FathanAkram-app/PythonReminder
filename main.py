import PySimpleGUI as sg
import time

window = sg.Window(
    title="You Lived", 
    layout=[
        [sg.Text(size=(21,2),font=('Oswald',32),text='Reminder')],
        [sg.Text(size=(21,1),font=('Oswald',21), key='seconds')],
        [sg.ProgressBar(60, orientation='h', size=(40, 10), key='pBarS')],
        [sg.Text(size=(21,1),font=('Oswald',21), key='minutes')],
        [sg.ProgressBar(60, orientation='h', size=(40, 10), key='pBarM')],
        [sg.Text(size=(21,1),font=('Oswald',21), key='hours')],
        [sg.ProgressBar(60, orientation='h', size=(40, 10), key='pBarH')],
        [sg.Text("",size=(5,5))],
        [sg.Text('Set a reminder',font=('Oswald',21))],
        [sg.Text('Seconds', size =(15, 1)), sg.InputText()],
        [sg.Text('Minutes', size =(15, 1)), sg.InputText()],
        [sg.Text('Hours', size =(15, 1)), sg.InputText()],
        [sg.Text('Notes', size =(15, 1)), sg.InputText()],
        [sg.Submit(), sg.Cancel()]
    ], 
)

while window(timeout=20)[0] != sg.WIN_CLOSED:
    current_time = time.localtime()
    final_time = lambda x : time.strftime(x, current_time)
    window['seconds']("Seconds: "+str(final_time("%S")))
    window['pBarS'].UpdateBar(final_time("%S"))
    window['minutes']("Minutes: "+str(final_time("%M")))
    window['pBarM'].UpdateBar(final_time("%M"))
    window['hours']("Hours: "+str(final_time("%H")))
    window['pBarH'].UpdateBar(final_time("%H"))