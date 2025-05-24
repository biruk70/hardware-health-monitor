import psutil
import platform
import socket
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Collect system metrics
def collect_system_metrics():
    battery = psutil.sensors_battery()
    metrics = {
        "CPU Usage (%)": psutil.cpu_percent(interval=1),
        "Memory Usage (%)": psutil.virtual_memory().percent,
        "Available Memory (MB)": psutil.virtual_memory().available / 1024 / 1024,
        "Disk Usage (%)": psutil.disk_usage('/').percent,
        "Available Disk (GB)": psutil.disk_usage('/').free / 1024 / 1024 / 1024,
        "Battery (%)": battery.percent if battery else None,
        "Is Charging": battery.power_plugged if battery else None,
        "System": platform.system(),
        "Release": platform.release(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Time Collected": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return metrics

# Get metrics
data = collect_system_metrics()

# Convert to DataFrame
df = pd.DataFrame(data.items(), columns=["Metric", "Value"])
print(df)

# Plot percentage metrics
fig, ax = plt.subplots()
plot_data = df[df['Metric'].isin(["CPU Usage (%)", "Memory Usage (%)", "Disk Usage (%)", "Battery (%)"])]
plot_data = plot_data.dropna()
plot_data["Value"] = plot_data["Value"].astype(float)
ax.bar(plot_data["Metric"], plot_data["Value"])
ax.set_title("System Usage")
ax.set_ylabel("Percentage")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
