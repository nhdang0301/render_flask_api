import requests

url = 'https://citeseerxapi.onrender.com'
data = {'text': 'paper propose miml multiinstance multilabel learning framework example described multiple instance associated multiple class label compared traditional learning framework miml framework convenient natural representing complicated object multiple semantic meaning learn miml example propose mimlboost mimlsvm algorithm based simple degeneration strategy experiment show solving problem involving complicated object multiple semantic meaning miml framework lead good performance consideringthat degeneration process may lose information propose dmimlsvm algorithm tackle miml problem directly regularization framework moreover show even access real object thus cannot capture information real object using miml representation miml still useful propose insdif subcod algorithm insdif work transforming singleinstances miml representation learning subcod work transforming singlelabel example miml representation learning experiment show task able achieve better performance learning singleinstances singlelabel example directly'}
response = requests.post(url, json=data)

print(response.json())
