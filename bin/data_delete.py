import os, sys, requests
'''
	the delete function is where the requests work is made.
	here we initiate a session with the server.
	retrieve the item ids within the ranges that we added into our list.
	after that we send a DELETE request to the server with a maximum of 10000 ids.
	this last_request is made after each id retrieval from the server.
'''
def delete(url, user_token, app_token, device, is_deleted, items_range, wipe, range_list):
	# declare
	neg_range_length = -len(range_list)
	temp = 0
	all_ids = []
	# declare: file_path, session, headers
	init_session = url + "/apirest.php/initSession"
	headers = {'Content-Type':'application/json','Authorization':'user_token ' + user_token, 'App-Token': app_token}
	link = url + "/apirest.php/" + device + "/"
	# clear screen
	os.system("cls")
	try:
		# GET request: initiate session with glpi
		response = requests.get(init_session, headers = headers)
		# GET requests: grab a session token
		session_token = response.json().get("session_token")
		# generate a custom header with the given informations
		new_header = {'Content-Type':'application/json','Session-Token':session_token, 'App-Token': app_token}
		try:
			# opening requests session
			session = requests.Session()
			# updating the header
			session.headers.update(new_header)
			# checking if range_list from fetch function is empty or not
			if len(range_list) == 0:
				print("<DataError> There is no value to use.")
				sys.exit(0)
			elif len(range_list) != 0:
				# conditional loop to iterate the requests process
				while temp != neg_range_length:
					# increment -> 1
					temp -= 1
					# GET request: try to grab some things to check if we can speak to restAPI
					# if we can it will be used to send a DELETE request to the server within the items retrieved
					second_response = session.get(link + "?only_id=true&is_deleted=" + str(is_deleted) + "&range=" + str(range_list[temp]) + "&get_hateoas=false")
					# condition block: if there is no items to retrieve, we just quit the program
					if len(second_response.json()) == 0:
						input("There is no objects to delete.\nPress any key to quit...")
						break
					else:
						# create a dict with our data in it
						payload_dict = {'input': second_response.json(), 'force_purge': wipe}
						# printout
						print("Waiting for the server to process...")
						# DELETE request: this will delete the items from the list we precedently exported
						last_request = session.delete(link, json = payload_dict)
						# print out the answer informations
						print("\n{}\n".format(last_request))
						continue
		# exceptions management for the second try
		except requests.exceptions.HTTPError as errh:
			print(errh)
		except requests.ConnectionError as errc:
			print(errc)
		except requests.exceptions.TooManyRedirects as errT:
			print(errT)
		except requests.exceptions.Timeout as errt:
			print(errt)	
	# exceptions management for the first try
	except requests.exceptions.HTTPError as errh:
		print(errh)
	except requests.ConnectionError as errc:
		print(errc)
	except requests.exceptions.TooManyRedirects as errT:
		print(errT)
	except requests.exceptions.Timeout as errt:
		print(errt)