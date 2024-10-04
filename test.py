import requests

url = 'http://localhost:5000/classify'
data = {'text': 'new messagepassing scheme mrf optimization proposed paper scheme inherits better theoretical property stateoftheart message passing method practice performs equally welloutperforms based powerful technique dual decomposition lead elegant general framework understandingdesigning messagepassing algorithm provide new insight existing technique promising experimental result comparison state art demonstrate extreme theoretical practical potential approach'}
response = requests.post(url, json=data)

print(response.json())
