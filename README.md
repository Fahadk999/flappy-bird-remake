# Flappy Bird Remake
This is my remake of the flappy bird game
I previously made 2 similar games but was to complicated back then,

## How to run?
1. Pull the repo, and make sure you have uv installed, if not run
   - Powershell for **Windows**
     - `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
   - Mac or linux terminal for **Mac or Linux**
     - `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Then inside folder run `uv sync`
3. And finally run `uv run main.py`

## How to Build?
1. For **Mac and Linux**
   - `uv run pyinstaller --noconfirm --onedir --windowed --add-data "assets:assets" --add-data "src/database/schema.sql:src/database" main.py`
3. For **Windows**
   - `uv run pyinstaller --noconfirm --onedir --windowed --add-data "assets;assets" --add-data "src/database/schema.sql;src/database" main.py`

**Executable will be in `dist/build`, just run it `./main` or `main.exe`**

## Controls
[Space] to **Yump** :>

*Have fun*
