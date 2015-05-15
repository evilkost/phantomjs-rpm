#!/bin/sh

if [ ! -e SOURCES ]
then
    mkdir -p SOURCES
fi

if [ ! -e SRPMS ]
then
    mkdir -p SRPMS
fi

VERSION="1.9.8-2"
DIST="fc20"


spectool -C SOURCES -g SPECS/phantomjs.spec
rpmbuild --define "_topdir `pwd`" -bs SPECS/phantomjs.spec

mock --new-chroot --dnf --no-cleanup-after --no-clean --resultdir RPMS `pwd`/SRPMS/phantomjs-${VERSION}.${DIST}.src.rpm

