import requests, json

class RequestManager():

	def __init__(self, params, Utils):
		self.params = params
		self.Utils = Utils
		self.POST = True if params.requestData else False
		self.urlPayload = params.urlPayload if params.requestData else params.urlPayload[0:params.urlPayload.index('?')]
		self.__initCookies()
		self.__initRequestData()
		
	def __findPayload(self, response, payload):
		if payload in response: return True
		if payload.replace("/","\/") in response: return True
		if payload.replace("\"","\\\"") in response: return True

	def checkVuln(self):
		response = requests.get(self.params.urlVuln, cookies=self.params.cookies)
		if self.__findPayload(response.text, self.params.requestData[self.params.injectParam]):
			if self.params.output: self.Utils.saveFindings(self.params)
			print('\nFounded!! -> ' + self.params.requestData[self.params.injectParam])
			
	def sendPayload(self, payload):
		self.params.requestData[self.params.injectParam] = payload
		if self.POST:
			res = requests.post(self.urlPayload, data = self.params.requestData, cookies = self.params.cookies)
		else:
			textData = ''
			for param in self.params.requestData:
				textData += param + '=' + data[param] + '&'
			requests.get(self.urlPayload + '?' + textData[0:-1], cookies = self.params.cookies)
				
	def __initRequestData(self):
		data = {}
		if self.POST:
			for param in self.params.requestData.split('&'):
				data[param.split('=')[0]] = param.split('=')[1]
		else:
			for param in self.params.urlPayload[self.params.urlPayload.index('?')+1:].split('&'):
				data[param.split('=')[0]] = param.split('=')[1]
		self.params.requestData = data
	
	def __initCookies(self):
		cookies = {}
		if self.params.cookies:
			for cookie in self.params.cookies.split('&'):
				cookies[cookie[0:cookie.index('=')]] = cookie[cookie.index('=')+1:]
		self.params.cookies = cookies
