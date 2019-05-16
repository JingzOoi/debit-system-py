import formLogin
import PySimpleGUI as sg

layout = [
    [sg.Text('Main Menu', key='_title_')],
    [sg.Button('Point-of-Sale interface', key='_POS_')],
    [sg.Button('Order History', key='_order_')],
    [sg.Button('Logout', key='_logout_')]
]

window = sg.Window('Main Menu', layout)


def run(session: dict):
    while True:
        event, values = window.Read()
        if event is None:
            break
        elif event == '_logout_':
            window.Close()
            formLogin.run()
            break
