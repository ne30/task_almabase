# importing all the necessary modules and functions
import time
from repoFunc import top_repo
from contribDet import get_contrib_detail


#Continuous loop until the user want to exit
while(1):

	#takin the organisation name as an input
	print("Enter the organisation name:")
	orgName = input()
	
	#Limiting the api per_page response to max 30, it can be extended
	repoCount = 31
	while (repoCount>30):

		#Input of the number of top repositories user want to check
		print("Enter the total number of top repositories you want to check: (limited to 30)")
		repoCount = int(input())

		#Checking the limits of repoCount
		if (repoCount>30):
			print("Entered value is not servicable")
		else:
			print("Loading...")

			#Calling the function so that the api calling can be done
			details = top_repo(orgName,repoCount)

			#Input of the number of top committees which user want to check
			print("Enter the number of top committees which you want to see:")
			commCount = int(input())

			#Checking the validity of the return value, i.e. if details is none then api didn't got the expected results 
			if details is not None:

				print("Here are the repositories.")
				
				#As the result was in JSON format so getting the 'items' and storing in a list (arr)
				arr = details['items']

				#storing the minimum value as there may be case in which the organisation may have lesser number of repositories then the expexted repositories by the user
				value = min(repoCount,len(arr))
				

				for i in range(value):

					#printing the repo name
					print((i+1),"-> ", arr[i]['name'])

					#total number of forks on that particular repository
					print("Total number of forks", arr[i]['forks'])
					print("Details of top m or all the committees with their commit counts:")
					
					#Storing the api url got from first call to other API endpoint, to get the respective repository further details.
					api_url_base_contrib = arr[i]["contributors_url"]
					
					#Calling the function so that the api calling can be done
					contrib_detail = get_contrib_detail(api_url_base_contrib, commCount)

					#Checking the validity of the return value, i.e. if details is none then api didn't got the expected results 
					if contrib_detail is not None:

						#storing the minimum value as there may be case in which the repository may have lesser number of committees than the user expects
						value = min(commCount,len(contrib_detail))
						
						for j in range(value):
							#Printing the committee user name on Github (further actual name of committee can be accessed by another API call)
							print("    ",(j+1), "-> ",contrib_detail[j]['login'])
							print("    ","  Total number of contributions= ",contrib_detail[j]['contributions'])
							
							#Callin sleep function
							time.sleep(0.1)
					else:
						#In case if there are no committees
						print("No committees found.")
					print()
					print()
			else:
				#In case there is no organisation by the name entered by user
				print("No organisation found.")

	#To continue for other organisation search
	print("Do you want to continue? (If no please enter n else press any key)")
	s = input()

	#If user wants to exit
	if(s=='n' or s=='N'):
		print("Exiting")
		break
