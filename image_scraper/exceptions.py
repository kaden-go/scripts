""" 
Custom exceptions 
"""

class UrlNotValidError(Exception):
	"""
	Exception raised if invalid URL is passed to the script
	"""
	
	def __init__(self, message="URL not valid"):
		self.message = message
		super().__init__(self.message)

	def __str__(self):
		return f'{self.message}'	

