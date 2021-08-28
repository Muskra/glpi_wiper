import sys, os, configparser
from bin.data_delete import delete as delete
from bin.fetch import range_fetch as range_fetch

'''
	This function is the configuration parser of the program.
	It'll takes from the config.ini file the variables that are important to use, parse it.
	After that, it reads the other optionals options and makes the script work with it if needed.
'''
def main():
	# declare
	url = ""
	user_token = ""
	app_token = ""
	device = ""
	is_deleted = 0
	items_range = '0-10000'
	max_range = 0
	iterator = 0
	rest = 0
	wipe = False
	temp = items_range.split('-')
	range_list = []
	# configparser: declaration
	config = configparser.ConfigParser()
	# configparser: opening config file
	config.read('config.ini')
	# condition block: verifiying config file conformity before launch
	if 'url' not in config['Server']:
		print("<ConfigError> Required option: <url> is missing.")
		sys.exit(0)
	elif 'user_token' not in config['Server']:
		print("<ConfigError> Required option: <user_token> is missing.")
		sys.exit(0)
	elif 'app_token' not in config['Server']:
		print("<ConfigError> Required option: <app_token> is missing.")
		sys.exit(0)
	elif 'device' not in config['Object-Type']:
		print("<ConfigError> Required option: <device> is missing.")
		sys.exit(0)
	else:
		# parsing: server info to our variables
		url = config['Server']['url']
		user_token = config['Server']['user_token']
		app_token = config['Server']['app_token']
		# parsing: object-type into our variables
		device = config['Object-Type']['device']
		# parsing optional: is_deleted
		if 'is_deleted' in config['Options']:
			is_deleted = int(config['Options']['is_deleted'])
		# parsing optional: items_range
		if 'items_range' in config['Options']:
			items_range = str(config['Options']['items_range'])
			# redeclare temp value
			temp = items_range.split('-')
			# condition: verify if the value is not over 10000 because glpi can't handle that.
			if int(temp[1]) > 10000:
				print("<ConfigError> Optional: custom <items_range> option exceeded max value.")
				sys.exit(0)
		# parsing optional: max_range
		if 'max_range' in config['Options']:
			# i choose here to not go over 999999, try it at your will but i didn't even tried it.
			if int(config['Options']['max_range']) > 999999:
				print("<ConfigError> Optional: custom <max_range> option exceeded max value.")
				sys.exit(0)
			elif int(temp[1]) > int(config['Options']['max_range']):
				print("<ConfigError> Optional: conflict between <items_range> and <max_range> options.")
				sys.exit(0)
			else:
				# declare: values wich will be gave to our fetch function (not needed before so declared here).
				max_range = int(config['Options']['max_range'])
				iterator = int(max_range / int(temp[1]))
				rest = int(max_range % int(temp[1]))
				# call: fetch function
				range_list = range_fetch(int(temp[1]), max_range, iterator, rest)
		# printout configuration
		print("Configuration is:\nurl: {}\nuser_token: {}\napp_token: {}\ndevice: {}\nis_deleted: {}\nitems_range: {}\nmax_range: {}".format(url, user_token, app_token, device, is_deleted, items_range, max_range))
		# checking for the wipe parameter, prompt before run
		while True:
			if 'wipe' in config['Options'] and config['Options']['wipe'] == 'True':
				wipe = True
				print("\nThe option <wipe> is set to True. BE AWARE this will erase all objects from the <device> option you defined !!!")
				prompted = input("Are you sure to continue ? y/n\n$_ ")
				if prompted == "y" or prompted == "Y":
					# call: delete function, this will process tasks to GLPI
					delete(url, user_token, app_token, device, is_deleted, items_range, wipe, range_list)
					break
				elif prompted == "n" or prompted == "N":
					input("End of the program... Press 'Return' key to continue.")
					break
			else:
				# call: delete function, this will process tasks to GLPI
				delete(url, user_token, app_token, device, is_deleted, items_range, wipe, range_list)
				break

# call: main function
if __name__ == '__main__':
	main()