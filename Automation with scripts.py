import os
import shutil
from datetime import datetime

# Display current date and time
current_time = datetime.now()

print("===== Task Automation Script =====")
print("Current Date and Time:", current_time)

# Create log file
log_file = "task_log.txt"

with open(log_file, "a") as file:
    file.write(f"Task executed at: {current_time}\n")

print("Log saved successfully in task_log.txt")

# Create backup folder if it doesn't exist
backup_folder = "backup"

if not os.path.exists(backup_folder):
    os.mkdir(backup_folder)

# Copy log file to backup folder
shutil.copy(log_file, backup_folder)

print("Backup created successfully.")
print("Automation task completed!")