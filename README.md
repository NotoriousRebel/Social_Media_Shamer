## Social_Media_Shamer
Breaches happen all the time, it would be a shame if people used those credentials for their social media accounts.

### What is this tool?
Written in Python 3.5 and utilizing requests and bs4, this tool takes in a set of credentails or a text file of credentials and runs them against numerous social media sites and determines if they are valid. If entering a text file see example text file. 

### What does it test against at the moment?
Currently just Linkedin and Twitter; however, I am planning to add more. 

### What else?
You can also pass in a custom url and the form data for the login page and the credentials will be tested against that site as well. (soon)

### How to use it?
```pip install -r requirements.txt``` and to run 
```social_media_shamer.py -user username -passw password``` or 
```social_media_shamer.py -f path\to\txtfile -ft```

