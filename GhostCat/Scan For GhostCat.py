import requests

def check_ghostcat_vulnerability(url):
    try:
        response = requests.get(url)
        if "CVE-2020-1938" in response.text:
            return url + " is vulnerable to GhostCat."
        else:
            return url + " is not vulnerable to GhostCat."
    except Exception as e:
        return str(e)

print("Ex: https://google.com")
url = input('Enter URL To Scan For GhostCat Vulnerability: ')
vulnerability_status = check_ghostcat_vulnerability(url)
print(vulnerability_status)