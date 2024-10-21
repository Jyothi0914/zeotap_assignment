import matplotlib.pyplot as plt

def plot_temperature_trends(data):
    timestamps = [d['timestamp'] for d in data]
    temps = [d['temperature'] for d in data]

    plt.plot(timestamps, temps)
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Trends')
    plt.show()
