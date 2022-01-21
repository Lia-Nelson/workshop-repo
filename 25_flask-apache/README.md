# how-to :: DEPLOY A FLASK APP ON APACHE2
---
## Overview
Guide to creating a deploying a Flask app on Apache2

### Estimated Time Cost: 30 minutes

### Prerequisites:
- A Digital Ocean account with a payment method
- You are breathing

## Instructions (Two Different Methods)

### Deploying Flask app with virtual host
1. Enable mod_wsgi
   ```
   sudo apt-get install libapache2-mod-wsgi-py3 python-dev
   ```
   ```
   sudo a2enmod wsgi 
   ```
2. Create flask app (replace FlaskApp with name you would like to give)
   ```
   cd /var/www
   ```
   ```
   sudo mkdir FlaskApp
   ```
   ```
   cd FlaskApp
   ```
    ```
   sudo mkdir FlaskApp
   ```
   ```
   cd FlaskApp
   ```
   ```
   sudo mkdir static templates
   ```
   Add the contents of your flask app into __init__.py
   ```
   sudo nano __init__.py 
   ```
   ```
   from flask import Flask
   app = Flask(__name__)
   @app.route("/")
   def hello():
   	return "Hello, I hate Digital Ocean!"
   if __name__ == "__main__":
   	app.run()
   ```
3. Install Flask
   ```
   sudo apt-get install python3-pip 
   ```
   ```
   sudo pip3 install virtualenv 
   ```
   replace venv with the name of virtual environment
   ```
   sudo virtualenv venv
   ```
   ```
   source venv/bin/activate 
   ```
   ```
   sudo pip3 install Flask 
   ```
   Test if you installed it
   ```
   sudo python3 __init__.py 
   ```
4. Configure and enable virtual host (note again that all the FlaskApp -> <your_new_name>)
   ```
   sudo nano /etc/apache2/sites-available/FlaskApp.conf
   ```
   Change mywebsite.com to the IP, and FlaskApp to name of your flask app
   ```
   <VirtualHost *:80>
		ServerName mywebsite.com
		ServerAdmin admin@mywebsite.com
		WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
		<Directory /var/www/FlaskApp/FlaskApp/>
			Order allow,deny
			Allow from all
		</Directory>
		Alias /static /var/www/FlaskApp/FlaskApp/static
		<Directory /var/www/FlaskApp/FlaskApp/static/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
   </VirtualHost>
   ```
   Enable Virtual Host
   ```
   sudo a2ensite FlaskApp
   ```
5. Create WSGI file 
   ```
   cd /var/www/FlaskApp
   ```
   ```
   sudo nano flaskapp.wsgi 
   ```
   ```
   #!/usr/bin/python
   import sys
   import logging
   logging.basicConfig(stream=sys.stderr)
   sys.path.insert(0,"/var/www/FlaskApp/")

   from FlaskApp import app as application
   application.secret_key = 'Add your secret key'
   ```
6. Apply changes
   ```
   sudo service apache2 restart 
   ```
You should be able to access your virtual host at your ip. 

### IMPORTANT!!! How to deploy more complicated apps (with multiple files and db files)
There are three important new things to account for as your app gets larger...
1. First off, (I think) you have to move the stuff from the app directory into your innermost FlaskApp directory so apache(2) can most easily find the init file. The quick way to do this is by using scp -r to move your app folder into your outermost FlaskApp folder and just changing the name (but remember to bring along your requirements.txt file for the venv).
2. Second!! For some odd reason, it's hard for apache to find your local helper .py files (locally imported modules). So, at the top of the file that imports all the local modules (generally __init__.py), add the following code:
	```
	import sys
	sys.path.append("/var/www/FlaskApp/FlaskApp")
	```
3. Third (And finally)! Change the permissions on the database file so that apache can definitely access it.
	* Change the owner of the db file to apache
	```
	sudo chown www-data:www-data db_file.db
	````
	* Put the db file in its own directory to be sure the permissions 100% change properly- you can call the directory tmp
	```
	cd /var/www/FlaskApp/FlaskApp
	sudo mkdir tmp
	sudo mv db_file.db tmp/db_file.db
	```
	* Change all the "db_file.db" to "tmp/db_file.db" in your code
	* Change the permssions of the folder to rwx for user and rx for everyone else
	```
	sudo chmod 755 tmp
	```
	* Now all the priviledges should be in place so restart server
	```
	sudo service apache2 restart
	```
If it still doesn't work, run the following to see what the other errors are 
```
sudo cat /var/log/apache2/error.log
```


## Other

### Add your first app on the droplet by running the app normally (easier, fewer spots for errors, but when you exit, the process ends)
1. Clone your workshop repo onto the new machine (use http unless you want to add a key to the VM)
   ```
   git clone https://github.com/<your_username>/<workshop_repo_name>.git
   ```
2. Before doing anything else, type in the following commands so that python3 works while running flask
   ```
   sudo apt-get update
   sudo apt-get upgrade
   sudo apt-get install python3-pip
   sudo apt-get install python3-dev
   sudo apt-get install python3-setuptools
   sudo apt-get install python3-venv
   sudo apt-get install build-essential libssl-dev libffi-dev
   sudo apt-get install libapache2-mod-wsgi-py3
   ```
3. Find the code for the simplest version of a flask app– perhaps k09?- and cd into that directory
    ```
    cd <workshop_repo_name>/<app_you_want>
    ```
4. Make and activate a virtual environment in that directory
    ```
    python3 -m venv <environment_name>
    source <environment_name>/bin/activate
    ```
5. Use pip install to get some basic packages 
    ```
    pip install wheel 
    pip install flask
    pip install uwsgi
    pip install requests
    ```
OR (if the directory has a requirements.txt)
    ```
    pip install -r requirements.txt
    ```

6. Make a quick change to where your app loads- open up the file that runs the app (should be app.py) and put '0.0.0.0' in the run parentheses
    ```
    nano (or vim...) app.py
    ```
  Then: scroll to the ```if __name__ == "__main__"``` and alter ```app.run``` to 
  ```app.run(host='0.0.0.0')```

7. Enable traffic on port 5000 on the ufw firewall (default flask port)
    ```
    sudo ufw allow 5000
    ```
7. Run the app
    ```
    python3 app.py
    ```
8. Check if the app worked on port 5000 of your droplet (hopefully it does!!)

### Resources
* https://pythonforundergradengineers.com/flask-app-on-digital-ocean.html
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
* https://stackoverflow.com/questions/46208907/flask-operationalerror-unable-to-open-database-file
* https://www.digitalocean.com/community/questions/python-can-t-find-local-files-modules
---

Accurate as of (last update): 2022-01-18

#### Contributors:  
Eliza Knapp, pd2  
Andrew Juang, pd2  
Noakai Aronesty, pd2
