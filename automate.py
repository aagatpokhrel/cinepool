#one time execution only

import os
import platform
import subprocess
from datetime import datetime, time, timedelta

def create_cron_job():
    # Run the script at 3:00 am every day
    cron_time = time(hour=3, minute=0)
    path_to_script = os.path.join(os.getcwd(),"/pipeline/main.py")
    cron_command = "python {}".format(path_to_script)

    # Add the cron job to the crontab
    os.system("echo '%s %s * * * %s' >> mycron" % (cron_time.minute, cron_time.hour, cron_command))
    os.system("crontab mycron")
    os.remove("mycron")


def create_task_scheduler_job():
    # Run the script at 3:00 am every day
    start_date = datetime.now() + timedelta(days=1)
    start_time = time(hour=3, minute=0)

    # Build the task scheduler command
    path_to_script = os.path.join(os.getcwd(),"/pipeline/main.py")
    task_command = "python {}".format(path_to_script)
    task_command_args = ""
    task_name = "My Script"
    task_trigger = "/Daily /At %s:%s /Next:%s" % (start_time.hour, start_time.minute, start_date.strftime('%Y-%m-%d'))

    # Create the task scheduler job
    subprocess.run(["schtasks.exe", "/Create", "/TN", task_name, "/TR", task_command,"/SC", "Daily", "/ST", start_time.strftime('%H:%M'), "/SD", start_date.strftime('%m/%d/%Y'), "/F"])

def main():
    # Determine the operating system
    os_type = platform.system()

    # Create the task scheduler or cron job, depending on the operating system
    if os_type == "Windows":
        create_task_scheduler_job()
    elif os_type == "Linux":
        create_cron_job()
    else:
        print("Unsupported operating system")

if __name__ == "__main__":
    main()
