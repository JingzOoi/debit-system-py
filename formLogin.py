import class_employee
import mainMenu
import PySimpleGUI as sg

layout = [
    [sg.Text('Login')],
    [sg.Text('Username'), sg.InputText(key='_username_')],
    [sg.Text('Password'), sg.InputText(key='_password_')],
    [sg.Submit(), sg.Quit()]
]


def run():
    while True:
        window = sg.Window('Login', layout)

        event, values = window.Read()
        if event is None or event == 'Quit':
            window.Close()
            break
        else:
            for employee in class_employee.employee_list().values():
                if employee["username"] == values["_username_"]:
                    if employee["password"] == values["_password_"]:
                        emp = employee
                        window.Close()
                        mainMenu.run(emp)
                        break
                    else:
                        sg.PopupError(
                            'Incorrect password')
                        window.Close()
                        break
            else:
                sg.PopupError('Username not found in database')
                window.Close()
                break
