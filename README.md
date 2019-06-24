
# GoPro 7 Python Clien

Command reference found here https://github.com/KonradIT/goprowifihack/blob/master/HERO7/HERO7-Commands.md

## Setup

1. Enable Wireless Connection in GoPro7 Device (click ON) > Select GoPro App.
1. Connect your machine to the GoPro7 Wi-Fi and enter password provided in Client Info of device.
1. Connect and manage the GoPro7 device using the client API.

## Basic Usage
```		
gopro = GoPro7Client(log_file=None)
print('status:', gopro.status())
logging.info('set photo mode:', gopro.set_primary_mode(mode=PrimaryMode.PHOTO))
logging.info('take photo:', gopro.take_photo())
```
