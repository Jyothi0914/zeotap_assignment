class AlertSystem:
    def __init__(self, temp_threshold):
        self.temp_threshold = temp_threshold
        self.alert_triggered = False

    def check_alert(self, latest_data):
        temp = latest_data['temperature']
        if temp > self.temp_threshold:
            self.trigger_alert(temp)

    def trigger_alert(self, temp):
        print(f"ALERT: Temperature exceeds {self.temp_threshold}°C! Current temperature: {temp}°C")
        self.alert_triggered = True
