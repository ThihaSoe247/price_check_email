import requests
from bs4 import BeautifulSoup
import smtplib
headers_para = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/120.0.0.0 Safari/537.3",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get("https://www.jdsports.co.th/men/mens-footwear/", headers=headers_para)
html = response.content
soup = BeautifulSoup(html, "lxml")
price = soup.find(class_="itemPrice").getText()

price = price.split('THB')[1]
price = price.split(",")
price = price[0]+price[1]
price = price.split(".")[0]
current_price = int(price)
print(current_price)
target_price = 4000
USER = "thihasos14122001@gmail.com"
PASS = "zlzx frox aeya yjct"
RECEIVE = "thiha.so65@rsu.ac.th"
LINK = "https://www.jdsports.co.th/men/mens-footwear/"
if current_price <= target_price:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=USER, password=PASS)
    connection.sendmail(from_addr=USER, to_addrs=RECEIVE, msg="Go Buy the Sneaker from JD Sports.".encode("utf-8"))
