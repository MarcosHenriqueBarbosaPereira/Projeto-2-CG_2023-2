import threading
import PySimpleGUI as sg
import os.path
import torch
from TTS.api import TTS
from torchMain import generate

sg.theme("DarkBlue14")

readText = str('')
sourceAudio = str('')

device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

#cria a coluna de importar o arquivo
file_list_column = [
    #importação do arquivo de audio
    [
        sg.Text("Audio Sample Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER1-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 10), key="-FILE LIST1-"
        )
    ],
    #Inserção do texto
    [
        sg.Text("Reading text"),
        sg.InputText(enable_events=True, key='-IN-'),
        
    ],
    #botão de converter
    [
        sg.Button("Gerar", key="-TORCH-")
    ]
]

#criando o layout
layout = [
    [
        sg.Column(file_list_column),
    ]
]

#abre a janela
window = sg.Window("Audio Generator", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    #quando seleciona a pasta, mostra uma lista de arquivos
    if event == "-FOLDER1-":
        folder = values["-FOLDER1-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".wav", ".mp3", ".flac"))
            and not f.startswith("output_result")
        ]
        
        window["-FILE LIST1-"].update(fnames)
    #quando seleciona o arquivo
    elif event == "-FILE LIST1-": 
        try:
            filename = values["-FILE LIST1-"][0]
            sourceAudio = filename

        except:
            pass

    #quando entra com um texto
    elif event == "-IN-":
        readText = values["-IN-"]        
        

    #quando o botao de converter é pressionado, chama a função de converter e atualiza a imagem da direita
    elif event == "-TORCH-":
       
        x = threading.Thread(target=generate,args=(readText,sourceAudio, tts))
        x.start()


window.close()