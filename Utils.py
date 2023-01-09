import argparse,re,os

class Utils:

	def __init__(self):
		self.args = {}

	def getParams(self):
		parser = argparse.ArgumentParser(description='Sometimes it is necessary to check if the payload works in another page. JAPXSS comes in handy and automates this process.', usage='python3 japxss.py -u "https://<YOUR_TARGET>/page1" -v "https://<YOUR_TARGET>/page2" -d "name=kevin&surname=lin&sesskey=U8AbkMluUu" -j name -w wordlist.txt --cookie "sessiontoken=75e6d7f6boa5838aee254d2b69369999"')
		parser.add_argument('--urlPayload', '-u', help='The base URL to send the payload', type=str, required=True)
		parser.add_argument('--urlVuln', '-v', help='The URL used to check for the presence of the payload', type=str, required=True)
		parser.add_argument('--requestData', '-d', help='Data used in the request', type=str)
		parser.add_argument('--injectParam', '-j', help='The variable from requestData used to inject the payload into', type=str, required=True)
		parser.add_argument('--wordlist', '-w', help='The path to the wordlist to use', type=str, required=True)
		parser.add_argument('--cookies', '-c', help='Cookies to use in the request', type=str)
		parser.add_argument('--thread', '-t', help='Number of threads to use for scanning.', type=int)
		parser.add_argument('--sleep', '-s', default=1, help='Waiting time from "sending payload request" and "check for vulnerability". Default 1 second', type=int)
		parser.add_argument('--output', help='Save data to output file', type=str)
		self.args = parser.parse_args()
		return self.args

	def checkParams(self):
		urlRegex = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
		check = 'Error: '
		if not re.match(urlRegex, self.args.urlPayload): 
			check += 'There is an error with the urlPayload'
		if not re.match(urlRegex, self.args.urlVuln):
			check += 'There is an error with the urlVuln'
		if self.args.injectParam not in self.args.requestData: 
			check += 'injectParam was not found in the requestData'
		if not self.__checkPathExist(self.args.wordlist):
			check += 'The wordlist does not exist on the system'
		if len(check) > 7: print(check)
		return False if len(check) > 7 else True
		
	def readWordlist(self):
		wordlistFile = open(self.args.wordlist, "r")
		wordlist = wordlistFile.readlines()
		return wordlist
		
	def __checkPathExist(self, path):
		return os.path.isfile(path)
		
	def saveFindings(self, params):
		saveFile = open(params.output, "a")
		saveFile.write('\nurlPayload: ' + params.urlPayload + ' -- urlVuln: ' + params.urlVuln + ' -- Payload found: ' + params.requestData[params.injectParam])
		saveFile.close()