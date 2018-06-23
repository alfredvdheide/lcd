Credit goes to:
* https://github.com/the-raspberry-pi-guy/lcd for LCD screen

* https://github.com/sivel/speedtest-cli for speedtest script




### Installation

>terminal instructions:
```
git clone <url of this repo>
cd speedtest-for-rpi-screen
sudo sh install.sh
```
>Then after the reboot go back to the folder
```
cd speedtest-for-rpi-screen
python3 start.py
```
  
 
>Note: If your screen has any other amount of characters, e.g. 20 you can change this by going editting the value on line 21 of start.py
```
num_cols = 20
```
