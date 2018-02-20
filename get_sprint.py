import requests
import json
import base64

#dump = json.dumps(j, indent = 4)
def scrape(username, password, company, board):

	text = ""
	url = "https://" + company.lower() + ".atlassian.net/rest/api/2/search?jql=Sprint in openSprints()"

	userpass = username + ":" + password
	userpass_64 = base64.b64encode(userpass)

	HEADER = {"Authorization": "Basic {}".format(userpass_64)}
	response = requests.get(url, headers=HEADER)

	try:
		j = json.loads(response.text)
		
		dump = json.dumps(j, indent = 4)
		#print dump

		total = j["total"]
		i = 0

		while (i < total):
			key = j["issues"][i]["key"]
			name = j["issues"][i]["fields"]["summary"]
			status = j["issues"][i]["fields"]["status"]["statusCategory"]["name"]
			
			if (key.split("-")[0].lower() == board.lower()):
				text += "\n" + key + ", " + name + ", " + status

			i += 1
		
		text += "\n"
			
	except ValueError:
		text = "Error: account does not exist"
		
	return text