# AnonCDN-BOT
a BOT automaticly uploading multiple files to AnonCDN controlling your browser. This tool uses Firefox driver.
<a href="https://www.youtube.com/watch?v=AlOpkwJYmnc&feature=youtu.be">
  Video Proof
</a>
![unknown](https://user-images.githubusercontent.com/48758770/159125833-05416cbb-f903-4e8e-af74-0b7ea75f5ae3.png)

# Requirements
- python3
- selenium (python framework)
- Windows
- Firefox (pre-installed)

# Installation
Download this repistory as a ZIP.<br>
Install <a href="https://www.python.org/downloads/">Python</a> on Windows 10.<br>
Install <a href="https://www.mozilla.org/nl/firefox/new/">FireFox Browser</a>
Open your CMD in the directory for 'AnonCDN-BOT' and then run the following commands:<br>
```shell
pip install selenium

// After that it is installed.
// Follow the usage instructions below
```

# Usage
First go ahead and put all your files you want to upload into the same directory as 'AnonCDN-BOT' (local DIRECTORY, SAME DIRECTORY).<br>
Then put your filenames into 'list.txt' like ``filename.zip``, ``filename.mp4`` and so on.<br>
Then follow the following commands:
                                                                                            
```shell
python anonup.py
```
All uploaded files to the CDN will be saved at ``uploads.txt``


