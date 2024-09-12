import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt

def real_cepstrum(x):
    # Compute the real cepstrum of a signal.
    spectrum = np.fft.fft(x)
    log_spectrum = np.log(np.abs(spectrum))
    ceps = np.fft.ifft(log_spectrum).real
    return ceps

sample_rate, audio_data = wavfile.read('256.wav')

# calculate the real cepstrum
ceps = real_cepstrum(audio_data)

# Apply a filter to only keep the quefrency 20–30 range
ceps_filtered = np.zeros_like(ceps)
ceps_filtered[20:30] = ceps[20:30]

log_spectrum_filtered = np.fft.fft(ceps_filtered)
spectrum_filtered = np.exp(log_spectrum_filtered)
audio_filtered = np.fft.ifft(spectrum_filtered).real

wavfile.write('filtered_audio_20_30.wav', sample_rate, audio_filtered.astype(np.int16))

plt.plot(ceps_filtered[10:50])
plt.title('Filtered Cepstrum (Quefrency 20-30)')
plt.xlabel('Quefrency')
plt.ylabel('Amplitude')
plt.savefig('filtered_cepstrum_plot.png')
