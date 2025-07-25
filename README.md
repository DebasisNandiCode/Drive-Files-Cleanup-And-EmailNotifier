Drive-Files-Cleanup-And-EmailNotifier

A Python automation script to delete .xlsx and .csv files from a shared drive folder and send an email notification with details of deleted files.

📌 Features
✅ Automatically scans a shared drive folder.
✅ Deletes all .xlsx and .csv files.
✅ Sends an HTML email with details of deleted files.
✅ Configurable SMTP settings (works with Office 365).

📂 Folder Structure
Drive-Files-Cleanup-And-EmailNotifier/
│── cleanup_email_notifier.py   # Main Python script
│── README.md                   # Documentation

🔧 Setup Instructions
1️⃣ Install Python (>=3.8)
Download and install Python from python.org.

2️⃣ Clone this repository
git clone https://github.com/<your-username>/Drive-Files-Cleanup-And-EmailNotifier.git
cd Drive-Files-Cleanup-And-EmailNotifier

3️⃣ Install dependencies
pip install -r requirements.txt

⚙️ Configuration
Edit the following variables in the script:
shareDrive_Path = "\\\\10.xxxx.xxx.14\\xxxxxxxxxx\\reporting\\reports"

smtp_username = "your-email@domain.com"
smtp_password = "your-app-password"
sender_email = "your-email@domain.com"
recipient_emails = ["recipient1@domain.com", "recipient2@domain.com"]
smtp_server = "smtp.office365.com"
smtp_port = 587

📧 Email Example
The email includes:
Deleted files count
Timestamp of deletion
Folder path
List of deleted files

👨‍💻 Author
Debasis Nandi

