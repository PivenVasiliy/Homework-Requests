import requests

heroe_url = 'https://superheroapi.com/api/2619421814940190/search/'
heroes_name = [{'name': 'Hulk'}, {'name': 'Thanos'}, {'name': 'Captain America'}]

for name in heroes_name:

    url = requests.get(heroe_url + name['name'])
    name['intelligence'] = int(url.json()['results'][0]['powerstats']['intelligence'])

print('Самый умный герой:', sorted(heroes_name, key=lambda hero: -hero['intelligence'])[0]['name'])

