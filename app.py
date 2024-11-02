import psutil
import platform
import time
import docker
from flask import Flask, render_template

app = Flask(__name__)
client = docker.from_env()  # Initialize the Docker client

@app.route('/')
def index():
    # Get CPU and memory usage
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    # Get OS Version
    os_version = platform.platform()

    # Get OS Type
    os_type = platform.system()

    # Get system uptime
    uptime_seconds = int(time.time() - psutil.boot_time())
    uptime_minutes, uptime_seconds = divmod(uptime_seconds, 60)
    uptime_hours, uptime_minutes = divmod(uptime_minutes, 60)

    # Get all containers (both running and stopped)
    containers_info = []
    for container in client.containers.list(all=True):
        container_info = {
            "name": container.name,
            "id": container.short_id,
            "status": container.status,
        }

        if container.status == 'running':
            # Get stats for running containers
            container_stats = container.stats(stream=False)
            container_info.update({
                "cpu_usage": container_stats['cpu_stats']['cpu_usage']['total_usage'],
                "memory_usage": container_stats['memory_stats']['usage'],
                "memory_limit": container_stats['memory_stats']['limit']
            })
        else:
            # For stopped containers, stats are not available
            container_info.update({
                "cpu_usage": None,
                "memory_usage": None,
                "memory_limit": None
            })

        containers_info.append(container_info)

    return render_template(
        'index.html',
        cpu_percent=cpu_percent,
        memory=memory,
        os_version=os_version,
        os_type=os_type,
        uptime_hours=uptime_hours,
        uptime_minutes=uptime_minutes,
        uptime_seconds=uptime_seconds,
        containers_info=containers_info
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

