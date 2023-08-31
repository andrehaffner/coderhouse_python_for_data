from plyer import notification
from datetime import datetime


def alert(level, base, stage):
    if int(level) == 1:
        title = "Soft alert"
    elif int(level) == 2:
        title = "Medium alert"
    elif int(level) == 3:
        title = "Loud alert"
    else:
        notification.notify(title="Invalid alert level", message="", app_name="notification.py", timeout=5)
        return
    now = datetime.now()
    message = f"failed to load base {base} on stage {stage}\n{now}"
    notification.notify(title=title, message=message, app_name="notification.py", timeout=5)


alert(0, "base 0", "preparing data")
alert(3, "base 3", "reporting data")
