import simpleaudio as sa
import pathlib
from pathlib import Path
import random
playlist=[str(Path("discoMusic/disco-145049.wav")),str(Path("discoMusic/fairiesx27-disco-145381.wav")),str(Path("discoMusic/funky-disco-140046.wav")),str(Path("discoMusic/funky-disco-155292.wav")),str(Path("discoMusic/pop-nu-disco-dancing-on-the-moon-111445.wav"))]
index=random.randint(0,len(playlist))
filePath=playlist[index]
wav_obj=sa.WaveObject.from_wave_file(filePath)
play_obj=wav_obj.play()
play_obj.wait_done()