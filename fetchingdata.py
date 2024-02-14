import requests

def fetchandsave(url, path):
    r=requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

url="https://hprera.nic.in/PublicDashboard"
fetchandsave(url, "data/Dashboardinfo.html")

