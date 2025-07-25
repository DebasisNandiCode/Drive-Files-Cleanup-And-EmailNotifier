import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurable Variables
shareDrive_Path = "\\10.xxx.xxx.14\xxxxxxxxxx\reporting\reports"

smtp_username="xxxxxxxxxx@fusioncx.com"
smtp_password="xxxxxxxxxxx"
sender_email = "xxxxxxxxxx@fusioncx.com"
recipient_emails = ["xxxxxxxxxx@fusioncx.com"]
smtp_server = "smtp.office365.com"
smtp_port = 587


# Validate Share Drive Path
if not shareDrive_Path:
    raise ValueError("Share Drive Path is not set.")

# Step 1: Delete .xlsx and .csv files
deleted_files = []

if os.path.exists(shareDrive_Path):
    for file in os.listdir(shareDrive_Path):
        file_path = os.path.join(shareDrive_Path, file)
        if os.path.isfile(file_path) and file.endswith(('.xlsx', '.csv')):
            try:
                os.remove(file_path)
                deleted_files.append(file)
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")
    
    if deleted_files:
        print(f"Deleted {len(deleted_files)} files successfully from Share Drive Path")

else:
    print("Share Drive Folder Path NOT Found!")

# Step 2: Send Email Notification
if deleted_files:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_list = "<br>".join([f"{i+1}. {f}" for i, f in enumerate(deleted_files)])

    subject = "Files Deleted from Share Drive Folder"
    body = f"""\
<html>
<body>
Hello Team,<br><br>
The following {len(deleted_files)} files have been deleted from the Share Drive folder:<br><br>
Time: {now}<br>
Folder Path: {shareDrive_Path}<br><br>
Deleted Files:<br>
{file_list}<br><br>
Regards,<br>
Automation Team
</body>
</html>
"""

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipient_emails)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, recipient_emails, msg.as_string())

        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
else:
    print("No files were deleted, so no email was sent.")
