import requests
import random

proxy_list = []
with open('raw_proxy_list.txt') as f :
    for line in f:
        proxy_list.append(line.strip())
    working_proxies = []
    not_working_proxies = []
    for i in proxy_list:
        print('IP that is being checked: ', i)
        try:
            proxy = {
                "http":"http://"+i,
                "https":"http://"+i
            }
            res = requests.get('https://linksrt.com', verify=False, proxies=proxy)
            working_proxies.append(i)
        except:
            not_working_proxies.append(i)
            pass

print("Working IPs: ", working_proxies)
print("Not Working IPs: ", not_working_proxies)

# for i in range(3):
#     random_ip = random.choice(working_proxies)
#     print("Random IP selected: ", random_ip)
#
#     try:
#         proxy = {
#             "http": "http://" + random_ip,
#             "https": "http://" + random_ip
#         }
#         res = requests.get('http://ip.jsontest.com/', proxies=proxy)
#         print(f"Request received from following IP:\n {res.text}")
#     except:
#         pass



