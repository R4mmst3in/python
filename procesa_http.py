import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com','https//api.github.com/invalid']:
	try:
		r = requests.get(url)
		r.raise_for_status()

	except HTTPError as http_err:
		print(f'HTTP error ocurred: {http_err}')

	except Exception as err:
		print(f'Other error ocurred {err} {r.status_code}')

	else:
		print(f'Success {r.status_code} !!!')
