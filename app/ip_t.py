import requests

print("""
██╗██████╗░░░░░░░██████╗░██╗██████╗░░█████╗░████████╗███████╗
██║██╔══██╗░░░░░░██╔══██╗██║██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║██████╔╝█████╗██████╔╝██║██████╔╝███████║░░░██║░░░█████╗░░
██║██╔═══╝░╚════╝██╔═══╝░██║██╔══██╗██╔══██║░░░██║░░░██╔══╝░░
██║██║░░░░░░░░░░░██║░░░░░██║██║░░██║██║░░██║░░░██║░░░███████╗
╚═╝╚═╝░░░░░░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
""")
ip = input("Enter IP To Scan: ")
url = f"https://ipinfo.io/{ip}?token=89eb984d917dd5"
response = requests.get(url).json()

print("IP:", response['ip'])
print("\n")
print("ADDRESS:")
print("Country Code:", response['country'])
print("Region Name:", response['region'])
print("City:", response['city'])
print("\n")
print("POSTAL/TIMEZONE:")
print("Postal Code:", response['postal'])
print("Timezone:", response['timezone'])
print("\n")
print("LAT/LONG")
print("Location:", response['loc'])