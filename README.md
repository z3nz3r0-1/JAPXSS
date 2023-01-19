# JAPXSS
Sometimes, during web application penetration tests, it is necessary to check if the XSS payload works in another page. JAPXSS comes in handy and automates this process.

Example:
  python3 japxss.py -u "https://<YOUR_TARGET>/page1" -v "https://<YOUR_TARGET>/page2" -d "name=kevin&surname=lin&sesskey=U8AbkMluUu" -j name -w wordlist.txt --cookie "sessiontoken=75e6d7f6boa5838aee254d2b69369999"
  
  python3 japxss.py -u "https://<YOUR_TARGET>/page1" -v "https://<YOUR_TARGET>/page2" -d "name=kevin&surname=lin&sesskey=U8AbkMluUu" -j name -w wordlist.txt --output saveFindings.txt
