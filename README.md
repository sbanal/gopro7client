
# GoPro Hero 7 Python Client

Command reference found here https://github.com/KonradIT/goprowifihack/blob/master/HERO7/HERO7-Commands.md

## Setup

1. Enable Wireless Connection in GoPro7 Device (click ON) > Select GoPro App.
1. Connect your machine to the GoPro7 Wi-Fi and enter password provided in Client Info of device.
1. Connect and manage the GoPro7 device using the client API.

## Basic Usage

1. Create client and pair 
```
gopro = GoPro7Client()
gopro.pair()
```
1. Get status of device
```
print('status:', gopro.status())
```
1. Take photo
```
result = gopro.set_mode(mode=PrimaryMode.PHOTO, sub_mode=PhotoSubMode.NIGHT)
logging.info('set photo mode: %s', result)
result = gopro.take_photo()
logging.info('take_photo_result: %s', result)
```
