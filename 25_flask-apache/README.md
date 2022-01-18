### Add your first app on the droplet! 
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

### Make it run in a nicer place
sudo nano /etc/apache2/sites-available/appname.conf
- paste stuff from second link


### Resources
* https://pythonforundergradengineers.com/flask-app-on-digital-ocean.html
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
---

Accurate as of (last update): 2022-01-11

#### Contributors:  
Eliza Knapp, pd2  
Andrew Juang, pd2  
Noakai Aronesty, pd2
