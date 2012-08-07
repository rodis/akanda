LIB = akanda
UNAME := $(shell uname)
DEV_DIR = ~/lab/DreamHost/dhc
PYPF_DIR = $(DEV_DIR)/pypf
TXROUTES_DIR = $(DEV_DIR)/txroutes
AKANDA_DIR = $(DEV_DIR)/akanda
PYPF_INSTALL = /usr/local/lib/python2.7/site-packages/pypf
PYPF_URL = git@github.com:dreamhost/pypf.git
TXROUTES_URL = git@github.com:dreamhost/txroutes.git
AKANDA_URL = git@github.com:dreamhost/akanda.git
USER = oubiwann
PYTHON = python2.7
PIP = /usr/local/bin/pip-2.7
GIT = /usr/local/bin/git
#PF_HOST ?= 10.0.4.186
PF_HOST_UNAME ?= OpenBSD
NOSE= $(PYTHON) $(shell which nosetests-2.7)

clean:
	sudo rm -rfv dist/ build/ MANIFEST *.egg-info
	rm -rfv _trial_temp/ CHECK_THIS_BEFORE_UPLOAD.txt twistd.log
	find ./ -name "*~" -exec rm -v {} \;
	sudo find ./ -name "*.py[co]" -exec rm -v {} \;
	find . -name "*.sw[op]" -exec rm -v {} \;

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

$(DEV_DIR):
	mkdir -p $(DEV_DIR)

$(PYPF_DIR):
	-cd $(DEV_DIR) && git clone $(PYPF_URL)

$(PYPF_INSTALL): $(DEV_DIR) $(PYPF_DIR)
	-cd $(PYPF_DIR) && sudo $(PYTHON) setup.py install

python-deps: $(PYPF_INSTALL)
	sudo $(PIP) install coverage
	sudo $(PIP) install netaddr
	sudo $(PIP) install flask
	sudo $(PIP) install https://github.com/nose-devs/nose/zipball/master
#	sudo $(PIP) install https://github.com/openstack/horizon/zipball/master

install-dev: $(PYTHON) $(GIT) python-deps
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

local-dev-deps:
ifeq ($(PF_HOST_UNAME), FreeBSD)
	ssh root@$(PF_HOST) "cd /usr/ports/net/rsync && make install clean"
endif
ifeq ($(PF_HOST_UNAME), OpenBSD)
	ssh root@$(PF_HOST) "pkg_add -i rsync"
endif

clone-dev:
	git push
	-ssh root@$(PF_HOST) \
	"git clone $(AKANDA_URL) $(AKANDA_DIR)"

push-dev: clone-dev
	git push
	ssh root@$(PF_HOST) \
	"cd $(AKANDA_DIR) && git pull && python setup.py install"

rsync-push-dev: local-dev-deps
	rsync -az -e "ssh . root@$(PF_HOST):$(AKANDA_DIR)/"

scp-push-dev:
	scp -r . root@$(PF_HOST):$(AKANDA_DIR)/
	ssh root@$(PF_HOST) \
	"cd $(AKANDA_DIR) && python setup.py install"

check-dev:
	-make check
	-pep8 $(LIB)
	-pyflakes $(LIB)

check:
	$(NOSE) -v $(LIB)

check-cover:
	$(NOSE) -v --with-coverage --cover-package=$(LIB) --cover-branches

iso:
	"./scripts/create-akanda-livecd.sh"

run-dev:
	$(PYTHON) akanda/routerapi/devserver.py
