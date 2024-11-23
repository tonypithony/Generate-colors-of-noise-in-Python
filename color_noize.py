# https://stackoverflow.com/questions/67085963/generate-colors-of-noise-in-python
# https://habr.com/ru/articles/321874/

import numpy as np
import matplotlib.pyplot as plt

def plot_spectrum(s):
    f = np.fft.rfftfreq(len(s))
    return plt.loglog(f, np.abs(np.fft.rfft(s)))[0]

def noise_psd(N, psd = lambda f: 1):
        X_white = np.fft.rfft(np.random.randn(N));
        S = psd(np.fft.rfftfreq(N))
        # Normalize S
        S = S / np.sqrt(np.mean(S**2))
        X_shaped = X_white * S;
        return np.fft.irfft(X_shaped);

def PSDGenerator(f):
    return lambda N: noise_psd(N, f)

@PSDGenerator
def white_noise(f):
    return 1;

@PSDGenerator
def blue_noise(f):
    return np.sqrt(f);

@PSDGenerator
def violet_noise(f):
    return f;

@PSDGenerator
def brownian_noise(f):
    return 1/np.where(f == 0, float('inf'), f)

@PSDGenerator
def pink_noise(f):
    return 1/np.where(f == 0, float('inf'), np.sqrt(f))


plt.style.use('dark_background')
plt.figure(figsize=(12, 8), tight_layout=True)
for G, c in zip(
        [brownian_noise, pink_noise, white_noise, blue_noise, violet_noise], 
        ['brown', 'hotpink', 'white', 'blue', 'violet']):
    plot_spectrum(G(30*50_000)).set(color=c, linewidth=3)
plt.legend(['brownian', 'pink', 'white', 'blue', 'violet'])
plt.suptitle("Colored Noise")
plt.ylim([1e-3, None]);
plt.show()



HERTZ = 1

SAMPLE_FREQ_HZ  = 125 * HERTZ
SAMPLE_INTV_SEC = 1/SAMPLE_FREQ_HZ

def plot_test_points(sample_count: int = None):
    n = sample_count if sample_count else 1000
    fig, ax_list = plt.subplots(5, 1, figsize=(12, 8), tight_layout=True)
    i = 0
    for G, c, l in zip(
            [brownian_noise, pink_noise, white_noise, blue_noise, violet_noise],
            ['brown', 'hotpink', 'white', 'blue', 'violet'],
            ['brown', 'pink', 'white', 'blue', 'violet']):
        ax = ax_list[i]
        t = [x*SAMPLE_INTV_SEC for x in range(0, n)]
        ax.plot(t, G(n), color=c, linewidth=0.5, label=l)
        ax.legend(loc='lower left')
        ax.set_xlabel("Time [sec]")
        i += 1
    plt.suptitle(f"Colored Noise (n={n} points; sampling rate = {SAMPLE_FREQ_HZ}Hz)")
    plt.show()

plot_test_points()