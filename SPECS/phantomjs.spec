# taken from the master branch

%define name	phantomjs
%define version	1.9.8
%define release 2%{?dist}

Summary:	a headless WebKit with JavaScript API
Name:		%{name}
Version:	%{version}
License:	BSD
Release:	%{release}
Packager:	Matthew Barr <mbarr@snap-interactive.com>
Group:		Utilities/Misc
#BuildRoot:  %{_topdir}/BUILDROOT/
Source:		https://bitbucket.org/ariya/phantomjs/downloads/%{name}-%{version}-source.zip
#Source0:	%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: flex
BuildRequires: bison
BuildRequires: gperf
BuildRequires: ruby
BuildRequires: openssl-devel
BuildRequires: freetype-devel
BuildRequires: fontconfig-devel
BuildRequires: libicu-devel
BuildRequires: sqlite-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel

%description
PhantomJS is a headless WebKit with JavaScript API. It has fast and native
support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG. PhantomJS is created by Ariya Hidayat.

%prep
%setup -q

%build
./build.sh --confirm

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/examples
cp bin/%{name} %{buildroot}%{_bindir}/%{name}
cp examples/* %{buildroot}%{_datadir}/%{name}/examples/
cp CONTRIBUTING.md %{buildroot}%{_datadir}/%{name}/
cp ChangeLog %{buildroot}%{_datadir}/%{name}/
cp LICENSE.BSD %{buildroot}%{_datadir}/%{name}/
cp README.md %{buildroot}%{_datadir}/%{name}/

%files
%defattr(0444,root,root)
%attr(0555,root,root)%{_bindir}/%{name}
%{_datadir}/%{name}/

%changelog
* Fri May 15 2015 Valentin Gologuzov <vgologuz@redhat.com>
- added spec from master to produce src.rpm

* Wed Apr 24 2013 Robin Helgelin <lobbin@gmail.com>
- updated to version 1.9

* Thu Jan 24 2013 Matthew Barr <mbarr@snap-interactive.com>
- updated to version 1.8

* Thu Nov 15 2012 Jan Schaumann <jschauma@etsy.com>
- first rpm version
