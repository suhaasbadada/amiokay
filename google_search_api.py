import requests, json

api_key = 'AIzaSyB3hybE6Sku91eKuffSmigIYcxovClM9sE'

url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"



def treatment_near_me(query):
	r = requests.get(url + 'query=' + query + '&key=' + api_key)
	x = r.json()
	y = x['results']
	li=[]
	for i in range(len(y)):
		name=y[i]['name']
		lat=(y[i]['geometry']['location']['lat'])
		lng=(y[i]['geometry']['location']['lng'])
		rating=y[i]['rating']
		li.append([name,lat,lng,rating])
	# print(y)
	return li[:4]

