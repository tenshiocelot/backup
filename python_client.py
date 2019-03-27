import argparse
import requests

def Main():
	parser = argparse.ArgumentParser()
	
	parser.add_argument("-u","--user", help = "Your usename", action = 'store_true', default = 'Tenshiocelot'), 
	parser.add_argument("-l", "--list-repos", help = "Fetch and lists your repos", action = "store_true")
	parser.add_argument("-r", "--repos", help = "Fetch your repo and present an stdout", action = "store_true")
	parser.add_argument("-p", "--pull-requests", help = "Prints open pull requests for repo", action = "store_true")


	args = parser.parse_args()

	print(args)

	if args.user != "Tenshiocelot":
		args.user = input('Username: ')

	print(args)

if __name__ == '__main__':
	Main()