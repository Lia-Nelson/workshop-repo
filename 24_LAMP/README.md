# how-to :: PROVISION A DIGITAL OCEAN DROPLET, INSTALL UBUNTU 20.04.3, APACHE2 AND ADD YOUR FIRST BASIC APP.
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: 30 minutes - 1 hour

### Prerequisites:
- A Digital Ocean account with a payment method
- You are breathing


## Instructions
### Set up a Droplet
#### We will be using SSH keys because password authentication is less secure. 
1. If you do not have SSH keys create one by typing 
    ```
    ssh key-gen
    ```
    and copying the contents of the key 
    ```
    cat /Users/your_username/.ssh/id_rsa.pub
    ```
2. In https://cloud.digitalocean.com/account/security, click Add SSH Key and copy and paste the contents of your ssh key into it. 
3. Log in to your Digital Ocean account and from the control panel, click Create -> Droplets. We will be using Ubuntu 20.04 with the Basic Plan and Regular Intel with SSD which should cost $5/month. 
4. Create your droplet!!!

### Initial Server Setup With Ubuntu 20.04
1. Connect to the as the root user (you can find the server ip in the droplets page of your Digital Ocean dashboard)
   ```
   ssh root@your_server_ip
   ```
3. Once you are logged in as root, we will add a new account to log into instead of root. (replace your_username with your username)
   ```
   adduser your_username
   ```
4. Grant your account with admin privileges
   ```
   usermod -aG sudo your_username
   ```
   Now you can use sudo on your new account!
5. Set up a basic firewall to make sure only connections to certain services are allowed.
   ```
   ufw allow OpenSSH
   ```
   ```
   ufw enable
   ```
   You can see that SSH connections are allowed by typing
   ```
   ufw status
   ```
   ```Output
   Status: active

   To                         Action      From
   --                         ------      ----
   OpenSSH                    ALLOW       Anywhere
   OpenSSH (v6)               ALLOW       Anywhere (v6)
   ```
   Currently the firewall is only allowing SSH connections!
6. As root on your virtual machine, you will need a copy of your local public key to use the new account
   ```
   rsync --archive --chown=your_username:your_username ~/.ssh /home/your_username
   ```
7. You should be able to log into the new user account by typing
   ```
   ssh your_username@your_server_ip
   ```
You should be good to go to install the apache web server! 

### Install the Apache Web Server on Ubuntu 20.04
1. Install the Apache2 package.
   ```
   sudo apt update
   ```
   ```
   sudo apt install apache2
   ```
2. Adjust firewall to allow access to the default web ports
   ```
   sudo ufw allow 'Apache'
   ```
   Verify the change by typing
   ```
   sudo ufw status
   ```
   ```
   Output
   Status: active
   To                         Action      From
   --                         ------      ----
   OpenSSH                    ALLOW       Anywhere                  
   Apache                     ALLOW       Anywhere                
   OpenSSH (v6)               ALLOW       Anywhere (v6)             
   Apache (v6)                ALLOW       Anywhere (v6)    
   ```
3. Check with the systemd init system to make sure the service is running by typing:
   ```
   sudo systemctl status apache2
   ```
   ```
   Output
    ● apache2.service - The Apache HTTP Server
     Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2020-04-23 22:36:30 UTC; 20h ago
       Docs: https://httpd.apache.org/docs/2.4/
    Main PID: 29435 (apache2)
      Tasks: 55 (limit: 1137)
     Memory: 8.0M
     CGroup: /system.slice/apache2.service
             ├─29435 /usr/sbin/apache2 -k start
             ├─29437 /usr/sbin/apache2 -k start
             └─29438 /usr/sbin/apache2 -k start
   ```
Go to http://your_server_ip, you should see the default Ubuntu 20.04 Apache web page with a red "It Works!" page. 

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
   ```
3. Find the code for the simplest version of a flask app– we recommend 14_form- and cd into that directory
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
* https://docs.digitalocean.com/tutorials/recommended-droplet-setup/
* https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04
* https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-20-04
* https://pythonforundergradengineers.com/flask-app-on-digital-ocean.html
---

Accurate as of (last update): 2022-01-11

#### Contributors:  
Andrew Juang, pd2
Eliza Knapp, pd 2

_Note: the two spaces after each name are important! ( <--burn after reading)  _