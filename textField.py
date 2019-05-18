def is_filled(valuesList):
    for value in valuesList.values():
        if value == '':
            return False
    else:
        return True


def update(textFieldsList, values: list):
    for textField, value in zip(textFieldsList, values):
        textField.Update(value)
