import requests
import folium
import webbrowser
import numpy as np
from folium.plugins import MarkerCluster


location = []
while True:

    loc_temp = input("Where to?: ")
    
    if loc_temp == '':
        break
    else:
        location.append(loc_temp)


coordinates = []

for loc in location:
    URL = 'https://maps.googleapis.com/maps/api/geocode/json?key=your_API_key' \
'&sensor=false&language=ko&address={}'.format(loc)

    response = requests.get(URL)

    # JSON 파싱
    data = response.json()

    # lat, lon 추출
    lat = data['results'][0]['geometry']['location']['lat']
    lng = data['results'][0]['geometry']['location']['lng']
    
    coordinates.append([lat, lng])
    
coordinates = np.asarray(coordinates)
# 검색할 주소
m = folium.Map(
    location = [coordinates[:, 0].mean(), coordinates[:, 1].mean()],
    zoom_start = 10
    )

marker_cluster = MarkerCluster().add_to(m)
for idx in range(len(location)):
    folium.Marker(location=coordinates[idx], 
            popup=location[idx], 
            icon=folium.Icon(color = 'blue', icon = 'ok')).add_to(m)
# Save to html
m.save('folium_kr.html')
webbrowser.open_new("folium_kr.html")
