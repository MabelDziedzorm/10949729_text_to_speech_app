import PySimpleGUI as sg
import pyttsx3

engine = pyttsx3.init()

def speak(text, voice):
    engine_voice = engine.getProperty('voices')
    if voice == 'Female':
        engine.setProperty('voice', engine_voice[1].id)
    engine.say(text)
    engine.runAndWait()
text = sg.Input('', enable_events=True, key='INPUT', font=('Arial Bold', 20), expand_x=True, justification='left')
gender =sg.Combo(['Male', 'Female'], default_value='Male')
layout = [[sg.Text('Enter text to speak:')],
          [text],
          [sg.Text('Select voice type:'),           gender],
          [sg.Button('Speak'), sg.Button('Exit')]]

window = sg.Window('Text-to-Speech App', layout)
while True:
    event, values = window.read()
# End program if user closes window or
# presses the Exit button
    if event == "Exit" or event == sg.WIN_CLOSED:
        window.close()
        break
    if event == 'INPUT':
        output =values['INPUT']
    if event == "Speak":
        speak(output, values[0])
        



