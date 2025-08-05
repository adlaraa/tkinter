import requests
import pprint

url = 'https://teste-473ad-default-rtdb.firebaseio.com/'



# Recebendo do Firebase
def receive_from_firebase(id):
    try:
        _url = f"{url}{id}.json"
        response = requests.get(_url)
        if response.status_code == 200:
            print(f"[Firebase] Status code: {response.status_code}.")
            data = response.json()
            print("[Firebase] Data received successfully.")
            pprint.pprint(data)
            return data
        else:
            print(f"[Firebase] Failed to receive data. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"[Firebase] Error receiving data: {e}")
        return None
    
sade = receive_from_firebase('atual')
  #  87 a 119 

import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
raiz = tk.Tk ()
raiz.title("sweety")
raiz.geometry ("500x200")
quadro = ttk.Frame(raiz)
texto = ttk.Label(quadro, text = (sade))
texto.pack()
botao = ttk.Button(quadro, text = "Sair", command=raiz.destroy)
botao.pack()
quadro.pack(expand=True)
raiz.mainloop()
import tkinter as tk
import serial 
import json
from datetime import datetime

# Leitura dos dados
porta_serial = serial.Serial ('https://teste-473ad-default-rtdb.firebaseio.com/atual.json , 9600, timeout = 1')
def ler_dados():
    try:
        linha = porta_serial.readline().decode().strip()
        if linha:
            dados = json.loads(linha)  # Converte string JSON em dicionário
            data_hora = dados.get("Datetime", "---")
            temp = dados.get("Temperature", "---")
            pressao = dados.get("Pressure", "---")
            return data_hora, temp, pressao
    except Exception as e:
        print("Erro ao ler dados:", e)
    return "---", "---", "---"

# Atualiza os valores no painel
# Interface principal
janela = tk.Tk()
janela.title("Painel Informativo - Clima")
janela.geometry("350x200")
janela.resizable(False, False)
janela.configure(bg="#f0f0f0")

# Labels
label_data = tk.Label(janela, text="🕒 Data/Hora: ---", font=("Arial", 12), bg="#f0f0f0")
label_data.pack(pady=5)

label_temp = tk.Label(janela, text="🌡️ Temperatura: --- °C", font=("Arial", 12), bg="#f0f0f0")
label_temp.pack(pady=5)

label_pressao = tk.Label(janela, text="🌬️ Pressão: --- hPa", font=("Arial", 12), bg="#f0f0f0")
label_pressao.pack(pady=5)

# Botão de saída
botao_sair = tk.Button(janela, text="Sair", command=janela.destroy, bg="#d9534f", fg="white", width=10)
botao_sair.pack(pady=15)

# Começa a atualizar
janela.mainloop()