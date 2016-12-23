#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-saharaclient
Version  : 0.18.0
Release  : 32
URL      : http://tarballs.openstack.org/python-saharaclient/python-saharaclient-0.18.0.tar.gz
Source0  : http://tarballs.openstack.org/python-saharaclient/python-saharaclient-0.18.0.tar.gz
Summary  : Client library for Sahara API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-saharaclient-bin
Requires: python-saharaclient-python
BuildRequires : cliff-python
BuildRequires : cmd2-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : jsonpatch-python
BuildRequires : jsonpointer-python
BuildRequires : jsonschema-python
BuildRequires : keystoneauth1-python
BuildRequires : msgpack-python-python
BuildRequires : openstacksdk-python
BuildRequires : os-client-config-python
BuildRequires : oslo.log-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pyinotify-python
BuildRequires : pyparsing-python
BuildRequires : pytest
BuildRequires : python-cinderclient-python
BuildRequires : python-dev
BuildRequires : python-glanceclient-python
BuildRequires : python-keystoneclient-python
BuildRequires : python-novaclient-python
BuildRequires : python-openstackclient-python
BuildRequires : python3-dev
BuildRequires : requests-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : testrepository-python
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : virtualenv

%description
Python bindings to the OpenStack Sahara API
===========================================

%package bin
Summary: bin components for the python-saharaclient package.
Group: Binaries

%description bin
bin components for the python-saharaclient package.


%package python
Summary: python components for the python-saharaclient package.
Group: Default
Requires: keystoneauth1-python
Requires: oslo.log-python
Requires: prettytable
Requires: python-keystoneclient-python
Requires: python-openstackclient-python
Requires: requests-python
Requires: six-python

%description python
python components for the python-saharaclient package.


%prep
%setup -q -n python-saharaclient-0.18.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sahara

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
