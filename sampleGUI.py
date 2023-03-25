import PySimpleGUI as sg

history = 'bin/history'

with open(history) as f:
    string = f.readlines()[-1]

layout = [
    [sg.Text('this is test GUI')],
    [sg.Text('Enter something on Row 2'), sg.InputText(string)],
    [sg.Button('ok'), sg.Button('Cancel')]
]

# Create the Window
window = sg.Window('Window Title', layout, keep_on_top=True)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == 'ok':
        with open(history, 'a') as f:
            f.write('\n' + values[0])
    print(event)
    print('You entered ', values[0])

window.close()