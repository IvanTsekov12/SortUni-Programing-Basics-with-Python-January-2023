import time

from plyer import notification

task = input("Enter the task: ")
show_after_secs = int(input("Set the timer to (seconds): "))
# TODO Let the user choose hours, minutes or seconds

time.sleep(show_after_secs)  # accept seconds

notification.notify(
    title="Reminder",
    message=task,
    app_icon="icon.ico",
)
