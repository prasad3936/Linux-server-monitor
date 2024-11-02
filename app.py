import psutil
import platform
import time
import docker
from flask import Flask, render_template
from datetime import timedelta

app = Flask(__name__)
client = docker.from_env()  # Initialize the Docker client

def bytes_to_gb(bytes_value):
    """Convert bytes to gigabytes."""
    return round(bytes_value / (1024 ** 3), 2)

def calculate_cpu_percent(cpu_stats, precpu_stats):
    """Calculate the CPU usage percentage for Docker containers."""
    try:
        cpu_delta = cpu_stats['cpu_usage']['total_usage'] - precpu_stats['cpu_usage']['total_usage']
        system_delta = cpu_stats['system_cpu_usage'] - precpu_stats['system_cpu_usage']
        
        num_cpus = len(cpu_stats['cpu_usage']['percpu_usage']) if 'percpu_usage' in cpu_stats['cpu_usage'] else 1
        
        if system_delta > 0 and cpu_delta > 0:
            cpu_percent = (cpu_delta / system_delta) * num_cpus * 100
        else:
            cpu_percent = 0.0
        return round(cpu_percent, 2)
    except KeyError:
        return 0.0

@app.route('/')
def index():
    # Get CPU and memory usage for the host
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    # Convert system memory values to GB
    memory_total_gb = bytes_to_gb(memory.total)
    memory_used_gb = bytes_to_gb(memory.used)
    memory_free_gb = bytes_to_gb(memory.available)
    memory_percent = memory.percent

    # Get OS Version and Type
    os_version = platform.platform()
    os_type = platform.system()

    # Get system uptime in hours, minutes, and seconds
    uptime_seconds = int(time.time() - psutil.boot_time())
    uptime_str = str(timedelta(seconds=uptime_seconds))  # Format as HH:MM:SS

    # Get all containers (both running and stopped)
    containers_info = []
    for container in client.containers.list(all=True):
        container_info = {
            "name": container.name,
            "id": container.short_id,
            "status": container.status,
        }

        if container.status == 'running':
            container_stats = container.stats(stream=False)
            cpu_usage_percent = calculate_cpu_percent(
                container_stats['cpu_stats'],
                container_stats['precpu_stats']
            )

            memory_usage_gb = bytes_to_gb(container_stats['memory_stats']['usage'])
            memory_limit_gb = bytes_to_gb(container_stats['memory_stats']['limit'])

            container_info.update({
                "cpu_usage": f"{cpu_usage_percent}%",
                "memory_usage": f"{memory_usage_gb} GB",
                "memory_limit": f"{memory_limit_gb} GB"
            })
        else:
            container_info.update({
                "cpu_usage": "N/A",
                "memory_usage": "N/A",
                "memory_limit": "N/A"
            })

        containers_info.append(container_info)

    return render_template(
        'index.html',
        cpu_percent=cpu_percent,
        memory_total_gb=memory_total_gb,
        memory_used_gb=memory_used_gb,
        memory_free_gb=memory_free_gb,
        memory_percent=memory_percent,
        os_version=os_version,
        os_type=os_type,
        uptime_str=uptime_str,  # Pass formatted uptime
        containers_info=containers_info
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
