## Loud House
**Loud House is a simple python program that takes control over a Google device's volume and media player. This program was originally tested on a Google Home Mini.**

Many thanks to this library: https://github.com/home-assistant-libs/pychromecast

# The What
The most annoying thing you can do ever. Welcome to Loud House. This simple python program(feel free to read), will simple play a given mp3 file on a specified Google Home.
Pretty simple right? That's the goal! The IP address of your Google Home can be found in the Google Home app, if you don't know where, then **google it.**
Alternativly, you can do a pingsweep for a device that has the following open:
```
8008/tcp  open  http
8009/tcp  open  ajp13
8443/tcp  open  https-alt
9000/tcp  open  cslistener
10001/tcp open  scp-config
```
These daemons are what you can usually find open on a home.
If you are interested in more IOT security stuff involving the Google Home, you need to check out this great resource.
https://www.theregister.com/2018/10/31/google_home_api/
https://www.digitaltrends.com/home/google-home-hub-hack/

# The How
This exploit uses a library meant to aid people in commuticating with their Google Chromecast.
As you are about to see, this can be used other ways.

The program is simple and frankly your better off just experimenting with it yourself.
If you haven't done so already, ```chmod +x ./setup.sh; ./setup.sh```
The setup script only installs dependancies nothing more.

The mp3 file must be hosted, do not specify a file path. You can host an mp3 on your own webserver or via a file hoster such as filebin.net.

Please note this exploit is not recursive by default (a verbal stop command will stop your audio.) To fix this and be recursive, specify the **-r** argument. This will play your mp3 anytime it detects its not playing.
The verbose argument outputs the status of the media device at the time the mp3 is playing. Be warned it is messy.
See **-h** for a full list of options.
![Action!](https://i.ibb.co/bKNbBWk/image.png "usuage")

# In Action
![Action!](https://i.ibb.co/vLTYSwL/Screenshot-at-2020-10-29-22-06-07.png "example")


I am not responsible or liable for any misuse of the exploit; it was made solely for educational purposes.
