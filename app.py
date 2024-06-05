import sounddevice as sd # pip install sounddevice soundfile

import numpy as np
import soundfile as sf

# Paramètres d'enregistrement
fs = 44100  # fréquence d'échantillonnage
duration = 30  # durée d'enregistrement (en secondes)

# Calcul du nre d'échantillons à enregistrer
num_samples = int(fs * duration)

# Définition de la fonction de rappel pour l'enregistrement
def callback(indata, frames, time, status):
    # Copie des données d'entrée dans un tableau NumPy
    data = np.copy(indata)
    # Écriture des données dans le fichier audio
    sf.write("output.mp3", data, fs)

# Démarrage de l'enregistrement
with sd.InputStream(callback=callback):
    sd.sleep(duration * 1000)  # attente de la fin de l'enregistrement
