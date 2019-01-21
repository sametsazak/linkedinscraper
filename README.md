# CryingLinked

CryingLinked is an another information gathering tool written in python that scrapes linkedin.com with given company url and generates email addresses

![alt text](https://raw.githubusercontent.com/sametsazak/cryinglinked/master/images/crying.png)

## Install and Usage:

1) First, you need to download Chrome Driver from http://chromedriver.chromium.org/downloads (to your OS(mac,windows or linux)) in same directory.

2) Install requirements via pip3
```
pip3 install -r req.txt
```

3) Start cryinglinked.py

````
python3 cryinglinked.py
````

## How to scrape?:

![alt text](https://raw.githubusercontent.com/sametsazak/cryinglinked/master/images/1.png)
![alt text](https://raw.githubusercontent.com/sametsazak/cryinglinked/master/images/2.png
)

````
list
use 1
info
set username test@test.com
set password testpassword
set url https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%22162479%22%5D
set page 100 (max 100)
generate
````
then it will write Output.csv for you.
Example output.csv:
```
name,title
John Brown, Software Quality and Testing Manager
Emma Watson, Senior Project Manager
...
..
.
```

## How to generate email adresses?:

![alt text](https://raw.githubusercontent.com/sametsazak/cryinglinked/master/images/3.png)

````
list
use 2
info
use 1 (choose email pattern)
info
set Input (default: Output.csv)
set Output (output file exp : Emails.txt)
set Domain (example : test.com) -> test@test.com
generate
````

then it will write Emails.txt for you.

Example emails.txt (pattern 1):
```
john.brown@domain.com
emma.watson@domain.com
```

PS: This script contains very bad code but it works:)



