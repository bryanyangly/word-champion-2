# Word Champion

Word Champion is an engaging game designed to test and enhance your vocabulary and image recognition skills. Players are presented with a series of images and must quickly associate the correct word with each image. The game challenges players to think fast and expand their vocabulary in a fun and interactive way.

## Windows

The game consists of three windows:

*   **Lobby Window:** This window allows you to select the level and countdown time before starting the game.
*   **Game Window:** In this window, you will be presented with an image. You can then choose to skip or pass the word associated with the image.
*   **Result Window:** This window displays your performance, showing the level you played, the time you used, and the number of words you passed and skipped.

## Build Instructions

To build the game into a single executable:

1.  Make sure you have Python installed.
2.  Run the `build.ps1` PowerShell script. This script will:
    *   Install PyInstaller using `uv pip install pyinstaller`.
    *   Build the executable using `pyinstaller --onefile --noconsole main.py --exclude-module input`. The `--noconsole` option hides the console window.
    *   Copy the 'input' folder to 'dist/data' so the game can access the images.

The resulting executable will be in the `dist` folder.

## Input Folder Structure

The `input` folder should contain subfolders for each level. Each level folder should contain the images for that level. For example:

```
input/
    level1/
        image1.jpg
        image2.png
    level2/
        image3.jpg
        image4.png
```
