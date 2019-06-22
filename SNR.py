import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from scipy.io import wavfile

file_name = ''                      # Example: file_name = '2500hz.wav'
frequency_target =                  # Example: frequency_target = 2500

Fs, data = wavfile.read(file_name)  # File must be in the same directory

data = data[1:Fs*10]

size = np.size(data)

y = abs(fourier.fft(data))
y = y[:np.size(data)//2]

f = np.linspace(0, Fs/2, size//2)

power = y**2 * f

f_margin = round(frequency_target/100)
f_margin_left = round((frequency_target - f_margin) / (Fs/2) * np.size(f))
f_margin_right = round((frequency_target + f_margin) / (Fs/2) * np.size(f))

power_signal = sum(power[f_margin_left:f_margin_right])
power_noise = sum(power) - power_signal

SNR = power_signal / power_noise

print(SNR)

plt.plot(f, y)
plt.show()
