import requests
import pprint
response = requests.get('https://api.github.com/')
# response = requests.get('https://www.google.com/')
# print(response.status_code)
# print(response.ok)
# if response.ok:
#     print('запрос уcпешно выполнен')
# else:
#     print('произошла ошибка')
print(response.text)
# print(response.content)
response_json = response.json()
pprint.pprint(response_json)

