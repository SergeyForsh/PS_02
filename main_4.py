import requests

img = "https://sun9-72.userapi.com/s/v1/ig2/dFfXdRcivOT0WmQwtPezcpCxxswf9cWveo8BfAI9oqxQ8xVGAAZdZ36gdR6D1vHTXIEcuKnaVgI9By9O6Vz2l8Ow.jpg?quality=96&as=32x48,48x72,72x108,108x162,160x240,240x360,360x540,480x720,540x810,640x960,648x972&from=bu&u=hZeIXwlQWJM9j35nhSOeBjnsvXBeIQPz_ZQYyN3HYho&cs=538x807"

response = requests.get(img)

with open('test.jpg', 'wb') as file:
    file.write(response.content)
