# edibo_site
### Flask tutorials
#### Articles
* [habr](https://habr.com/ru/post/346306/)
* [Wikibooks](https://ru.wikibooks.org/wiki/Flask#%D0%A8%D0%B0%D0%B3_0:_%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BA%D0%B0%D1%82%D0%B0%D0%BB%D0%BE%D0%B3%D0%BE%D0%B2)
* [Flask russian](https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html#quickstart)
* [Pythonru](https://pythonru.com/uroki/1-vvedenie-vo-flask)

#### Books
* Flask Web Development, 2nd Edition (habr link is translation of this book)

#### Video course 
* [Олег Молчанов Flask course](https://www.youtube.com/watch?v=Y_oyx36AdV0&list=PLlWXhlUMyooZr5R2u2Zwxt6Pw6iwBo5y5&index=1)
# Virtualenv
> 




> Step 1: Update your repositories
* `sudo apt-get update`
* `sudo apt install python3.8`
* `sudo apt install python3-venv` 
> Step 2: Install pip for Python 3
* `sudo apt-get install build-essential libssl-dev libffi-dev python-dev`
* `sudo apt install python3-pip`

> Step 3: Use pip to install virtualenv (if not installed)
`sudo pip3 install virtualenv`
---
> Step 4: Launch your Python 3 virtual environment, here the name of my virtual environment will be env3
* `virtualenv -p python3 <name-env>` or
* `> python3 -m venv <name-env>` (work for me)
> Step 5: Activate your new Python 3 environment. There are two ways to do this
* `---> (dote forward) . <name-env>/bin/activate` or
*  `source <name-env>/bin/activate` which does exactly the same thing

> you can make sure you are now working with Python 3
`python -- version`
>

> this command will show you what is going on: the python executable you are using is now located inside your virtualenv repository
`which python `

> Step 6: code your stuff
`...`

> Step 7: done? leave the virtual environment
`deactivate`

--- 
P.S. Some commands could be wrong. Check it out.
