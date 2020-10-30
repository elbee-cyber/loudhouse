#!/usr/bin/python3
from termcolor import colored
import argparse,sys,time,os,pychromecast,pyfiglet
#Banner
print(colored("="*100,'yellow'))
print(colored("                @elbee_ez | Discord: J5B5ahP | This program uses the Pychromecast lib ",'yellow'))
print(colored(pyfiglet.figlet_format("                   Loud House"),'yellow'))
print(colored("="*100,'yellow'))

#args and checking
parser = argparse.ArgumentParser(description='Control the volume and play mp3s on a google cast device.')
parser.add_argument('-i','--ip',required=True,type=str,help='IP of google device.')
parser.add_argument('-s','--sound',type=str,required=True,metavar='mp3',help='Direct download link for mp3 file to play.')
parser.add_argument('-m','--magnitude',type=float,required=True,metavar='volume',help='Volume at which to play the mp3.')
parser.add_argument('-r','--recursive',action='store_true',help='Audio to be recursive in the event someone verbally issues a stop command.')
parser.add_argument('-v','--verbose',action='store_true',help='Be verbose.')
args = parser.parse_args()
if ".mp3" in args.sound and "http" in args.sound:
	pass
else:
	print(colored("%s is not a valid direct mp3 link!" % args.sound,'red'))
	sys.exit(1)
def validate_ip(s):
    a = s.split('.')
    if len(a) != 4 or "127.0.0.1" in s:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True
if validate_ip(args.ip):
	pass
else:
	print(colored("%s is an invalid IP!" % args.ip,'red'))
	sys.exit(1)
print('Will play %s on %s' % (args.sound,args.ip))

#program
try:
	device = pychromecast.Chromecast(args.ip)
except:
	print(colored("Could not connect to specified IP!",'red'))
	sys.exit(1)
print(args.ip+" is up!")
device.wait()
volume = device.status.volume_level
device.set_volume(args.magnitude)
mc = device.media_controller

def reoccur(mp3,mag):
	mc.play_media(mp3, 'audio/mp3')
	print(colored("Playing "+str(mp3)+" at a volume of "+str(mag), 'green'))
	time.sleep(5)
	check = str(mc.status); check = check.split("duration': ", 1)[1]; check = check.split(", \'stream_type", 1)[0]; check = float(check) 
	timeout = time.time() + check - 2
	while True:
		stat = str(mc.status)
		time.sleep(1)
		if time.time() + 2 > timeout:
			break

		if "PLAYING" in stat:
			if args.verbose:
				print(stat)
		else:
			print("Time left: "+str(timeout))
			timeout = time.time() + check - 2
			print(colored("Someone stopped the MP3! Putting it back on...",'blue'))
			device.set_volume(mag)
			mc.block_until_active()
			reoccur(mp3,mag)

if args.recursive:
	reoccur(args.sound, args.magnitude)
	time.sleep(5)
	print(colored("MP3 finished! Thanks for shopping with us!","green"))
	sys.exit(1)
else:
	mc.play_media(args.sound, 'audio/mp3')
	print(colored("Playing "+str(args.sound)+" at a volume of "+str(args.magnitude), 'green'))
	if args.verbose:
		foo = str(mc.status);
		print(foo)
	time.sleep(10)
	bar = str(mc.status); bar = bar.split("duration': ", 1)[1]; bar = bar.split(", \'stream_type", 1)[0]; bar = float(bar)
	time.sleep(bar)
	print(colored("MP3 finished! Thanks for shopping with us!","green"))
