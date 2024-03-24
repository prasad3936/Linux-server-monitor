import psutil
import platform
import time
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Get CPU and memory usage
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    #Get OS Version#
    os_version = platform.platform()

    #Get OS TYpe 
    os_type = platform.system()

    ## Get system uptime
    uptime_seconds = int(time.time() - psutil.boot_time())
    uptime_minutes, uptime_seconds = divmod(uptime_seconds, 60)
    uptime_hours, uptime_minutes = divmod(uptime_minutes, 60)
            

    return render_template('index.html', cpu_percent=cpu_percent, memory=memory,
                           os_version=os_version, os_type=os_type,
                           uptime_hours=uptime_hours, uptime_minutes=uptime_minutes, uptime_seconds=uptime_seconds)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
