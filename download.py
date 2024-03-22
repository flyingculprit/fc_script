import requests


def download(url):
    get_responce = requests.get(url)
    file_name = url.split("/")[-1]#to split the words before / 
    #print(file_name)
    with open("sample.jpg","wb") as out_file:
        out_file.write(get_responce.content) #file create and write th message
download("https://wallpapercave.com/wp/wp2318912.jpg")