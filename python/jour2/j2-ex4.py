import psutil
import time

def monitor_cpu(interval=5, duration=None):
    start_time = time.time()

    while duration is None or time.time() - start_time < duration:
        cpu_usage = psutil.cpu_percent(interval=interval)
        print(f"Utilisation du CPU : {cpu_usage}%")
        time.sleep(interval)

monitor_cpu(duration=30)