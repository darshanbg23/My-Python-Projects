# WhatsApp Message Scheduler

## Project Description
The **WhatsApp Message Scheduler** is a Python-based mini-project that allows users to schedule and send WhatsApp messages automatically at a specified date and time. Using the Twilio API for WhatsApp, this script simplifies the process of sending pre-planned messages to recipients, making it ideal for reminders, greetings, and notifications.

---

## Features
- **Schedule Messages**: Set a specific date and time to send a WhatsApp message.
- **User-Friendly Input**: Interactive prompts for recipient details and message content.
- **Automated Delivery**: Automatically sends the message at the scheduled time.
- **Error Handling**: Includes basic error handling to manage invalid inputs or API issues.

---

## How It Works
1. The user provides the recipient's name, WhatsApp number (with the country code), and the message content.
2. The user specifies the date and time for the message to be sent.
3. The script calculates the delay based on the current time and waits until the specified time.
4. At the scheduled time, the script uses the Twilio API to send the message to the recipient's WhatsApp.

---

## Prerequisites
Before running this project, ensure you have the following:
1. **Python 3.x** installed on your system.
2. A valid **Twilio account** with:
   - Account SID
   - Authentication Token
   - WhatsApp-enabled Twilio phone number.

---

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/whatsapp-message-scheduler.git
   cd whatsapp-message-scheduler
   ```

2. Install the required dependencies:
   ```bash
   pip install twilio
   ```

3. Update the placeholders in the script with your Twilio credentials:
   - Replace `YOUR_TWILIO_Account-SID` with your Account SID.
   - Replace `YOUR_TWILIO_Auth-Token` with your Auth Token.
   - Replace `Your-WhatsApp-enabled Twilio phone number` with your WhatsApp-enabled Twilio phone number.
   - Ensure these placeholders are updated in the following lines of the code:
     ```python
     account_sid = 'YOUR_TWILIO_Account-SID'
     auth_token = 'YOUR_TWILIO_Auth-Token'
     from_='whatsapp:Your-WhatsApp-enabled Twilio phone number'
     ```

---

## Usage
1. Run the script:
   ```bash
   python whatsapp_message_scheduler.py
   ```

2. Follow the on-screen prompts to:
   - Enter the recipient's name and WhatsApp number.
   - Specify the message content.
   - Provide the date and time for sending the message.

3. The script will confirm the scheduling and send the message automatically at the specified time.

---

## Example
```
Enter the recipient name: John
Enter the recipient Whatsapp number with country code (e.g., +91): +1234567890
Enter the message you want to send to John: Hello John! Don't forget about our meeting tomorrow.
Enter the date to send the message (YYYY-MM-DD): 2025-01-15
Enter the time to send the message (HH:MM in 24-hour format): 09:00
Message scheduled to be sent to John at 2025-01-15 09:00:00.
Message sent successfully! Message SID: SMXXXXXXXXXXXXXXXXX
```

---

## Notes
- Ensure your system's clock is accurate to avoid scheduling errors.
- Double-check the recipient's WhatsApp number, including the country code.
- Messages can only be sent to numbers that have contacted your Twilio WhatsApp sandbox (for development accounts).

---

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

## Acknowledgments
- [Twilio API for WhatsApp](https://www.twilio.com/whatsapp)
