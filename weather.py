import requests

url = 'https://api.weatherbit.io/v2.0/forecast/daily?city=Delhi&key=71959c3e875c4f8281c3bbf21de8337d&days=2'
res = requests.get(url)
data = res.json()

def weather_info(msg):
	if 'today' in msg:
		temp = data['data'][0]['high_temp']
		return(temp)
	elif 'tomorrow' in msg:
		j = data['data'][1]['high_temp']
		return(j)
	else:
		return("I am still under development")

