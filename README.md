# A simple HTTP server in python for web development

Set up a very simple HTTP server for testing your AJAX-calls without having
to use something like MAMP or LAMP. 

Only programmed with UNIX based systems in mind. 

## Features

* Set custom hostnames. Automaticly alters the ```/etc/hosts``` file and adds host if it does not exist. Default value is to use local ip (127.0.0.1)
* Select port to use. Default value is 8080. 
* Automaticly opens your default browser to the given host.

# Installation

Run the ```sudo make install``` command. This will copy the script to a hidden folder in your home directory, and make a symbolic link in your ```/usr/bin``` directory. If you are skeptical of running sudo commands on the bash script, take a look in the Makefile to see full list of commands.  

To uninstall use the ```sudo make uninstall``` command. Or run

```bash
rm -rf ~/.simplserv
rm -f /usr/bin/simplserv
```

# Usage

```bash
$ simplserv -h

usage: simplserv [-h] [-v] [-p PORT] [-host HOSTNAME]

Start a simple HTTP server, for simpler testing of AJAX calls, 
pathing of files and auto adding host name.

optional arguments:
  -h, --help      show this help message and exit
  -v, --version   show program's version number and exit
  -p PORT         The port to use for the HTTP server
  -host HOSTNAME  Hostname alias
```

### Example:
```bash
$ simplserv -host simplserv.dev -p 8800
Serving at http://simplserv.dev:8800/
localhost - - [27/Feb/2012 15:34:52] "GET / HTTP/1.1" 200 -
localhost - - [27/Feb/2012 15:34:52] code 404, message File not found
localhost - - [27/Feb/2012 15:34:52] "GET /favicon.ico HTTP/1.1" 404 -
```

If you are using a custom hostname for the first time, you probably need to run the command as sudo, as it requires premissions to the ```/etc/hosts``` file. You can omit sudo the second time of running, though. 