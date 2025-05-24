# 🖥️ Hardware Health Monitor Dashboard

A Python-based dashboard that displays real-time system health metrics such as CPU usage, memory usage, disk space, battery status, and basic hardware info. Built using `psutil`, `matplotlib`, and `pandas`.

## 🔧 Features

- ✅ Live monitoring of:
  - CPU usage
  - RAM usage and available memory
  - Disk usage and available storage
  - Battery percentage and charging status (if available)
  - System info: OS, processor, IP address, machine type
- 📊 Bar chart visualization using `matplotlib`
- 🧠 Easy to extend with logging or a web interface (like Streamlit)

## 🚀 How to Run

1. **Clone the repository**
```bash
git clone https://github.com/biruk70/hardware-health-monitor.git
cd hardware-health-monitor
Install the required packages

bash
Copy
Edit
pip install psutil pandas matplotlib
Run the Python script

bash
Copy
Edit
python hardware_dashboard.py
📦 Dependencies
psutil

pandas

matplotlib

You can install them all at once using:
