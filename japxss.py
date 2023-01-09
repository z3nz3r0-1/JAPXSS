# Author: z3nz3r0
#!/usr/bin/python3

from Utils import Utils
from RequestManager import RequestManager
import time, threading
import numpy as np
from progress.bar import Bar

def requestBlock(rm, payloads, params):
	bar = Bar('Sending requests and check for vulns...', max=len(payloads), fill='@', suffix='%(percent).1f%% - %(eta)ds')
	for payload in payloads:
		rm.sendPayload(payload)
		time.sleep(params.sleep)
		rm.checkVuln()
		bar.next()
		
def main():
	mc = Utils()
	params = mc.getParams()
	if mc.checkParams():
		rm = RequestManager(params, mc)
		wordlist = mc.readWordlist()
		payloads = []
		for payload in wordlist:
			payloads.append(payload.lstrip().rstrip())
		
		if params.thread:
			payloads = np.array_split(np.array(payloads), params.thread)
			for payloadGroup in payloads:
				threading.Thread(target=requestBlock, args=(rm, payloadGroup, params,)).start()
		else:
			threading.Thread(target=requestBlock, args=(rm, payloads, params, )).start()
						
if __name__ == '__main__':
    main()
