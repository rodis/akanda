UNAME := $(shell uname)
DEV_DIR = ~/lab/DreamHost/dhc
PYPF_DIR = $(DEV_DIR)/pypf
AKANDA_DIR = $(DEV_DIR)/akanda
PYPF_INSTALL = /usr/local/lib/python2.7/site-packages/pypf
PYPF_URL = git@github.com:dreamhost/pypf.git
USER = oubiwann
PYTHON = /usr/local/bin/python
GIT = /usr/local/bin/git
TWISTD = /usr/local/bin/twistd
PF_HOST ?= 10.0.4.186

system-setup:
	pw user mod $(USER) -G wheel

install-ports:
	portsnap fetch
	portsnap extract

update-ports:
	portsnap fetch
	portsnap update

$(PYTHON):
ifeq ($(UNAME), FreeBSD)
	cd /usr/ports/lang/python && make install clean
endif
ifeq ($(UNAME), OpenBSD)
	pkg_add -i python
endif

$(GIT):
ifeq ($(UNAME), FreeBSD)
	cd /usr/ports/devel/git && make install clean
endif
ifeq ($(UNAME), OpenBSD)
	pkg_add -i git
endif

$(TWISTD):
ifeq ($(UNAME), FreeBSD)
	cd /usr/ports/devel/py-twisted && make install clean
endif
ifeq ($(UNAME), OpenBSD)
	pkg_add -i py-twisted-core
endif

$(DEV_DIR):
	mkdir -p $(DEV_DIR)

$(PYPF_DIR):
	-cd $(DEV_DIR) && git clone $(PYPF_URL)

# This assumes running as root
$(PYPF_INSTALL): $(DEV_DIR) $(PYPF_DIR)
	cd $(PYPF_DIR) && python setup.py install

install-dev: $(PYTHON) $(GIT) $(TWISTD) $(PYPF_INSTALL)
ifeq ($(UNAME), FreeBSD)
	@echo "Be sure you have pf enabled on your system:"
	@echo " * edit your /etc/rc.conf"
	@echo " * add rules to /etc/pf.conf"
	@echo " * start pf: sudo /etc/rc.d/pf start"
	@echo
	@echo "To use the dev targets, you will need to edit your"
	@echo "/etc/ssh/sshd_config to allow remote login for root"
	@echo "and then you'll need to restart ssh:"
	@echo "  /etc/rc.d/sshd restart"
	@echo
endif

push-dev:
	git push
	ssh root@$(PF_HOST) \
	"cd $(AKANDA_DIR) && git pull && python setup.py install"

check-dev: push-dev
	ssh root@$(PF_HOST) "cd $(AKANDA_DIR) && python -c \
	'from akanda import scripts;scripts.run_all()'"
