#Modelo de Chat com intereação fala-escuta

# ====================================================================================
# 0 - IMPORTANDO BIBLIOTECAS 
# ====================================================================================
import os
import sounddevice as sd
import numpy as np
import wavio
import speech_recognition as sr
from gtts import gTTS
import pygame
from dotenv import load_dotenv

# ====================================================================================
# CONFIGURAÇÕES INICIAIS
# ====================================================================================

# Carrega variáveis do arquivo .env
load_dotenv("chatbotK.env")

# Pega a chave da Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


#Definindo o modelo de LLM
from langchain_groq import ChatGroq
chat = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)


# Duração da gravação em segundos
DURACAO_GRAVACAO = 5
# Taxa de amostragem do áudio
FS = 44100

# ====================================================================================
# FUNÇÃO 1 - GRAVAR ÁUDIO
# ====================================================================================
def gravar_audio(filename="entrada.wav", duracao=DURACAO_GRAVACAO, fs=FS):
    print("Gravando sua voz...")
    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1, dtype=np.int16)
    sd.wait()
    wavio.write(filename, audio, fs, sampwidth=2)
    print("Gravação concluída.")

# =====================================================================================
# FUNÇÃO 2 - RECONHECER TEXTO
# =====================================================================================
def reconhecer_texto(filename="entrada.wav"):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)
    try:
        texto = r.recognize_google(audio, language="pt-BR")
        print(f"Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print("Não entendi o que foi dito.")
        return ""
    except sr.RequestError:
        print("Erro ao conectar com o serviço de reconhecimento de voz.")
        return ""


# ===================================================================================
# FUNÇÃO 3 - GERAR RESPOSTA 
# ===================================================================================
def gerar_resposta(prompt):
    try:
        # Usando o modelo de chat llama
        resposta = chat.invoke(f"Usuário disse: {prompt}")
        
        # Exibe e retorna a resposta em texto
        print(f"\n Resposta: {resposta.content}\n")
        return resposta.content

    except Exception as e:
        print(f" Erro ao gerar resposta: {e}")
        return "Desculpe, ocorreu um erro ao processar sua resposta."


# ====================================================================================
# FUNÇÃO 4 - FALAR TEXTO
# ====================================================================================
def falar_texto(texto):
    if not texto:
        return
    tts = gTTS(text=texto, lang="pt")
    tts.save("resposta.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("resposta.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

# =====================================================================================
# FLUXO PRINCIPAL
# =====================================================================================
if __name__ == "__main__":
    print("=== Chatbot de Áudio com GPT ===")
    gravar_audio()
    texto_usuario = reconhecer_texto()
    if texto_usuario:
        resposta = gerar_resposta(texto_usuario)
        falar_texto(resposta)
    else:
        print("Nenhum áudio reconhecido. Tente novamente.")