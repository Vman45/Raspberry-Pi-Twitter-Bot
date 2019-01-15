# How to Setup a Raspberry Pi

## Table of Contents
[Step 0: Hardware Prerequisites](https://gist.github.com/Raymo111/3981668f8055d4d74ff9e7afb5471756#step-0-hardware-prerequisites)  \
[Step 1: Flash Your MicroSD Card](https://gist.github.com/Raymo111/3981668f8055d4d74ff9e7afb5471756#step-1-flash-your-microsd-card)  \
[Step 2: Configuring Your Pi](https://gist.github.com/Raymo111/3981668f8055d4d74ff9e7afb5471756#step-2-configuring-your-pi)  \
[Step 3: Customizing Your Pi](https://gist.github.com/Raymo111/3981668f8055d4d74ff9e7afb5471756#step-3-customizing-your-pi)  \
[Step 4: Step 4: Setup SSH](https://gist.github.com/Raymo111/3981668f8055d4d74ff9e7afb5471756#step-4-setup-ssh)

## Step 0: Hardware Prerequisites
You will need the following prerequisites:

1. A Raspberry Pi. I'm using a Pi3 Model B that comes with built-in bluetooth, WiFi, 4 USB ports, HDMI, audio jack, and a standard Android Power Outlet.

2. A microSD card to host the Pi's OS on. You may need an adapter if your computer doesn't support just plugging in MicroSD Cards.

3. A Computer to flash your MicroSD Card from and read this tutorial on.

4. Keyboard, Screen, HDMI cable, Ethernet cable, standard Android power cable.
I'll assume you have the hardware above, so let's get started.

## Step 1: Flash Your MicroSD Card

1. Plug your MicroSD Card into your computer.

2. Download and install [Etcher](https://www.balena.io/etcher/).

3. Download and unzip [Raspbian Stretch Lite](https://downloads.raspberrypi.org/raspbian_lite_latest). This is a command-line based, no-desktop very-lightweight version of Raspbian. It should download relatively fast, as it is only 351MB (for the November 2018 Version)

4. Open Etcher and choose the .ISO file you've unzipped containing your Raspbian OS, and choose your MicroSD Card. Click **Flash**, and wait for it to finish. You may get several popups from Explorer if you're on Windows, but you can just ignore them.

5. **Eject** and remove your MicroSD Card from your computer.

6. **Make sure your Pi is unplugged**. Insert the MicroSD Card you just flashed into your Pi.

7. Connect a keyboard, screen (via the HDMI port), and ethernet cable to your Pi. Plug the Pi's power cable in, and it should boot up automatically.

## Step 2: Configuring Your Pi

1. When you see `raspberrypi login:` and a blinking cursor at the bottom of your screen, type in
```
pi
```
for the login and then hit enter. The default password is
```
raspberry
```
We'll change it in a minute.

2. Type in
```
sudo apt update
```
This command updates all the sources that Raspbian pulls updates from. `apt` is a package manager. `sudo` means **super-used do**, meaning that you get elevated priviledges when you run the command.
You might have seen `apt-get`, but `apt` is newer and more user-friendly. Wait for the command to finish.

3. When you see `pi@raspberrypi:~ $` again, this means that the command you've executed has finished. Go ahead and type
```
sudo apt full-upgrade
```
Enter
```
y
```
when prompted. This may take a while, but do watch the progress bar on the bottom of your screen.

4. When your Pi has finished updating, do
```
sudo apt autoremove && sudo apt clean
```
This removes all unnecessary packages and saves you memory. The `&&` joins multiple lines of commands together so you only need to type one line.

5. Type
```
sudo raspi-config
```
This gets you into a blue graphical screen where you can use the arrow keys to choose and enter to select different options. Use the arrow keys to select `8 Update` and hit enter to update the configuration tool.

6. Wait for a few seconds, then scroll down to `4. Localisation Options` and enter. Hit enter again to change your locale. Scroll down to `en_GB.UTF-8 UTF-8` and hit the spacebar to deselect it if there is an asterisk next to it. Keep scrolling down to `en_US.UTF-8 UTF-8` and hit the spacebar to select it. Then hit enter to finalize your changes. Use the down arrow to scroll down to en_US.UTF-8. Hit enter once and wait for it to go back to the `raspi-config` screen.

`4. Localisation Options` using your arrow keys and enter it again. This time, go to I2 with your down arrow, and change your timezone. Wait a moment, then use your arrow keys to select first your continent, then your city. I choose `Toronto`, under `America`. If you're in the US, you can go into `US` and choose your region if you want to.

7. Go back to `4. Localisation Options` again and choose the keyboard you're using. I'm using a `Dell USB Multimedia Keyboard`. CHoose yours and enter. Now if you're in the UK, you can select the keyboard layout you want. But if you're not, then go down to `other` and choose the keyboard layout that your keyboard has. I'm going to choose English (US). After you enter, choose the version of your keyboard layout. Choose the topmost one if you don't understand the rest of the options. Enter through the Alt-gr selection and the Compose Key selection. You won't need those for now.

8. Finally, go back into `4. Localisation Options` for the last time and select `I4 Change Wi-fi Country`. This is **very important** as you could be arrested for using the wrong wireless settings for your country. Select your country and enter. Hit enter again at the `<Ok>` message.

9. Now go down to `7. Advanced Options` and hit enter for `A1 Expand Filesystem`. This makes sure that our Pi takes up the whole SD Card and has space to install stuff.

10. The last thing we are going to configure is the password. Hit enter at `1 Change User Password`. Follow the onscreen instructions to change your password. Finally use the right arrow twice to go to `<Finish>`, and hit enter.

11. The last thing you need to do for configuration is reboot the Pi. Type in
```
reboot
```
and wait for the Pi to reboot.

## Step 3: Customizing Your Pi

1. When your Pi finishes rebooting, type
```
pi
```
as the login and whatever password you set earlier on to login.

2. You can remove the rainbow screen on boot with:
```
sudo nano /boot/config.txt
```
Nano is an easy to use text editor in Linux. Scroll down to the bottom with your arrow keys and add this line to the end of the text file:
```
disable_splash=1
```
Now Ctrl-x to exit nano and enter `y` to save.

3. Reboot, and you will not see the rainbow splash again. If you want to see it for some reason, then just go back into `/boot/config.txt` and comment out that line you just added (add a `#` in front of it).

4. You just used nano to edit a file. Now use nano to edit `/etc/motd`. Make sure you `sudo nano`, or you will not be able to write to the file. This is the message of the day, a message you see every time you login. Make sure your cursor is at the beginning of the file, then ctrl-^ and scroll down to the end of the file. Make sure you have selected the whole file, then ctrl-k. Now, the file should be blank. Type in whatever you want to see on login, then save and exit (ctrl-x, y to save)

5. Now type
```
exit
```
and login again. you should see your message on the screen!

## Step 4: Setup SSH

SSH is a way to access the command line of a computer remotely from another computer or device. First, you need to set a static ip address for your Pi.

1. Find your local IP address:
```
ip -4 addr show | grep global
```
You should see something like:
```
inet 192.168.2.37/24 brd 10.1.1.255 scope global eth0
```
**192.168.2.37** is my Pi's local IP address, the address for your Pi on your own internet. The **/24** is your network size, and it's most likely 24. Write your IP address down somewhere.

2. Find your router's local IP address:
```
ip route | grep default
```
You should see something like:
```
default via 192.168.2.1 dev eth0 src 192.168.2.37 metric 202
```
In my case, **192.168.2.1** is my router's IP. Write this down too.

3. Finally, write down the address of your DNS server, which is usually the same as your router's IP.
```
cat /etc/resolv.conf

# Generated by resolvconf
domain home
nameserver 192.168.2.1
nameserver XXX.XXX.XXX.XXX
```
The first nameserver is the dns server you need to worry about write that down if it is different from your Router's IP.

4. Next, edit `/etc/dhcpcd.conf` with:
```
sudo nano /etc/dhcpcd.conf
```
You should see A whole bunch of text. These are your dhcpcd configurations. Scroll down to **# Example satic IP configuration** and change the next few lines to:
```
# Example satic IP configuration
interface eth0
static ip_address=192.168.2.37/24
static routers=192.168.2.1
static domain_name_servers=192.168.2.1
```
Note that **192.168.2.37/24** is my Pi's IP address, yours would be different, the first **192.168.2.1** should be your router's IP address, and the second your DNS server's address.
Now Ctrl-x and then y to save and exit, and reboot your Pi. It should now have a static IP address.

5. Now enable ssh with:
```
sudo systemctl enable ssh
sudo systemctl start ssh
```
Then reboot your Pi. You don't need to login.

6. Now, on the computer from which you're reading this, open up terminal if you're on Linux or a Mac. If you're on Windows, press the windows key and type cmd, then enter.

7. In your terminal, type:
```
ssh pi@192.168.2.37
```
Again, **192.168.2.37** is your Pi's local IP address. Enter `yes` to continue connecting.

8. Enter your Pi's password. If you are connected to your Pi, you should now see the message you set for login (MOTD) and you should be able to use your Pi from your own computer! At this point, you can disconnect your keyboard and screen from your Pi if you want, and simply connect to your Pi from your computer.

*That's it, you've now successfully setup your Raspberry Pi!*