#program that returns bpm, stats, as well as recommended songs based on image
#return stats in plaintext
#add spectogram in new directory

# Beat tracking example
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

#sound processing
import librosa
import librosa.display

#audio fingerprinting
import acoustid

# 1. Get the file path to the included audio example
filename = "sample.mp3"


#audio fingerprinting
#apikey = 'zEGpWdmmMA'
#duration = 25
#g = open("fingerprint.txt", "w+")
#g.write(acoustid.lookup(apikey,acoustid.fingerprint(44100,2,2),duration))

g.close()
print ("done fingerprinting")


# 2. Load the audio as a waveform `y`
#    Store the sampling rate as `sr`
y, sr = librosa.load(filename)

# 3. Run the default beat tracker
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# 4. Convert the frame indices of beat events into timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

#5. Compute short term fourier transformation of y
D = librosa.stft(y)

#6. Decompose stft into harmonic and percussive comps
D_harm, D_perc = librosa.decompose.hpss(D)

#7. print various spectograms
# Pre-compute a global reference power from the input spectrum
print("Plotting spectograms...\n")
rp = np.max(np.abs(D))

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
librosa.display.specshow(librosa.amplitude_to_db(D, ref=rp), y_axis='log')
plt.colorbar()
plt.title('Full spectrogram')

plt.subplot(3, 1, 2)
librosa.display.specshow(librosa.amplitude_to_db(D_harm, ref=rp), y_axis='log')
plt.colorbar()
plt.title('Harmonic spectrogram')
#save image as spectrogram
plt.savefig("spectrograms.png")

plt.subplot(3, 1, 3)
librosa.display.specshow(librosa.amplitude_to_db(D_perc, ref=rp), y_axis='log', x_axis='time')
plt.colorbar()
plt.title('Percussive spectrogram')
plt.tight_layout()

#print beat info into txt file
f = open("tempo.txt" ,"w+")
f.write("Your song played at {:.2f} bpm".format(tempo))
f.close()

#print beat_times to csv
print('Saving beat output to beat_times.csv')
librosa.output.times_csv('beat_times.csv', beat_times)
