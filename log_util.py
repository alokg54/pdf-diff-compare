"""
Module to configure logging

"""
import os
import logging
import datetime


def configure_logger():
	"""
	Method to generate log file

	:return: ``log handler``
	"""
	try:
		# Create and configure logger
		log_path = os.path.join(os.getcwd(), 'Log')
		if not os.path.exists(log_path):
			os.mkdir(log_path)
		today = datetime.date.today()
		date_time = datetime.datetime.now().strftime("%Y-%m-%d_%I_%M_%p")
		# TODO change path join to os.path.join method call
		if not os.path.exists(f'{log_path}\\{today}'):
			os.mkdir(f'{log_path}\\{today}')
		file_name = f'{log_path}\\{today}\\{date_time}.log'
		logging.basicConfig(
			level=logging.DEBUG,
			format="%(asctime)s [%(levelname)s] %(message)s",
			handlers=[logging.FileHandler(file_name), logging.StreamHandler()])
		# Creating an object
		log = logging.getLogger()
		return log
	except Exception as exp:
		print("Failed to create logger: ", exp)
