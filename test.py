import requests
from lxml import html

#<input autofocus="" class="override-aui text" id="js-email-field" name="username" maxlength="255" placeholder="Email" type="text" value="">
#<input class="override-aui text" id="js-password-field" name="password" placeholder="Password" type="password">
#<input type="hidden" name="csrfmiddlewaretoken" value="Fa2FSBswo3kqMHth4CW7dCY6tk48eUSMnN1qDOyM2eiwh8ByaquSUYJ9BrQoegMW">

session_requests = requests.session()

login_url = "https://bitbucket.org/account/signin/"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='csrfmiddlewaretoken']/@value")))[0]

email = raw_input("What is your account email? ")
password = raw_input("What is your account password? ")

payload = {"username": email, "password": password, "csrfmiddlewaretoken": authenticity_token}

result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
)

url = 'https://bitbucket.org/dashboard/overview'
result = session_requests.get(url)

print result.text