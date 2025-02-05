
✅ Step 1: Clone the Repository

The user must first download the project from GitHub.

bash

git clone <your-repo-url>
Replace <your-repo-url> with your actual GitHub repository link.

Example:
bash

git clone https://github.com/yourusername/voicebot.git

Then, move into the project directory:

bash

cd voicebot

✅ Step 2: Create & Activate a Virtual Environment (Recommended)

To avoid dependency conflicts, it's best to use a virtual environment.

On macOS/Linux:
bash

python3 -m venv venv

source venv/bin/activate

On Windows (CMD):

bash

python -m venv venv

venv\Scripts\activate

✅ Step 3: Install Dependencies

Run:

bash

pip install -r requirements.txt

This installs all required Python libraries.

✅ Step 4: Install the Package Locally

Since we packaged the bot as an installable Python package, the user needs to install it:

bash

pip install .

This will allow running voicebot as a command.

✅ Step 5: Grant Accessibility Permissions (macOS Users Only)

Since the bot interacts with the screen, users need to enable accessibility permissions.

On macOS:

1️⃣ Go to System Settings → Privacy & Security → Accessibility.


2️⃣ Enable permissions for Terminal (or the app running the bot).

3️⃣ Restart the terminal.

✅ Step 6: Run the VoiceBot
Once installed, users can run the bot using:
bash
voicebot
Alternatively, if running from the Python file directly:

bash

python3 -m voicebot.voice_bot
🎉 Done!
Your bot is now ready for use on any computer with just a few commands.



Example Voice Commands:
"Click Save" → Clicks the "Save" button
"Scroll down" → Scrolls the page down
"Switch tab" → Switches to the next tab
"Close window" → Closes the active window
"Go back" → Navigates back (browser)
"Open new tab" → Opens a new browser tab
🛠️ Development & Contribution
Fork the repository
Create a new branch:
bash
Copy
Edit
git checkout -b feature-new-feature
Commit your changes:
bash
Copy
Edit
git commit -m "Added new feature"
Push the branch:
bash
Copy
Edit
git push origin feature-new-feature
