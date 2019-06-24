from gopro7 import GoPro7Client, PrimaryMode, PhotoSubMode, MultiShotSubMode, VideoSubMode
import logging
import time

gopro = GoPro7Client()
gopro.pair()

print('status:', gopro.status())

## Take Photo
# mode_result = gopro.set_mode(mode=PrimaryMode.PHOTO, sub_mode=PhotoSubMode.NIGHT)
# logging.info('set photo mode: %s', mode_result)
# take_photo_result = gopro.take_photo()
# logging.info('take_photo_result: %s', take_photo_result)

## Multi-shot
mode_result = gopro.set_mode(mode=PrimaryMode.MULTI_SHOT, sub_mode=MultiShotSubMode.BURST)
logging.info('set photo mode: %s', mode_result)
multi_shot_result = gopro.take_photo()
logging.info('multi_shot_result: %s', multi_shot_result)

## Video
# mode_result = gopro.set_mode(mode=PrimaryMode.VIDEO, sub_mode=VideoSubMode.LOOPING)
# logging.info('set video mode: %s', mode_result)
# gopro.start_video()
# time.sleep(5)
# gopro.stop_video()


