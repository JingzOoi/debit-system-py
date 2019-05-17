import formLogin
import formItem
import PySimpleGUI as sg

layout = [
    [sg.Text('Main Menu', key='_title_')],
    [sg.Button('Point-of-Sale interface', key='_POS_')],
    [sg.Button('Manage Order', key='_order_')],
    [sg.Button('Manage Menu', key='_menu_')],
    [sg.Button('Manage Employee', key='_employee_')],
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
        elif event == '_menu_':
            formItem.run()
