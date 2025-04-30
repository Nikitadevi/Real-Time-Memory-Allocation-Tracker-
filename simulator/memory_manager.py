import psutil

def get_system_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    # Provide status
    if cpu_usage < 50 and memory_usage < 60:
        status = "System is in good condition."
    elif cpu_usage < 80 and memory_usage < 80:
        status = "System is under moderate load. Keep an eye on it."
    else:
        status = "High CPU or memory usage! Consider closing some applications."

    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "status": status
    }
