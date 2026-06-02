import requests
try:
    r=requests.get('https://wttr.in/?format=j1',timeout=5)
    data=r.json()
    print('Temperature:',data['current_condition'][0]['temp_C'])
except Exception as e:
    print('Error:',e)
