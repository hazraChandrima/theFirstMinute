# theFirstMinute

So that you don't have to stay up till the last minute....<br/>
...*a day before*

saves you from those stupid 12 am birthday wishes on WhatsApp, while you can sleep in peace.
We all know it's a pain in the butt to stay awake just for that, especially for someone you don't really care about...🥱

## 📜 Contents  

1. [What It Does](#-what-it-does)  
2. [Requirements](#-requirements)
3. [Prerequisites](#-prerequisites) 
4. [Setup and Installation](#%EF%B8%8F-setup-and-installation)
5. [Test the Script](#%EF%B8%8F-test-the-script)
6. [Schedule It with Task Scheduler](#-schedule-it-with-task-scheduler)
7. [How It Works](#-how-it-works)  
8. [Troubleshooting](#%EF%B8%8F-troubleshooting)  
9. [Contribute](#-contribute)  


<br/>

## ✨ What it does

This script automates sending a birthday wish to someone via the **WhatsApp Desktop App** on Windows, using **PyAutoGUI** for automation and **Task Scheduler** to run the script automatically at 12 am.


## ✅ Prerequisites

- A Windows machine (updates for Linux coming soon)
- Python installed on your system (3.8 or higher recommended).
- WhatsApp Desktop App installed on your Windows machine.
- Basic understanding of Task Scheduler on Windows.
- A comfortable sleep schedule


## 📝 Requirements

### Python Dependencies
Ensure you have Python installed on your system. The script uses the following libraries:
- **pyautogui** (for desktop automation)
- **time** (for time manipulation and delays)

---


## 🛠️ Setup and Installation

1. Clone the repo:
   ```bash
   git clone --depth=1 https://github.com/hazraChandrima/theFirstMinute.git
   cd theFirstMinute
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

4. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
5. Adjust Script Configuration:

   Edit the script file `/script.py` to configure your contact and message:
   ```python
   CONTACT_NAME = "Recipient's Name"
   MESSAGE = f"Wish you a very Happy Birthday dear {CONTACT_NAME}!!"
   ```
   > **Note: Ensure the contact name matches exactly how it appears in your WhatsApp Desktop.**

<br/>

## ⚙️ Test the Script

Run the script manually to test if it works:
   
   ```bash💡📜
   python adb_script.py
   ```


## 🕒 Schedule It with Task Scheduler

### Steps:

1. **Open Task Scheduler**  
   - Press `Win + S` and search for **Task Scheduler**.


2. **Create a Basic Task**  
   - Click on **Create Basic Task**.  
   - Name the task (e.g., `WhatsAppBirthdayAutomation`) and provide a short description.
   

3. **Set Trigger**  
   Choose **One Time** and set the start time to **12:00 AM** on the **day before the birthday**.


4. **Set Action**  
   - Select **Start a Program**.  
   - Fill in the following details:  

   - **Program/script:**  
     ```  
     C:\[path to venv]\Scripts\python.exe  
     ```  

   - **Add arguments:**  
     ```  
     C:\[path to theFirstMinute]\desktop_script.py  
     ```  

   - **Start in:**  
     ```  
     C:\[path to theFirstMinute]
     ```  


5. **Finish and Test**  
   - Save the task.  
   - Run the task manually in **Task Scheduler** to confirm it works. 
      > Note: Please don't test the script with the original birthday wish itself! gawd! 
   - The script will now run automatically at 12:00 AM on the day before the birthday.
   Copy code


---

## 🚀 How It Works

1. Opens the WhatsApp Desktop App using Windows Search.
2. Searches for the specified contact.
3. Sends the birthday message to the contact.
4. Allows you to sleep peacefully while the task is done automatically.


## 🛠️ Troubleshooting

If the script doesn't run as expected, it could possibly be due to:

1. If the script doesn’t click the right spots, recalibrate the screen coordinates or resolution scaling.
2. Make sure your screen resolution matches or adjust BASE_WIDTH and BASE_HEIGHT in the script.
3. Ensure WhatsApp Desktop is properly installed and linked to your account.


## 🧑‍💻 Contribute
Feel free to fork this repository and submit pull requests for:

- Adding features like multiple contacts, reminders, or more automation.
- Improving the accuracy of automation.
