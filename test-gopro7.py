from gopro7 import GoPro7Client		

gopro = GoPro7Client()
print('status:', gopro.status())
logging.info('set photo mode:', gopro.set_primary_mode(mode=PrimaryMode.PHOTO))
logging.info('take photo:', gopro.take_photo())
