import json
import time
import requests

def top_repo(orgName, repoCount):
	api_url_base = 'https://api.github.com/search/repositories?q=user:' + orgName + '&order=desc&type=fork&per_page=' + str(repoCount)
	response = requests.get(api_url_base)
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None

def get_contrib_detail(api_url_base_contrib, m):
	api_url_base = api_url_base_contrib + '?sort=contributions&page=1&order=desc&per_page=' + str(m)
	response = requests.get(api_url_base)
	if response.status_code == 200:
		return json.loads(response.content.decode('utf-8'))
	else:
		return None

s = '1'
while(s=='1'):
	print("Enter the organisation name:")
	orgName = input()
	repoCount = 31
	while (repoCount>30):
		print("Enter the total number of top repositories you want to check: (limited to 30)")
		repoCount = int(input())
		if (repoCount>30):
			print("Entered value is not servicable")
		else:
			print("Loading...")
			details = top_repo(orgName,repoCount)
			print("Enter the number of top committees which you want to see:")
			m = int(input())
			if details is not None:
				print("Here are the repositories.")
				arr = details['items']
				for i in range(repoCount):
					print((i+1),"-> ", arr[i]['name'])
					print("Total number of forks", arr[i]['forks'])
					print("Details of top m or all the committees with their commit counts:")
					api_url_base_contrib = arr[i]["contributors_url"]
					contrib_detail = get_contrib_detail(api_url_base_contrib, m)
					if contrib_detail is not None:
						value = min(m,len(contrib_detail))
						for j in range(value):
							print("    ",(j+1), "-> ",contrib_detail[j]['login'])
							print("    ","  Total number of contributions= ",contrib_detail[j]['contributions'])
							time.sleep(0.1)
					else:
						print("No committees found.")
					print()
					print()
			else:
				print("No organisation found.")
	print("Do you want to continue? (If yes please enter 1)")
	s = input()
	if(s!='1'):
		print("End")
