display_name = "Akanda"
library_name = "akanda"
version = "0.1.0"
author = "Duncan McGreggor"
author_email = "dev-community@dreamhost.com"
license = "BSD"
url = "http://github.com/dreamhost/akanda"
description = "Akanda Appliance"
long_description = "A packet filter appliance for OpenStack deployments."
requires = [
    # XXX twisted pip build fails on OpenBSD because it looks for epoll.h
    #"twisted",
    "txroutes",
    ]
