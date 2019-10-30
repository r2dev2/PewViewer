# PewViewer

## Execution
To watch the latest video posted by the configured youtuber, enter the following command.

``./watchNewest.bash``

## Setup
### Debian
Use the following commands in the terminal.

``sudo apt install mpv youtube-dl``

``chmod +x watchNewest.bash``


### MacOS
Use the following commands in the terminal if you have installed Homebew
``brew cask install mpv``

``brew install youtube-dl``

``chmod +x watchNewest.bash``


### Configure youtuber
* Open watchNewest.bash in a text editor
  * In Debian, execute ''gedit watchNewest.bash''
  * In MacOS, execute ''open watchNewest.bash''
* Edit the link in line 2 to the link of your youtube channel
* Save and exit
