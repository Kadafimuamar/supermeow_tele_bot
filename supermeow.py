import requests
import time
import random
import threading

def claim_reward(param_claim, thread_id):
    headers = {
        'accept': 'application/json; indent=2',
        'accept-language': 'id-ID,id;q=0.9,en-ID;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://lfg.supermeow.vip',
        'priority': 'u=1, i',
        'referer': 'https://lfg.supermeow.vip/',
        'sec-ch-ua': '""',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '""',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 13; Redmi Note 8 Build/TQ3A.230901.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/124.0.6367.123 Mobile Safari/537.36',
    }

    url_claim = 'https://api.supermeow.vip/meow/claim?' + param_claim

    while True:
        response = requests.post(url_claim, headers=headers).json()
        balance = response.get('balance', 'N/A')
        print(f'Account: {thread_id} | Your Balance: {balance}')
        rand_delay = random.randint(3700, 4000)
        delay = rand_delay
        for i in range(delay, 0, -1):
            minutes, seconds = divmod(i, 60)
            hours, minutes = divmod(minutes, 60)
            print(f"Account: {thread_id} | Next Claim In : {hours:02d}:{minutes:02d}:{seconds:02d}", end='\r')
            time.sleep(1)
        print("\n")

if __name__ == "__main__":
    param_claims = []
    num_threads = int(input("Enter the number of threads: "))
    for _ in range(num_threads):
        param = input('telegram=6279279513&auth_data=%7B%22query_id%22:%22AAGZM0Z2AgAAAJkzRnaxSO5C%22,%22user%22:%22%7B%5C%22id%5C%22:6279279513,%5C%22first_name%5C%22:%5C%22Bowneey%5C%22,%5C%22last_name%5C%22:%5C%22%5C%22,%5C%22username%5C%22:%5C%22bowneey%5C%22,%5C%22language_code%5C%22:%5C%22en%5C%22,%5C%22allows_write_to_pm%5C%22:true%7D%22,%22auth_date%22:%221717392077%22,%22hash%22:%22982131fa87d9ae30ed0cf6a758175755232bd0ac64966d1464210c240dce4cf2%22%7D')
        param_claims.append(param)

    threads = []
    for i, param_claim in enumerate(param_claims):
        thread = threading.Thread(target=claim_reward, args=(param_claim, i+1))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
