import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt

# load the WAV file
sample_rate, audio_data = wavfile.read('256.wav')

# compute the frequency domain of the audio signal
spectrum = np.fft.fft(audio_data)

# compute the logarithm of the magnitude spectrum
log_spectrum = np.log(np.abs(spectrum))

# compute theinverse FFT which is cepstrum
cepstrum = np.fft.ifft(log_spectrum).real

plt.plot(cepstrum)
plt.title('Full Cepstrum of the audio signal')
plt.xlabel('Quefrency')
plt.ylabel('Amplitude')
plt.savefig('full_cepstrum_plot.png')

log_spectrum_reconstructed = np.fft.fft(cepstrum)
spectrum_reconstructed = np.exp(log_spectrum_reconstructed)
audio_reconstructed = np.fft.ifft(spectrum_reconstructed).real
wavfile.write('reconstructed_audio.wav', sample_rate, audio_reconstructed.astype(np.int16))

