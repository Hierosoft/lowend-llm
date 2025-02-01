# lowend-llm
Chat with your own bot! Avoid giving your data away to cloud entities.

Short version (command-line only chat):
- Install ollama (See [Install](#install), but only do step 1)
```
ollama pull deepseek-r1
ollama run deepseek-r1
```
- Start chatting! You don't even need this Python software to do that.
  You've done all the steps you need to do. This repo is here just to
  make offline "AI" chat easier (which is actually simply LLM, as in
  "large language model" and lacking of what is defined as
  intelligence). I want to encourage and empower privacy, whether by
  helping you use ollama or lowend-llm Python software. If you want
  additional features, see the rest of the [Install](#install) section.
- NOTE: As of 2025, Microsoft Office 365 is reportedly going to require
  Copilot. Avoid leaking confidential data by using this repo's setup
  instructions for your very own LLM instance if you need a chat bot,
  and an alternative office such as
  [LibreOffice](https://libreoffice.org) for making documents,
  spreadsheets, drawings, etc. That way you can be sure your data is
  only where you put it.
- WARNING: Even when running your own local chat bot, do not use the
  same chat session nor save your session (`/save`) if discussing
  confidential information. Do not save, and instead type `/bye` to
  exit, then run ollama again for discussing the next compartmentalized
  information. See Ollama's documentation to see if there are any other
  ways there may be data leakage in your version and update it if
  necessary.
- IANAL. See [license](LICENSE) for license including disclaimers.

## Known Issues
See
[github.com/Hierosoft/lowend-llm](https://github.com/Hierosoft/lowend-llm)
to see if your issue is known or to report an issue that is not yet
there. Also click "Closed" issues in case your version is older than the
current git release, in which case, if your issue is closed simply
update lowend-llm (`cd lowend-llm` then `git pull`)

## Install
1. Install Ollama from [ollama.com/download](https://ollama.com/download)
   - Linux:
     - `curl -fsSL https://ollama.com/install.sh | sh`
       or `snap install ollama`
     - `sudo systemctl start ollama --now`
2. Install Python 3 or later from [python.org](https://python.org)
   - Linux: use the Software icon (or `sudo apt install python3` on deb-based distros)
3. Install git from [git-scm.com/downloads](https://git-scm.com/downloads)
   - Linux: use the Software icon (or `sudo apt install git` on deb-based distros)
4. Open a Terminal (called PowerShell on Windows 10 or earlier) and enter:
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


Otherwise, if using Windows, open a Terminal (called PowerShell on
Windows 10 or earlier):
```PowerShell
.\.venv\Scripts\pip install -r requirements.txt
```
or if using Linux/macOS and you don't want to do it the easy way with
precompiled packages:
- Install your distro's C developer tools metapackage (such as `sudo apt
  install build-essential` on deb-based distros or `sudo dnf
  groupinstall "Development Tools"` on rpm-based distros), or manually
  install packages for the GNU toolchain.
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

When using the local-chat command, replace "filename or question" in the
example with your question or a filename containing only your full
question such as a multiline question that may include code etc.

If using Linux or macOS:
```bash
./local-chat filename or question
```

Or in Windows Terminal:
```PowerShell
.\local-chat.ps1 filename or question
```
