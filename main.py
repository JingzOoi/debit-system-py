import formLogin
import PySimpleGUI as sg

layout = [
    [sg.Text('Debit System on Python')],
    [sg.OK(), sg.Quit()]
]

window = sg.Window('Welcome', layout)

while True:

    event, values = window.Read()

    if event is None or event == 'Quit':
        break
    else:
        window.Close()
        formLogin.run()
        break
