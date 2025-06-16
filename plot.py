import numpy as np
import matplotlib.pyplot as plt

def plot_sine_wave():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sin(x)

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label='sin(x)')
    plt.title('Sine Wave Example')
    plt.xlabel('x (radians)')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_square_wave():
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.sign(np.sin(x))

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label='Square Wave', color='orange')
    plt.title('Square Wave Example')
    plt.xlabel('x (radians)')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    
if __name__ == "__main__":
    plot_sine_wave()
