import requests


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)


download("https://stimg.cardekho.com/images/carexteriorimages/360x240/Nissan/Nissan-Terrano/1556018048112/047.jpg")
print("done...")
