# importing all the necessary modules
import requests
import json


#arguments provided were organisation name and the number of most popular repositories which user want to check
def top_repo(orgName, repoCount):

	#assigning the base url as it is an open source and free api no need for authentication 
	api_url_base = 'https://api.github.com/search/repositories?q=org:' + orgName + '&order=desc&type=fork&per_page=' + str(repoCount)
	
	#making a get request to the api
	response = requests.get(api_url_base)

	#check if the response we got was successful or not, if not return none
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None