import psutil
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    
    cpu_metric = psutil.cpu_percent(interval=1)
    memory_metric = psutil.virtual_memory().percent

    message = f"CPU Utilization: {cpu_metric} & Memory Utilzation: {memory_metric}"

    if cpu_metric >70 or memory_metric > 70:
        alert_message = "High CPU or Memory Utilization detected!!!. Please ScaleUp..."
        message += f" | {alert_message}"
        
    return message
    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


    