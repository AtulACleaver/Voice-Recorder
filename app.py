import sounddevice
from scipy.io.wavfile import write

# Import both of them and if you are new and confused just download pycharm–it is an IDE–, It will help you to
# download it.

# This is a sample rate
fs = 44100

second = int(input("Enter your time duration of the audio in seconds: "))  # This is the total time this video
# recording will go

# This will tell you that you have to start speaking
print("Recording...")

# This will record your voice.
record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait()

# Writing the recorded audio file
write("rename.wav", fs, record_voice)  # You can change this rename.wav just don't change .wav

# Optional just for a check
print("Recoding is finished. \nGo check it...")
