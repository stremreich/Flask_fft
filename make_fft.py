import numpy as np
import scipy.io.wavfile as wavfile
import scipy.signal as signal

def get_waveform(file_path):
    # Load audio file
    sample_rate, data = wavfile.read(file_path)
    
    # Normalize data
    data = data / np.max(np.abs(data))
    
    return data.tolist()

def get_fft(file_path):
    # Load audio file
    sample_rate, data = wavfile.read(file_path)
    
    # Compute FFT
    _, _, fft_data = signal.stft(data, fs=sample_rate, nperseg=1024)
    
    return fft_data.tolist()
