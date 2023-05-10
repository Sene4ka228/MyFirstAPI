#Arsēnijs Derbušs
#10.05.2023
#savienojums ar API domēnu
import requests

base_url = 'https://api.chucknorris.io/'

# 1. Pieprasījuma mērķis: Iegūt random joku par Čaku Norisu. Pamatojums: Lietotājs varēs iegūt nejaušo joku par Čaku Norisu.
def get_random_joke():
    endpoint = 'jokes/random'
    url = f'{base_url}{endpoint}'
    response = requests.get(url)
    data = response.json()
    return data
joke_data = get_random_joke()
print("1.pieprasījums:")
print(joke_data['value'])



# 2. Pieprasījuma mērķis: Iegūt sarakstu ar iespējamām kategorijām, kurās ir sadalīti joki par Čaku Norisu.Pamatojums: Es uztaisīju šo pieprasījumu, jo šādi var iegūt visas joku kategorijas. Lietotājs varēs izvēlēties kategoriju, pēc kuras viņš gribēs lasīt jokus
def get_categories():
    endpoint = 'jokes/categories'
    url = f'{base_url}{endpoint}'
    response = requests.get(url)
    data = response.json()
    return data

categories_data = get_categories()
print("2.pieprasījums:")
for category in categories_data:
    print(category)

# 3. Pieprasījuma mērķis: Iegūt joku pēc kategorijas. Pamatojums: Lietotājs grib redzēt joku no kategorijas "mūzika"
def get_joke_by_category(category):
    endpoint = f'jokes/random?category={category}'
    url = f'{base_url}{endpoint}'
    response = requests.get(url)
    data = response.json()
    return data
category = 'music'
print("3.pieprasījums:")
joke_data = get_joke_by_category(category)
print(joke_data['value'])