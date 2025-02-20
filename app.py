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































# import psutil
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     cpu_metrix = psutil.cpu_percent(interval=1)
#     mem_metrix = psutil.virtual_memory().percent

#     message = f"CPU Utilization: {cpu_metrix}% and Memory Utilization: {mem_metrix}%"

#     if cpu_metrix > 70 or mem_metrix > 70:
#         alert_mesage = "High CPU or Memory Utilization. Please scale up!!!"
#         message += f" | {alert_mesage}"
#         return message
    
# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0")

    