# lowend-llm
Chat with your own bot! Avoid giving your data away to cloud entities.

NOTE: The web interface does not work in this version.

## Install
- install Python 3 or later
- install Ollama
- install git
- Open a Terminal and enter:
```bash
ollama pull deepseek-r1
git clone https://github.com/Hierosoft/lowend-llm.git lowend-llm
cd lowend-llm
# Make sure you are in the directory before continuing.
python -m venv .venv
```

If you have linux, you can avoid compiling many things (Yes, sometimes
Python modules are compiled from C, Cython, Pyrex, etc.) if you simply
install your distro's package for the requirements instead of using
requirements.txt. Example package names (remove the "3" in package names
if using an Arch-based distro):
- `python3-requests python3-flask`
- Then use Python's pip to install the rest:
  `.venv/bin/pip install ollama jsonify`


Otherwise, if using Windows, open a Terminal (called PowerShell on Windows 10 or earlier):
```PowerShell
.\.venv\Scripts\pip install -r requirements.txt
```
or if using Linux/macOS and you don't want to do it the easy way with precompiled packages:
```bash
.venv/bin/pip install -r requirements.txt
```

## Use
- Open a terminal and enter:
```bash
cd lowend-llm
# Make sure you are in the directory before continuing.
```

When using the local-chat command, replace
"filename or question" in the example with your question or a filename
containing only your full question such as a multiline question.

Then if using Linux or macOS:
```bash
./local-chat filename or question
```

Or in Windows Terminal:
```PowerShell
.\local-chat.ps1 filename or question
```
