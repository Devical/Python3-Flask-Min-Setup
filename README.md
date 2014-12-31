Python3 + Flask Setup on Fedora 21
=======================

Bare minimum files and instructions for setting up a Python3 Flask environment for Fedora. Assumes requirements of: Vhost, VirtualEnvironment, Fedora 21, Flask, Apache(mod_wsgi).

<blockquote><strong>Note:</strong> Do not copy-paste everything. This is neither a production nor development setup.</blockquote>

This walk-along (doing this while typing walkthrough) and associated files cater to those having a difficult time setting up Flask for their new machine. Some parts of the code are not needed on production (debug=True), while other parts are not needed for development (activate_this.py), and even still, some parts are 'just because' (etc/hosts).

To emphasise; we're only trying to get 'Hello World!' working with a virtual environment and virtual host. You can take what you want and build your Flask application from there.

While this is in Fedora 21, the same ideas work with other distros.

<h2>What Does Fedora 21 Give You?</h2>

<blockquote><strong>Note:</strong> If you get that stupid 'not a COM32R image' error when booting Fedora from an usb drive, just hit <strong>Tab</strong> and type in an option it gives you (mine was 'linux0').</blockquote>

Fedora 21 (Workstation) comes with many tools already installed for development. Here are a few of note.
<ul>
  <li>Apache</li>
  <li>Python3.4</li>
  <li>Pip3</li>
  <li>Pyvenv-3.4</li>
  <li>Git</li>
  <li><a href='http://fedoraproject.org/wiki/Releases/21/ChangeSet'>And Much More</a></li>
</ul>

This is great! The less we have to install, the faster our setup. Install these packages if your distro doesn't have.

<h2>Make Yourself at Home.</h2>

Make Fedora your... workstation... Do all the things you would normally do before development.
<ul>
  <li>sudo yum update</li>
  <li>Custom Git Bash Prompt</li>
  <li>Install Text Editor (Vim for me)</li>
  <li>Install Favorite Browser</li>
  <li>Install/Setup Database You'll be Using</li>
  <li>Crack Your Knuckles</li>
  <li>Any Other Sacred Rituals...</li>
</ul>

<h2>Install Mod_wsgi and Python3-devel</h2>
Nothing like one-liners to pick up python modules.
```cli
sudo yum install python3-mod_wsgi python3-devel -y
```

<h2>Build File/Folder Structure</h2>

There are some extra files in the repository that don't belong. Below is what your project folder should look like.

<pre>
yourpojectname/
    app/
        static/
        templates/
        __init__.py
    yourprojectname.wsgi
</pre>

To make things easier, I'm going to install this project in the /var/www/ directory. Note that you will need to know your user/group from Fedora setup.

```cli
cd /var/www
sudo mkdir yourprojectname
sudo chown user:group yourprojectname/
cd yourprojectname/
mkdir app
mkdir app/static
mkdir app/templates
touch app/__init__.py
touch yourprojectname.wsgi
```

<h2>Setup Virtual Environment</h2>
Name your virtual environment whatever you want. Typical is just 'venv'.
```cli
pyvenv-3.4 venv
```

<h2>Install Flask on Virtual Environment</h2>
Activate virtual environment and install Flask with pip3
```cli
source venv/bin/activate
```
Should see your prompt change with '(venv)' at the beginning. Now install Flask.
```cli
pip3 install Flask
```
Then get out of your virtual environment
```cli
deactivate
```
<h2>Edit __init__.py</h2>
Yep, the simple "Hello World" from Flask
```cli
vim app/__init__.py
```
Here is the code: (for you lazy people)
```Python
#! /usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == "__main__":
    app.run(debug=True)
```
<blockquote>
<strong>People only needing development:</strong><br>
You're done here. Simply log into your virtual environment and run __init__.py (the code below)
<br>
Your server will be running (127.0.0.1:5000 typically) and you can develop your app from there.
</blockquote>
```cli
source venv/bin/activate
source app/__init__.py
```
For everyone else, let's keep going.

<h2>Make Apache and Mod_WSGI Work Together</h2>
<blockquote>See these files in the repository</blockquote>
Tell your local machine that if you type in 'yourprojectname.dev' into the address bar, look for something other than external website.
```cli
sudo vim /etc/hosts
```
Create new vhosts.conf file. It points to the .wsgi file.
```cli
sudo vim /etc/httpd/conf.d/vhosts.conf
```
The .wsgi file is basically a front controller for Python.
```cli
vim yourprojectname.wsgi
```
Jump into your venv/bin/ folder and add activate_this.py. This file is not with Python3 (pyvenv-3.4). You must create this file.
```cli
vim venv/bin/activate_this.py
```
<h2>Clean-Up and Launch</h2>
Couldn't get much simpler. Restart your Apache.
```cli
sudo service httpd restart
```
Then go to your browser and check out yourprojectname.dev




