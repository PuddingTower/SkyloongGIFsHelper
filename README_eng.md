[中文版](README.md) | [English Version](README_eng.md)

# GIF Cropper User Manual

Welcome to GIF Cropper! This application is designed to help users easily crop and adjust the resolution of GIF animations. This document will guide you through installation, usage, and troubleshooting.

## Table of Contents

1. [Introduction](#introduction)  
2. [System Requirements](#system-requirements)  
3. [Installation Guide](#installation-guide)  
4. [Usage Instructions](#usage-instructions)  
   - [Launching the Program](#launching-the-program)  
   - [Setting the Resolution](#setting-the-resolution)  
   - [Selecting GIF File or Directory](#selecting-gif-file-or-directory)  
   - [Cropping the GIF](#cropping-the-gif)  
   - [Saving the Cropped GIF](#saving-the-cropped-gif)  
5. [Configuration File](#configuration-file)  
6. [High DPI Support](#high-dpi-support)  
7. [FAQ](#faq)  

---

## Introduction

GIF Cropper is a desktop application developed with PyQt5 and Pillow, designed to provide users with an easy way to crop and adjust the resolution of GIF animations. Users can select a single GIF file or batch process an entire directory through an intuitive graphical interface, cropping and saving them at the specified resolution.

## System Requirements

- **Operating System:** Windows, macOS, or Linux  
- **Python Version:** Python 3.6 or later  
- **Dependencies:**  
  - PyQt5  
  - Pillow  

## Installation Guide

### 1. Install Python  
If you haven't installed Python yet, visit the [Python official website](https://www.python.org/downloads/) and download the latest version.

### 2. Install Dependencies  
Open a terminal (Command Prompt or PowerShell for Windows users) and run:

```sh
pip install PyQt5 Pillow
```

### 3. Dowload the GIF Cropper Source Code
Save the program code to a local directory, e.g., gif_cropper_eng.py

### 4. Run the Program
Navigate to the program directory in the terminal and run:
```sh
python gif_cropper_eng.py
```


## Usage Instructions

### Launching the Program
Double-click `gif_cropper_eng.py`, or launch it via the terminal using the command above. The main window "GIF Cropper" will appear.

### Setting the Resolution

- **Manual Input:**
  - Enter the desired resolution in the "Enter resolution (Width x Height)" field in the format `widthxheight` (e.g., `640x480`).

- **Quick Buttons:**
  - Click the "320x240" button to set the resolution to 320x240.
  - Click the "240x135" button to set the resolution to 240x135.

- **Saving the Resolution:**
  - The set resolution is automatically saved in the `config.txt` file and will be loaded the next time the program starts.

### Selecting GIF File or Directory

- **Select a Single GIF File:**
  - Click the "Select GIF" button to open a file selection dialog.
  - Browse and select the GIF file you want to crop.

- **Select a GIF Directory:**
  - Click the "Select GIF Directory" button to open a directory selection dialog.
  - Choose a folder containing multiple GIF files, and the program will process all GIFs in that directory.

### Cropping the GIF

- **Display Image:**
  - After selecting a GIF, the program will display the first frame.

- **Draw Crop Area:**
  - Click and drag with the left mouse button to draw a crop rectangle.
  - The crop area will automatically adjust to maintain the resolution ratio.

- **Adjust Crop Area:**
  - You can redraw the crop area or modify the resolution and redraw it.

### Saving the Cropped GIF

- **Confirm Crop:**
  - Once the crop area is set, click the "Confirm and Save" button.

- **Save File:**
  - The program will crop and adjust every frame of the GIF and generate a new file with `_cropped` appended to the original filename (e.g., `example_cropped.gif`).

- **Completion Prompt:**
  - A message box will appear showing the save path of the new file.

## Usage Instructions

### Launching the Program
Double-click `gif_cropper.py`, or launch it via the terminal using the command above. The main window "GIF Cropper" will appear.

### Setting the Resolution

- **Manual Input:**
  - Enter the desired resolution in the "Enter resolution (Width x Height)" field in the format `widthxheight` (e.g., `640x480`).

- **Quick Buttons:**
  - Click the "320x240" button to set the resolution to 320x240.
  - Click the "240x135" button to set the resolution to 240x135.

- **Saving the Resolution:**
  - The set resolution is automatically saved in the `config.txt` file and will be loaded the next time the program starts.

### Selecting GIF File or Directory

- **Select a Single GIF File:**
  - Click the "Select GIF" button to open a file selection dialog.
  - Browse and select the GIF file you want to crop.

- **Select a GIF Directory:**
  - Click the "Select GIF Directory" button to open a directory selection dialog.
  - Choose a folder containing multiple GIF files, and the program will process all GIFs in that directory.

### Cropping the GIF

- **Display Image:**
  - After selecting a GIF, the program will display the first frame.

- **Draw Crop Area:**
  - Click and drag with the left mouse button to draw a crop rectangle.
  - The crop area will automatically adjust to maintain the resolution ratio.

- **Adjust Crop Area:**
  - You can redraw the crop area or modify the resolution and redraw it.

### Saving the Cropped GIF

- **Confirm Crop:**
  - Once the crop area is set, click the "Confirm and Save" button.

- **Save File:**
  - The program will crop and adjust every frame of the GIF and generate a new file with `_cropped` appended to the original filename (e.g., `example_cropped.gif`).

- **Completion Prompt:**
  - A message box will appear showing the save path of the new file.

## Configuration File

The program uses a `config.txt` file to save the user-set resolution. The file format is `widthxheight` (e.g., `320x240`). If `config.txt` does not exist or has an invalid format, the program defaults to `320x240`.

### Manually Editing Configuration File

You can manually edit `config.txt` to change the default resolution. Ensure the format is correct, e.g.:
```sh
640x480
```

## High DPI Support

The program includes High DPI support to ensure clear display on high-resolution screens. These settings are configured automatically when the program starts and require no manual adjustment.

## FAQ

1. **The program won't start or shows an error**

   **Solution:**
   - Ensure you have installed the correct Python version (Python 3.6+ recommended).
   - Ensure all dependencies (`PyQt5` and `Pillow`) are installed.
   - Check if the program file is complete and correctly named `gif_cropper_eng.py`.

2. **Unable to load GIF file**

   **Solution:**
   - Make sure the selected file is a valid GIF.
   - Check if the file is corrupted by opening it with another viewer.

3. **Cropped GIF quality is poor**

   **Solution:**
   - Ensure the target resolution is not too low.
   - Choose an appropriate resolution to balance file size and quality.

4. **Unable to save the cropped GIF**

   **Solution:**
   - Ensure the target folder has write permissions.
   - Check if there is enough disk space.