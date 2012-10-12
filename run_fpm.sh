#!/bin/bash

set -e

# Package deb files using fpm.

PROJECTS="
    ceilometer_plugins
    dashboard_plugins
    nova_extensions
    router_appliance
    userapi_extensions
    "

LOGFILE=fpm.log

msg() {
    echo
    echo "================================================================================"
    echo "$*"
    echo "================================================================================"
}

pkgone() {
    typeset proj="$1"

    msg $proj

    rm -f *.deb

    msg "Running sdist"
    python setup.py sdist

    # Generate the deb package
    msg "Running fpm"
    fpm -s python \
        -t deb \
        --vendor "$(python setup.py --author)" \
        --maintainer "$(python setup.py --author-email)" \
        --exclude '*dist-packages/tests/*' \
        --description "$(python setup.py --description)" \
        .

    mv *.deb ../packages

}

show_packages() {
    # Show the details for the package we just created
    msg "Package details"
    for pkg in packages/*.deb
    do
        msg $pkg
        dpkg -I "$pkg"
    done
}

mkdir -p packages

for proj in $PROJECTS
do
    (cd $proj && pkgone $proj && cd ..) 2>&1 | tee ${LOGFILE}.${proj}
done

show_packages 2>&1 | tee $LOGFILE
