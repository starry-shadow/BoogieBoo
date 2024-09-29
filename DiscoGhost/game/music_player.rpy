import random
class music_player:
    playlist=["discoMusic/disco-145049.wav","discoMusic/fairiesx27-disco-145381.wav","discoMusic/funky-disco-140046.wav","discoMusic/funky-disco-155292.wav","discoMusic/pop-nu-disco-dancing-on-the-moon-111445.wav"]
    def musicPlayer():
        index=random.randint(0,len(playlist)-1) # generates a random index within the list
        play music playlist[index] # plays the random generated music