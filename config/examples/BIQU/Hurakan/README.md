# Biqu Hurakan Configuration

*Note:* Early Hurakan printers have a raised bed power switch, so enable (uncomment) `#define PROBING_MARGIN_BACK` in `Configuration_adv.h` to prevent the hotend from potentially colliding with the switch assembly while probing.

The Biqu Hurakan ships with a BigTreeTech Manta M4P motherboard which includes an integrated BigTreeTech CB1 single board computer running Klipper. See below for instructions on how to update the CB1 to run OctoPrint.

# Table of Contents

- [Update Hurakan CB1 Image Defaults](#update-hurakan-cb1-image-defaults)
  * [SSH into to the CB1](#ssh-into-to-the-cb1)
  * [Update Timezone](#update-timezone)
  * [Update NTP Server](#update-ntp-server)
    + [Reboot](#reboot)
  * [SSH into to the CB1](#ssh-into-to-the-cb1-1)
  * [Update APT](#update-apt)
- [Install OctoPrint via KIAUH](#install-octoprint-via-kiauh)
  * [Update PIP](#update-pip)
    + [Reboot](#reboot-1)
  * [Access OctoPrint via Web Browser](#access-octoprint-via-web-browser)

# Update Hurakan CB1 Image Defaults

⚠️ Start with the latest `Hurakan_Debian11_Mainsail_kernel5.16_YYYYMMDD.img.xz` image from [bigtreetech/CB1/releases](https://github.com/bigtreetech/CB1/releases). ⚠️

## SSH into to the CB1

```shell
ssh biqu@<ip address>
```
Password: `biqu`

## Update Timezone

*See [Wikipedia - List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) or run `timedatectl list-timezones` for list of valid time zone names. `America/Los_Angeles` is used as an example below:*

```shell
sudo timedatectl set-timezone America/Los_Angeles
```

## Update NTP Server

```shell
sudo nano /etc/scripts/init.sh
```

<img width="843" alt="image" src="https://user-images.githubusercontent.com/13375512/202753004-aebf01c5-4110-4598-9f28-fbaa82afc320.png">

Change:
`# sudo ntpdate stdtime.gov.hk`

To:
`# sudo ntpdate pool.ntp.org`

Press `CTRL`+`X` to exit

Press `Y` to save

### Reboot

```shell
sudo reboot
```

## SSH into to the CB1

```shell
ssh biqu@<ip address>
```
Password: `biqu`

## Update APT

```shell
sudo apt update

sudo apt upgrade
```

# Install OctoPrint via KIAUH

```shell
cd ~

git clone https://github.com/th33xitus/kiauh.git

./kiauh/kiauh.sh
```

*Note: Klipper, Moonraker, Mainsail, and KlipperScreen come preinstalled on the Hurakan image.*

Type 1 to install an app:

<img width="403" alt="image" src="https://user-images.githubusercontent.com/13375512/201934192-eb1ebdb4-bdcd-4b68-b5e7-2c794dc5966a.png">

Type 6 to install OctoPrint:

<img width="402" alt="image" src="https://user-images.githubusercontent.com/13375512/201934496-c55a04dc-37e9-4691-b29c-a4c60f9d669c.png">

## Update PIP

```shell
/home/biqu/.KlipperScreen-env/bin/python -m pip install --upgrade pip
```

### Reboot

```shell
sudo reboot
```

## Access OctoPrint via Web Browser

OctoPrint is now running at `<ip address>:5000`

After running the first time setup wizard, select `/dev/ttyACM0` as the serial port.

## Enable the `shutdown` Action Command in OctoPrint

To enable a graceful shutdown of OctoPrint from the LCD, open OctoPrint in your browser and go to Settings -> Serial Connection -> Firmware & protocol and scroll down to Action commands. Tick the "Enable the `shutdown` action command" box and reboot OctoPrint for the feature to be enabled.

<img width="691" alt="image" src="https://user-images.githubusercontent.com/13375512/205521020-1b1e64de-7326-4019-9bde-5ed05450e468.png">
