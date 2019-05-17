import PySimpleGUI as sg
import class_employee

layout = [
    [sg.Text('ID: '), sg.InputText(key='id')],
    [sg.Text('IC: '), sg.InputText(key='ic')],
    [sg.Text('Name: '), sg.InputText(key='name')],
    [sg.Text('Phone: '), sg.InputText(key='phone')],
    [sg.Text('Email: '), sg.InputText(key='email')],
    [sg.Text('Username: '), sg.InputText(key='username')],
    [sg.Text('Password: '), sg.InputText(key='password')],
    [sg.Submit(), sg.Cancel()]
]

def run():
    window = sg.Window('Add New Employee', layout)
    event, values = window.Read()
    if event == None or event == 'Cancel':
        window.Close()
    else:
        emp = class_employee.Employee(values)
        emp.add()
        sg.Popup('Employee Added.')
        window.Close()
