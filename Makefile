install-ports:
	portsnap fetch
	portsnap extract

update-ports:
	portsnap fetch
	portsnap update

install-git:
	cd /usr/ports/devel/git && make install clean

install-twisted:
	cd /usr/ports/devel/py-twisted && make install clean

