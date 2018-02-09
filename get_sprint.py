import requests
import json
import base64

#dump = json.dumps(j, indent = 4)
def scrape():

	url = "https://bytelion.atlassian.net/rest/api/2/search?jql=Sprint in openSprints()"

	#username = raw_input("What is your username? ")
	#password = raw_input("What is your password? ")

	#userpass = username + ":" + password
	userpass = "sethhdavis99:Newbie33"
	userpass_64 = base64.b64encode(userpass)

	HEADER = {"Authorization": "Basic {}".format(userpass_64)}

	response = requests.get(url, headers=HEADER)

	j = json.loads(response.text)

	total = j["total"]
	i = 0

	while (i < total):
		key = j["issues"][i]["key"]
		name = j["issues"][i]["fields"]["summary"]
		status = j["issues"][i]["fields"]["status"]["statusCategory"]["name"]

		print key + ", " + name + ", " + status

		i += 1
		
scrape()