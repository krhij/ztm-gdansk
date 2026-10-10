import requests
import time
import datetime
import os

url = "https://ckan2.multimediagdansk.pl/gpsPositions"

#stworzenie katalogu do zapisu
os.makedirs("data", exist_ok=True)

#to jedna godzina
work_time_seconds = 300


def write_data(data):
    now = datetime.datetime.now()
    save_file = now.strftime("%Y-%m-%d")
    save_path = f"data/{save_file}.jsonl"
    with open(save_path, "a", encoding="utf-8") as file:
                file.write(data.text + "\n")



def get_data(url):
    try:
        response = requests.get(url,timeout = 10)
        #obsluga timeout
        if (response.status_code == 429):
            time.sleep(15)
            return get_data(url)
        if response.status_code == 200:
            write_data(response)
    except Exception as e:
        print("error occured: ", e)
    

start_time = time.time()
while time.time() - start_time < work_time_seconds:
    get_data(url)
    time.sleep(20)
    print('\n', "READ ROUND DONE",'\n')

print('\n', "FINISHED",'\n')