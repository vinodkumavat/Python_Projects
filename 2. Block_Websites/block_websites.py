import time
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirected = "127.0.0.1"

# websites to block
websites_list = ["www.facebook.com", "facebook.com"]

while True:
    with open(host_path, 'r+') as file:
        content = file.read()
        for website in websites_list:
            if website in content:
                pass
            else:
                file.write(redirected+" "+website+"\n")
    print("Website is blocked")
    time.sleep(2)
