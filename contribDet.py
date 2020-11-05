# importing all the necessary modules
import requests
import json


#arguments provided were organisation contributions url and the number of committees which user want to check
def get_contrib_detail(api_url_base_contrib, m):

	#assigning the base url as it is an open source and free api no need for authentication 
	api_url_base = api_url_base_contrib + '?sort=contributions&page=1&order=desc&per_page=' + str(m)
	
	#making a get request to the api
	response = requests.get(api_url_base)
	
	#check if the response we got was successful or not, if not return none
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None