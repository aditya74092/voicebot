✅ Step 1: Clone the Repository
The user must first download the project from GitHub.

bash
Copy
Edit
git clone <your-repo-url>
Replace <your-repo-url> with your actual GitHub repository link.
Example:

bash
Copy
Edit
git clone https://github.com/yourusername/voicebot.git
Then, move into the project directory:

bash
Copy
Edit
cd voicebot
✅ Step 2: Create & Activate a Virtual Environment (Recommended)
To avoid dependency conflicts, it's best to use a virtual environment.

On macOS/Linux:
bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
On Windows (CMD):
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
✅ Step 3: Install Dependencies
Run:

bash
Copy
Edit
pip install -r requirements.txt
This installs all required Python libraries.

✅ Step 4: Install the Package Locally
Since we packaged the bot as an installable Python package, the user needs to install it:

bash
Copy
Edit
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
Copy
Edit
voicebot
Alternatively, if running from the Python file directly:

bash
Copy
Edit
python3 -m voicebot.voice_bot
🎉 Done!
Your bot is now ready for use on any computer with just a few commands.
