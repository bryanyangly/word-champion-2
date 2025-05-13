uv pip install pyinstaller
pyinstaller --onefile --noconsole main.py --exclude-module input
Copy-Item -Path "input" -Destination "dist/data" -Recurse
