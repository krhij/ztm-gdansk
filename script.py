import requests
import time
import datetime

url = "https://ckan2.multimediagdansk.pl/gpsPositions"

save_file = "data/test.jsonl"

#to jedna godzina
work_time_seconds = 300

now = datetime.now()


def get_data(url):
    try:
        response = requests.get(url,timeout = 10)
        #obsluga timeout
        if (response.status_code == 429):
            time.sleep(15)
            return get_data(url)
        if response.status_code == 200:
            # with open(save_file, "a", encoding="utf-8") as file:
            #     file.write(response.text + "\n")
            write_data(response)
    except Exception as e:
        print("error occured: ", e)
    

def write_data(data):
    save_file = str(now.year+"_"+now.day)
    with open(save_file, "a", encoding="utf-8") as file:
                file.write(data.text + "\n")

start_time = time.time()
while time.time() - start_time < work_time_seconds:
    get_data(url)
    time.sleep(20)
    print('\n', "READ ROUND DONE",'\n')

print('\n', "FINISHED",'\n')