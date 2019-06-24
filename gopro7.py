import urllib.request
import logging
from enum import Enum
from urllib.error import HTTPError


class PrimaryMode(Enum):
	VIDEO = 0
	PHOTO = 1
	MULTI_SHOT = 2

class PhotoSubMode(Enum):
	DEFAULT = 1
	NIGHT = 2

class MultiShotSubMode(Enum):
	BURST = 0
	TIMELAPSE = 1
	NIGHTLAPSE = 2

class VideoSubMode(Enum):
	DEFAULT = 0
	TIMELAPSE_VIDEO = 1
	VIDEO_PHOTO = 2
	LOOPING = 3
	TIME_WARP = 4


class GoPro7Client:

	def __init__(self, url = 'http://10.5.5.9/gp/gpControl', log=True, log_file=None, timeout=60):
		self.url = url
		if log is True:
			logging.basicConfig(filename=log_file, format='%(asctime)s %(levelname)s: %(message)s', 
				datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)

	def _send_http_request(self, main_command, command=None, uri=None, **kwargs):
		
		command_url = '{}/{}'.format(self.url, main_command)
		
		if command:
			command_url += '/' + command
		
		if uri is not None and len(uri) > 0:
			command_url += '/' + uri
		
		if len(kwargs) > 0:
			params = []
			for k, v in kwargs.items():
				params.append('{}={}'.format(k, v))
			command_url += '?' + '&'.join(params)

		logging.info('url: %s', command_url)
		try:
			with urllib.request.urlopen(command_url) as response:
	   			return response.read()
		except HTTPError as e:
			logging.error('HTTP error: %s, msg: %s', command_url, e)
			raise e
		
	def pair(self):
		return self._send_http_request(main_command='command', command='wireless', uri='pair/complete', 
			success=1, deviceName='DESKTOP')

	def status(self):
		return self._send_http_request(main_command='status', command=None)

	def set_boot_mode(self, mode):
		if mode not in PrimaryMode:
			raise ValueError('Invalid mode {}. Supported values are defined in enum PrimaryMode.'.format(mode))
		return self._send_http_request(main_command='setting', uri='53/{}'.format(mode.value))

	def set_mode(self, mode, sub_mode=None):
		
		if mode not in PrimaryMode:
			raise ValueError('Invalid mode {}. Supported values are defined in enum PrimaryMode.'.format(mode))
		if mode == PrimaryMode.PHOTO and sub_mode not in PhotoSubMode:
			raise ValueError('Invalid photo sub mode {}. Supported values are defined in enum PhotoSubMode.'.format(sub_mode))	
		if mode == PrimaryMode.MULTI_SHOT and sub_mode not in MultiShotSubMode:
			raise ValueError('Invalid multi-shot sub mode {}. Supported values are defined in enum MultiShotSubMode.'.format(sub_mode))	
		if mode == PrimaryMode.VIDEO and sub_mode not in VideoSubMode:
			raise ValueError('Invalid video sub mode {}. Supported values are defined in enum VideoSubMode.'.format(sub_mode))	
	
		if isinstance(mode, Enum):
			mode_value = mode.value
		if isinstance(sub_mode, Enum):	
			sub_mode_value = sub_mode.value

		if sub_mode:
			return self._send_http_request(main_command='command', command='sub_mode', uri=None, mode=mode_value, sub_mode=sub_mode_value)
		else:
			return self._send_http_request(main_command='command', command='mode', uri=None, p=mode_value)

	def take_photo(self):
		return self._send_http_request(main_command='command', command='shutter', uri=None, p=1)

	def start_video(self):
		return self._send_http_request(main_command='command', command='shutter', uri=None, p=1)
	
	def stop_video(self):
		return self._send_http_request(main_command='command', command='shutter', uri=None, p=0)
