DEV_DIR = ~/lab/DreamHost/dhc
PYPF_DIR = $(DEV_DIR)/pypf
PYPF_INSTALL = /usr/local/lib/python2.7/site-packages/pypf
PYPF_URL = git@github.com:dreamhost/pypf.git
USER = oubiwann
GIT = /usr/local/bin/git
TWISTD = /usr/local/bin/twistd

system-setup:
	pw user mod $(USER) -G wheel

install-ports:
	portsnap fetch
	portsnap extract

update-ports:
	portsnap fetch
	portsnap update

$(GIT):
	cd /usr/ports/devel/git && make install clean

$(TWISTD):
	cd /usr/ports/devel/py-twisted && make install clean

$(DEV_DIR):
	mkdir -p $(DEV_DIR)

$(PYPF_DIR):
	-cd $(DEV_DIR) && git clone $(PYPF_URL)

# This assumes running as root
$(PYPF_INSTALL): $(DEV_DIR) $(PYPF_DIR)
	cd $(PYPF_DIR) && python setup.py install

install-dev: $(GIT) $(TWISTD) $(PYPF_INSTALL)
	@echo "Be sure you have pf enabled on your system:"
	@echo " * edit your /etc/rc.conf"
	@echo " * add rules to /etc/pf.conf"
	@echo " * start pf: sudo /etc/rc.d/pf start"
