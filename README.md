# lowend-llm
Chat with your own bot! Avoid giving your data away to cloud entities.

NOTE: The web interface does not work in this version (The webAPI on port 5000 and webfrontend-cli scripts work, but the frontend on port 8080 does not).

## Install
- install Python 3 or later from [python.org](https://python.org)
  - Linux: use the Software icon (or `sudo apt install python3` on deb-based distros)
- install Ollama from [ollama.com/download](https://ollama.com/download)
  - Linux:
    - `curl -fsSL https://ollama.com/install.sh | sh`
      or `snap install ollama`
    - `sudo systemctl start ollama --now`
- install git from [git-scm.com/downloads](https://git-scm.com/downloads)
  - Linux: use the Software icon (or `sudo apt install git` on deb-based distros)
- Open a Terminal (called PowerShell on Windows 10 or earlier) and enter:
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
- Install your distro's C developer tools metapackage (such as `sudo apt install build-essential` on deb-based distros or `sudo dnf groupinstall "Development Tools"` on rpm-based distros), or manually install packages for the GNU toolchain.
- Go to a Terminal and run:
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
