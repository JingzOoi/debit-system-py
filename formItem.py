import PySimpleGUI as sg
import class_item

layout = [
    [sg.Text('Add Item')],
    [sg.Text('ID: '), sg.InputText(key='_id_')],
    [sg.Text('Name: '), sg.InputText(key='_name_')],
    [sg.Text('Price: '), sg.InputText(key='_price_')],
    [sg.Button('Search', key='_search_'), sg.Button('Add', key='_add_'), sg.Button(
        'Update', key='_update_'), sg.Button('Delete', key='_delete_'), ]
]


def run():

    while True:

        window = sg.Window('Add Item', layout)

        event, values = window.Read()

        if event is None or event == 'Cancal':
            window.Close()
            break

        else:
            txtName = window.Element('_name_')
            txtPrice = window.Element('_price_')
            txtID = window.Element('_id_')

            if event == '_search_':

                try:
                    item = class_item.item_list_search(values["_id_"])
                except KeyError:
                    sg.PopupError('Item not found')
                    window.Close()

                txtID.Update(value=item["id"])
                txtName.Update(value=item["name"])
                txtPrice.Update(value=item["price"])
                window.Close()

            elif event == '_add_':
                if values["_id_"] == '' or values["_name_"] == '' or values["_price_"] == '':
                    sg.PopupError('Fill in all the details')
                    window.Close()
                else:
                    try:
                        item = class_item.Item({
                            "id": values["_id_"],
                            "name": values["_name_"],
                            "price": float(values["_price_"])
                        })
                        item.add()
                        sg.Popup('Item added')
                        window.Close()
                    except ValueError:
                        sg.PopupError('Value Error')
                        window.Close()
