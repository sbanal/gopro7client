import urllib.request
import logging
from enum import Enum


class PrimaryMode(Enum):
	VIDEO = 0
	PHOTO = 1
	MULTI_SHOT = 2


class GoPro7Client:

	def __init__(self, url = 'http://10.5.5.9/gp/gpControl', log=True, log_file=None, timeout=60):
		self.url = url
		if log is True:
			logging.basicConfig(filename=log_file, format='%(asctime)s %(levelname)s: %(message)s', 
				datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)

	def _send_http_request(self, main_command, command, uri=None, **kwargs):
		
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
		with urllib.request.urlopen(command_url) as response:
   			return response.read()

	def status(self):
		return self._send_http_request(main_command='status', command=None)

	def set_primary_mode(self, mode):
		if mode not in PrimaryMode:
			raise ValueError('Invalid mode {}. Supported values are defined in enum PrimaryMode.'.format(mode))
		return self._send_http_request(main_command='command', command='mode', uri=None, p=mode.value)

	def take_photo(self):
		return self._send_http_request(main_command='command', command='shutter', uri=None, p=1)

	def start_video(self):
		return self._send_http_request(main_command='command', command='shutter', uri=None, p=1)
	
	def stop_video(self):
		return self._send_http_request(main_command='command', command='shutter', uri=None, p=0)




