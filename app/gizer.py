import os
import argparse
import socket
import requests

# Get IP and Country from a URL using freegeoip online service
def get_ip_country_freegeoip(url):
	print("FreeGeoIP: " + url + ": ", end='')
	r = requests.get("http://freegeoip.net/json/"+url)
	if not r.status_code // 100 == 2:
		print("Unexpected response from FreeGeoIP {}".format(r))
		return [url, "", ""]
	answer = r.json()
	print(answer.get('ip') + " - " + answer.get('country_name'))
	return [url, answer.get('ip'), answer.get('country_name')]

# Get IP and Country from a URL using the geolite database
def get_ip_country_geolite(url):
	print("Geolite: " + url + ": ", end='')
	reader = geolite2.reader()
	try:
		ip = socket.gethostbyname(url)
	except socket.gaierror:
		print("For URL: "+ url + " : Error: Couldn't get IP")
		return [url, "", ""]
	match = reader.get(ip)
	country = match.get('country').get('names').get('en')
	print(ip + " - " + country)
	return [url, ip, country]

def setupargs(parser):
	parser.add_argument("--list", help="The file containing the list of newline-seperated urls you want to parse")
	parser.add_argument("--url", help="The URL you want to check")
	parser.add_argument("--geolite", help="Use geolite local database instead", action='store_true')

# Main method
def main():
	parser = argparse.ArgumentParser()
	setupargs(parser)
	args = parser.parse_args()
	if not (args.list or args.url):
		print("No --url or --list argument given: nothing to do.")
		return
	if args.geolite:
		print("Using offline GeoLite database")
		global geolite2
		from geolite2 import geolite2
	else:
		print("Using online FreeGeoIP database")
	if args.list:
		print("Using " + args.list + " as input")
		data = [x.strip() for x in open(args.list)]
		data_ip = []
		if args.geolite:
			data_ip = [get_ip_country_geolite(x) for x in data]
		else:
			data_ip = [get_ip_country_freegeoip(x) for x in data]
		split = os.path.splitext(args.list)
		outfile = split[0] + "_parsed" + ".csv"
		with open(outfile, "w") as out:
			for i in data_ip:
				print(i[0] + "," + i[1] + "," + i[2], file=out)
		print("Written parsed URLs to " + outfile)
	elif args.url:
		if args.geolite:
			get_ip_country_geolite(args.url)
		else:
			get_ip_country_freegeoip(args.url)	

if __name__ == '__main__':
	main()