

# Make executionable
install:
	rm -rf ~/.simplserv
	rm -f /usr/bin/simplserv
	mkdir ~/.simplserv
	cp src/server.py ~/.simplserv/server.py
	chmod +x ~/.simplserv/server.py
	ln -s ~/.simplserv/server.py /usr/bin/simplserv

# Remove all references to system (executables, not repo)
uninstall: 
	rm -rf ~/.simplserv
	rm -f /usr/bin/simplserv

