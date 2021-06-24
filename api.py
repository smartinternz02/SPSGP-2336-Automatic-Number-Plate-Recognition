import requests

url = "https://zyanyatech1-license-plate-recognition-v1.p.rapidapi.com/recognize_url"

querystring = {"image_url":"http://eslamoda.com/wp-content/uploads/sites/2/2014/11/america-carro-600x600.jpg"}

headers = {
    'x-rapidapi-key': "a24b8d6f6bmsh0779b8e14615952p1eff3bjsndead2eb3001a",
    'x-rapidapi-host': "zyanyatech1-license-plate-recognition-v1.p.rapidapi.com"
    }

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)